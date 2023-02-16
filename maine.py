"""This is a maine program of mu4play."""
import subprocess
import datetime
import sys
import os
import pychromecrast
from pychromecast.controllers.youtube import YouTubeController

class DjangoServer :
    """this class is server class and chromecast class"""
    def __init__(self, wlist,chromecastname) -> None:
        self.ccn = chromecastname
        self.wlist = wlist
        self.count = 0
    def runserver(self) :
        """running django server."""
        subprocess.run("cd" + os.getcwd() + "\\mu4play", shell=True , check=False)
        subprocess.run("python manage.py runserver 0.0.0.0:8000", shell=True, check=False)
    def v2c(self) :
        """video casting to ccn chromecast."""
        def gettime() :
            return [datetime.datetime.now().hour, datetime.datetime.now().minute]
        while not gettime()[0] == 1 and gettime()[1] > 5 :

            chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=self.ccn)

            if not chromecasts:
                print("そんなchromecastはないよ")
                sys.exit(1)
            #caststart
            cast = chromecasts[0]
            cast.wait()

            youtube_cont = YouTubeController()
            cast.register_handler(youtube_cont)
            youtube_cont.play_video(self.wlist[self.count+1])
            browser.stop_discovery()
        return self.count
#maine
