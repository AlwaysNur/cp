import subprocess
import sys

path = sys.argv[1].strip()
# out = sys.argv[2].strip()

# print(path+ "11"+out)
# print(sys.argv)
subprocess.run(["zip", "temp"] + path,shell=True)