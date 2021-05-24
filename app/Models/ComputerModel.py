import subprocess
import os

class ComputerModel():
    def openApp(self, app):
        pipe = subprocess.PIPE
        p = subprocess.Popen(app, shell=True, stdin=pipe, stdout=pipe, stderr=subprocess.STDOUT,)
    def Computeroff(self):
        os.system('shutdown -s')
    def CompuerReboot(self):
        os.system('shutwodn /r /t 1')
    def ComputerSleep(self):
        os.system('shutdown /h')