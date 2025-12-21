import subprocess

def convert(o, i):
    subprocess.run(["tools/docify","{o}","{i}"])