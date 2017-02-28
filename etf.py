import urllib2
import threading
import os
# First: brew install terminal-notifier

def checkETF():
    threading.Timer(90.0, checkETF).start()
    target_url = "https://www.sec.gov/rules/sro/batsbzx.htm"
    data = urllib2.urlopen(target_url).read(20000) #set to only check first 20000 chars
    eachWord = data.split()
 
    if "Bitcoin" in eachWord:
        print "Found"
        notify(title = 'TO THE MOON?',
            subtitle = 'GET ON IT',
            message  = 'ETF NEWS')
    else:
        print "Nothing"

def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

# Calling the function
checkETF()
