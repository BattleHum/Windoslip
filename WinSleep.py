import subprocess


def fullOff():
    subprocess.call(["shutdown", "/s", "-t", time])

def saveprogress():
    subprocess.call(["shutdown", "/h", "-t", time])

def restart():
    subprocess.call(["shutdown", "/r", "time", time])
