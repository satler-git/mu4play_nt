import subprocess
import pychromecrast
import os

class server :
    def __init__(self, list,chromecastname) -> None:
        self.ccn = chromecastname
        self.list = list
        self.count = 0
    def runserver(self) :
        subprocess.run("cd" + os.getcwd() + "\\mu4play", shell=True)
        subprocess.run("python manage.py runserver 0.0.0.0:8000", shell=True)
    def b2c(self) :
        