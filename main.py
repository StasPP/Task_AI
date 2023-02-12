import eel
import os
import getStat

@eel.expose
def mainFunc(url):
    return getStat.getStat(url)

eel.init("web")
eel.start("result.html", size = (700, 700))

# print(getStat.getStat('https://stackoverflow.com/questions/4800419/finding-max-value-in-the-second-column-of-a-nested-list'))

# Get the list of all files and directories
# path =  os.getcwd()+'\\web'
# dir_list = os.listdir(path)
# print("Files and directories in '", path, "' :")
# print(dir_list)