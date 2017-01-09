import sys
import subprocess32 as subprocess

# Returns True if the files differ
def diff(f1, f2):
	# Run the process
	cmd = "diff -w %s %s"%(f1,f2)
        proc = subprocess.Popen(cmd.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout = "bad"
	stderr = "bad"
        try:
            stdout, stderr = proc.communicate(timeout=10)
        except:
	    sys.exc_clear()

	if stdout == "" and stderr == "":
		return False
	else:
		return True


#print file_differ("a.txt","b.txt")
