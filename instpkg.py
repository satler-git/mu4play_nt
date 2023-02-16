"""install packages"""
import subprocess
subprocess.run("python -m  pip install pychromecast", check=False , shell=True)
subprocess.run("python -m  pip install cx_freeze", check=False, shell=True)
subprocess.run("python -m  pip install django", check=False, shell=True)
