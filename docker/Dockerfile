FROM gradescope/auto-builds:ubuntu-18.04
WORKDIR /autograder

# Setup the container stuff that needs to be installed
#COPY requirements.txt /autograder/source/requirements.txt
COPY source/setup.sh /autograder/source/setup.sh
RUN apt-get update
RUN /autograder/source/setup.sh

# Put in the actual autograder
COPY autograder.zip /autograder/source/
RUN cd /autograder/source && unzip -o autograder.zip && rm autograder.zip

# Get the autograder script ready to run
RUN cp /autograder/source/run_autograder /autograder
RUN chmod ugo+x /autograder/run_autograder

RUN mkdir /autograder/submission