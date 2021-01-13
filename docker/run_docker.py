import glob
import os
import shutil
import sys
import tarfile
import time
from io import BytesIO, StringIO

import docker

DOCKER_IMAGE = "gs_test"

client = docker.from_env()

def copy_to_container(container, artifact_file, path='/autograder'):
    with create_archive(artifact_file) as archive:
        container.put_archive(path=path, data=archive)


def create_archive(artifact_file):
    pw_tarstream = BytesIO()
    pw_tar = tarfile.TarFile(fileobj=pw_tarstream, mode='w')
    file_data = open(artifact_file, 'rb').read()
    tarinfo = tarfile.TarInfo(name=artifact_file)
    tarinfo.size = len(file_data)
    tarinfo.mtime = time.time()
    # tarinfo.mode = 0600
    pw_tar.addfile(tarinfo, BytesIO(file_data))
    pw_tar.close()
    pw_tarstream.seek(0)
    return pw_tarstream


def run_submission(sd, docker_image=DOCKER_IMAGE):
    image = client.images.get(docker_image)
    container = client.containers.create(image, command="/bin/bash", tty=True,
                                         stdin_open=True, auto_remove=False)
    container.start()

    try:

        log = container.exec_run('mkdir /autograder/submission',
                                 stdout=True,
                                 stderr=True,
                                 stream=True)
        for line in log[1]:
            print(line.decode("utf-8"), end='')

        copy_to_container(container, sd, '/autograder/submission')

        #copy_to_container(container, 'run_autograder')
        #container.exec_run('cp /autograder/source/run_autograder /autograder')
        #container.exec_run('chmod ugo+x /autograder/run_autograder')

        container.exec_run(
            'rm -rf /autograder/submission/template/build',
            workdir='/autograder',
            privileged=True)

        log = container.exec_run('timeout 3m /autograder/run_autograder',
                                 stdout=True,
                                 stderr=True,
                                 stream=True,
                                 workdir='/autograder',
                                 privileged=True)
        for line in log[1]:
            print(line.decode("utf-8"), end='')

        st, status = container.get_archive('/autograder/results/results.json')
        ts = BytesIO()
        for d in st:
            ts.write(d)
        ts.seek(0)
        tar = tarfile.TarFile(fileobj=ts, mode='r')
        tar.extractall('results')
    except Exception as E:
        print(E)
    finally:
        # Need to debug? Uncomment this line so it will pause and leave the
        # docker image running.  Then you can docker exec into it to look
        # around.
        #input()
        container.stop(timeout=1)
        container.remove()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        run_submission(sys.argv[1])
    else:
        print("Usage: {sys.argv[0]} [submission.c]")
