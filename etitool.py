import os
import time
###########
# Clear Screen
time.sleep(0.5)
os.system("clear")

# Tool Banner
time.sleep(0.5)
os.system("figlet ETI-Tool")

# Tool Code
print("")
print("----------------------------------")
print("[1] Nmap")
print("[2] Updating and Upgrading Termux")
print("[3] Sqlmap")
print("[4] Zphisher")
print("[5] Hydra")
print("[00] Exit The Programme")
print("----------------------------------")
print("")
choose = input("Select > tool_install : ")
print("")

if choose == "1":
    os.system("apt-get update && apt upgrade -y && apt-get install nmap")

elif choose == "2":
    os.system("apt-get update && apt-get upgrade -y")

elif choose == "3":
    os.system("apt-get install python -y")
    os.system("apt-get install git -y")
    os.system("git clone https://github.com/sqlmapproject/sqlmap")
    os.aystem("clear && cd sqlmap")
    os.system("python sqlmap.py")

elif choose == "4":
    os.system("apt-get install php -y")
    os.system("apt-get install php7 -y")
    os.system("git clone https://github.com/htr-tech/zphisher")
    os.system("cd zphisher")
    os.system("bash zphisher.sh")

elif choose == "5":
    os.system("git clone https://github.com/facebookresearch/hydra")

elif choose == "00":
    os.system("clear")
    quit()
elif choose == "0":
    os.system("clear")
    quit()
elif choose <= "1" or "2" or "3" or "4" or "5":
    print("Number is not found")
    time.sleep(0.5)
    quit()
