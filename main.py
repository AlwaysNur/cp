import os
import subprocess
import sys
import time
from subprocess import DEVNULL

path = sys.argv[1].strip()
out = sys.argv[2].strip()
zip_name = "/tmp/temp.zip"

subprocess.run(["zip","-j", zip_name, path], stdout=DEVNULL)

subprocess.run(["mv", zip_name, out])

os.chdir(out)

subprocess.run(["unzip", "temp.zip"], stdout=DEVNULL, input=b'y')
subprocess.run("clear", shell=True)
os.remove("temp.zip")
