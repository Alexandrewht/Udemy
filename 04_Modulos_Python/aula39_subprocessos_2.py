import subprocess
import sys

# sys.platform = lista o sistema operacional
# linux = linux2,
# mac = darwin,
# windows = win32.
# print(sys.platform)


# linux e mac
cmd = ['ls', '-lah', '/']
encoding = 'latin1'
system = sys.platform

# se for windows, irá executar
if system == 'win32':
    cmd = ['ping', '127.0.0.1']
    encoding = 'cp850'

proc = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding= encoding,
    shell=True
)
print()
# print(proc.args)
# print(proc.stderr)
print(proc.stdout)
# print(proc.returncode)