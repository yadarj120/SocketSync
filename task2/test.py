import subprocess
import sys

print(subprocess.run(["pwd"], capture_output=True).stdout)

print(file=sys.stdout, flush=False)