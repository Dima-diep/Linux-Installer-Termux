#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
from prettytable import PrettyTable

os.system("clear")
for i in range(0,45):
    print("Loading install program:")
    print("#"*i)
    time.sleep(0.1)
    os.system("clear")
time.sleep(2.5)
print("What LinuxOS do you want install in Termux?")
time.sleep(2) 
x = PrettyTable()
x.field_names = ["N", "System"]
x.add_rows(
    [
        [1, "Kali Linux"],
        [2, "Ubuntu OS"],
        [3, "Debian OS"],
        [4, "Arch Linux"],
        [5, "Manjaro"],
        [6, "Fedora OS"],
        [7, "Void Linux"],
        [8, "Alpine Linux"],
        [9, "BackBox"],
        [10, "Cent OS"],
        [11, "openSUSE Leap"],
        [12, "openSUSE Tumbleweed"],
    ]
)
print(x)
time.sleep(1)
print("Choose your Linux OS (number OS by list) : ")

a = int(input())

os.system("clear")
time.sleep(2.5)
for i in range(0,3):
    def loading() -> None:
        load = ["\\", "|", "/", "-"]
        while True:
            for p in load:
                print("Setting up apt... {p}")
                sleep(0.5)
                os.system("clear")
time.sleep(2.5)
os.system("clear")

if a == 1:
    os.system("clear")
    time.sleep(5)
    os.system("toilet -F crop -F border KALI | lolcat -S 55 -a -s 40 -i")
    os.system("cat kali.linux | lolcat -S 55 -a -s 40 -i")
    time.sleep(1.25)
    print("Installing Kali subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg update -yq && pkg install wget curl proot tar -yq && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali.sh -O kali.sh && chmod +x kali.sh && bash kali.sh")
elif a == 2:
    os.system("clear")
    time.sleep(5)
    os.system("toilet -F crop -F border ubuntu | lolcat -S 30 -a -s 40 -i")
    os.system("cat Ubuntu | lolcat -S 30 -a -s 40 -i")
    time.sleep(1.25)
    print("Installing Ubuntu 20.04 LTS subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg update -yq && pkg install wget curl proot tar -yq && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20.sh -O ubuntu20.sh && chmod +x ubuntu20.sh && bash ubuntu20.sh")
elif a == 3:
    os.system("clear")
    time.sleep(5)
    os.system("cd ~ && toilet -F crop -F border DEBIAN | lolcat -S 40 -a -s 40 -i")
    time.sleep(1.25)
    print("Installing Debian subsystem Termux...")
    os.system("cat deb.ian | lolcat -S 40 -a -s 40")
    time.sleep(1.25)
    os.system("cd ~ && pkg update -yq && pkg install wget curl proot tar -yq && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian.sh -O debian.sh && chmod +x debian.sh && bash debian.sh")
elif a == 4:
    os.system("clear")
    time.sleep(5)
    os.system("toilet -F crop -F border Arch | lolcat -S 65 -a -s 40")
    time.sleep(1.25)
    print("Installing Arch subsystem Termux...")
    os.system("cat arch.linux | lolcat -S 65 -a -s 40 -i")
    time.sleep(1.25)
    os.system("cd ~ && pkg update -yq && pkg install wget curl proot tar -yq && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch.sh -O arch.sh && chmod +x arch.sh && bash arch.sh")
elif a == 5:
    os.system("clear")
    time.sleep(5)
    os.system("toilet -F crop -F border manjaro | lolcat -S 75 -a -s 40")
    time.sleep(1.25)
    print("Installing Manjaro subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg update -yq && pkg install wget curl proot tar -yq && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro.sh -O manjaro.sh && chmod +x manjaro.sh && bash manjaro.sh")
elif a == 6:
    os.system("clear")
    time.sleep(5)
    os.system("toilet -F crop -F border Fedora 33 | lolcat -S 62 -a -s 40 -i")
    time.sleep(1.25)
    print("Installing Fedora subsystem Termux...")
    os.system("cd ~ && pkg update -yq && pkg install wget curl proot tar -yq && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora.sh -O fedora.sh && chmod +x fedora.sh && bash fedora.sh")
elif a == 7:
    os.system("clear")
    time.sleep(5)
    os.system("toilet -F crop -F border void | lolcat -S 72 -a -s 40 -i")
    time.sleep(1.25)
    print("Installing void subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg update -yq && pkg install wget curl proot tar -yq && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void.sh && chmod +x void.sh && bash void.sh")
elif a == 8:
    os.system("clear")
    time.sleep(5)
    os.system("toilet -F crop -F border Alpine | lolcat -S 55 -a -s 40 -i")
    time.sleep(1.25)
    print("Installing Alpine subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg update -yq && pkg install wget curl proot tar -yq && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpine.sh -O alpine.sh && chmod +x alpine.sh && bash alpine.sh://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpine.sh | bash")
elif a == 9:
    os.system("clear")
    time.sleep(5)
    os.system("figlet -f big BackBox")
    time.sleep(1.25)
    print("Installing BackBox subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg install wget openssl-tool proot -yq && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && chmod +x * && bash backbox.sh && chmod +x * && ./start-backbox.sh")
elif a == 10:
    os.system("clear")
    time.sleep(5)
    os.system("figlet -f big CentOS | lolcat -S 50 -a -s 40 -i")
    time.sleep(1.25)
    print("Installing CentOS subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg install wget openssl-tool proot tar -yq && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && chmod +x * && bash centos.sh && chmod +x * && ./start-centos.sh")
elif a == 11:
    os.system("clear")
    time.sleep(5)
    os.system("figlet -f big openSUSE | lolcat -S 1 -a -s 40 -i")
    time.sleep(1.25)
    print("Installing openSUSE Leap subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg install wget openssl-tool proot tar -yq && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Leap/opensuse-leap.sh && chmod +x * && bash opensuse-leap.sh && chmod +x * && ./start-leap.sh")
elif a == 12:
    os.system("clear")
    time.sleep(5)
    os.system("figlet -f big openSUSE | lolcat -S 1 -a -s 40 -i")
    time.sleep(1.25)
    print("Installing openSUSE Tumbleweed subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg install wget openssl-tool proot tar -yq && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Tumbleweed/opensuse-tumbleweed.sh && chmod +x * && bash opensuse-tumbleweed.sh && chmod +x * && ./start-tumbleweed.sh")
