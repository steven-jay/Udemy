import time
from datetime import datetime as dt
import subprocess

hosts = '/etc/hosts'
redirect = '127.0.0.1'
websites = ['www.facebook.com', 'espnfc.com', '9gag.com', 'www.xkcd.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() \
        < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        for website in websites:
            try:
                subprocess.check_output('cat /etc/hosts | grep %s' % (website), shell=True) #check if website is in hosts file
            except subprocess.CalledProcessError: #if not in hosts file, add it to hosts file
                command = 'echo %s %s >> /etc/hosts' % (redirect, \
                website)
                subprocess.call(command, shell=True)
    else:
        for website in websites:
            try:
                subprocess.check_output('cat /etc/hosts | grep %s' % (website), shell=True) #check if website is in hosts file
                command = 'sed -i \'\' \'s/%s %s\n//g\' /etc/hosts' % (redirect, \
                website)
                subprocess.call(command, shell=True)
            except subprocess.CalledProcessError: #if not in hosts file, add it to hosts file
                pass
    time.sleep(5)
