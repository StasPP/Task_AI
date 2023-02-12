import eel
import os
import getStat

@eel.expose
def mainFunc(url):
    return getStat.getStat(url)

eel.init("web")
eel.start("result.html", size = (700, 700))
