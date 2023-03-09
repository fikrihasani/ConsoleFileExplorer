import subprocess, os, platform

if platform.system() == 'Darwin':       # macOS
    subprocess.call(('open', "main.py"))
elif platform.system() == 'Windows':    # Windows
    os.startfile("main.py")
else:                                   # linux variants
    os.open("main.py",os.O_CREAT|os.O_RDWR)