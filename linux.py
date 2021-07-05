#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
from colorama import init
from termcolor import colored

init()
print("Install requirements... ")
os.system("apt install figlet toilet ruby2")
os.system("gem install lolcat")
os.system("clear")
for i in range(0,45):
    print("Loading install program:")
    print("#"*i)
    time.sleep(0.1)
    os.system("clear")
time.sleep(2.5)
print("<What LinuxOS do you want install in Termux>")
print("<==========================================>")
time.sleep(2)
print("<-----------------KaliLinux---------------->")
print("<-----------------Ubuntu OS---------------->")
print("<-----------------Debian OS---------------->")
print("<-----------------ArchLinux---------------->")
print("<------------------Manjaro----------------->")
print("<-----------------Fedora OS---------------->")
print("<------------------Void OS----------------->")
print("<-----------------Alpine OS---------------->")
print("<------------------BackBox----------------->")
print("<------------------Cent OS----------------->")
print("<---------------openSUSELeap--------------->")
print("<------------openSUSETumbleweed------------>")
print("<----------------Black Arch---------------->")
print("<-----------------ParrotOS----------------->")
time.sleep(2)
print("<==========================================>")
time.sleep(1)
print("Choose your Linux OS (number OS by list) : ")

a = int(input())

os.system("clear")
time.sleep(2.5)
def loading() -> None:
    load = ["\", "|", "/", "-"]
    while True:
        for p in load:
            print("Setting up apt... {p}")
            sleep(0.5)
            os.system("clear")
def loading() -> None:
    load = ["\", "|", "/", "-"]
    while True:
        for p in load:
            print("Setting up apt... {p}")
            sleep(0.5)
            os.system("clear")
def loading() -> None:
    load = ["\", "|", "/", "-"]
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
    os.system("toilet -F crop -F border KALI | lolcat -S 55 -a -s 40")
    time.sleep(1.25)
    print("Installing Kali subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali.sh | bash && chmod +x * && ./start-kali.sh")
elif a == 2:
    os.system("clear")
    time.sleep(5)
    os.system("toilet -F crop -F border ubuntu | lolcat -S 30 -a -s 40")
    time.sleep(1.25)
    print("Installing Ubuntu 20.04 LTS subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && proot-distro install ubuntu-20.04")
elif a == 3:
    os.system("clear")
    time.sleep(5)
    os.system("cd ~ && toilet -F crop -F border DEBIAN | lolcat -S 40 -a -s 40")
    time.sleep(1.25)
    print("Installing Debian subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian.sh | bash && cgmod +x * && ./start-debian.sh")
elif a == 4:
    os.system("clear")
    time.sleep(5)
    os.system("toilet -F crop -F border Arch | lolcat -S 65 -a -s 40")
    time.sleep(1.25)
    print("Installing Arch subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch.sh | bash && chmod + x * && ./start-arch.sh")
elif a == 5:
    os.system("clear")
    time.sleep(5)
    os.system("toilet -F crop -F border manjaro | lolcat -S 75 -a -s 40")
    time.sleep(1.25)
    print("Installing Manjaro subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch.sh | bash && chmod +x * && ./start-arch.sh")
elif a == 6:
    os.system("clear")
    time.sleep(5)
    os.system("toilet -F crop -F border Fedora 33 | lolcat -S 62 -a -s 40")
    time.sleep(1.25)
    print("Installing Fedora subsystem Termux...")
    os.system("cd ~ && pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora.sh | bash && chmod +x * && ./start-fedora.sh")
elif a == 7:
    os.system("clear")
    time.sleep(5)
    os.system("toilet -F crop -F border void | lolcat -S 72 -a -s 40")
    time.sleep(1.25)
    print("Installing void subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void.sh | bash && chmod + * && ./start-void.sh")
elif a == 8:
    os.system("clear")
    time.sleep(5)
    os.system("toilet -F crop -F border Alpine | lolcat -S 55 -a -s 40")
    time.sleep(1.25)
    print("Installing Alpine subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpine.sh | bash && chmod + x * && ./start-alpine.sh")
elif a == 9:
    os.system("clear")
    time.sleep(5)
    os.system("figlet -f big BackBox")
    time.sleep(1.25)
    print("Installing BackBox subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && chmod +x * && bash backbox.sh && chmod +x * && ./start-backbox.sh")
elif a == 10:
    os.system("clear")
    time.sleep(5)
    os.system("figlet -f big CentOS | lolcat -S 50 -a -s 40")
    time.sleep(1.25)
    print("Installing CentOS subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && chmod +x * && bash centos.sh && chmod +x * && ./start-centos.sh")
elif a == 11:
    os.system("clear")
    time.sleep(5)
    os.system("figlet -f big openSUSE | lolcat -S 1 -a -s 40")
    time.sleep(1.25)
    print("Installing openSUSE Leap subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Leap/opensuse-leap.sh && chmod +x * && bash opensuse-leap.sh && chmod +x * && ./start-leap.sh")
elif a == 12:
    os.system("clear")
    time.sleep(5)
    os.system("figlet -f big openSUSE | lolcat -S 1 -a -s 40")
    time.sleep(1.25)
    print("Installing openSUSE Tumbleweed subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Tumbleweed/opensuse-tumbleweed.sh && chmod +x * && bash opensuse-tumbleweed.sh && chmod +x * && ./start-tumbleweed.sh")
elif a == 13:
    os.system("clear")
    time.sleep(5)
    os.system("figlet -f big BlackArch")
    time.sleep(1.25)
    print("Installing BlackArch subsystem Termux...")
    time.sleep(1.25)
    os.system("cd ~ && pacman-key --init && pacman-key --populate archlinuxarm && pacman -Sy --noconfirm curl && curl -O https://blackarch.org/strap.sh && chmod +x strap.sh && ./strap.sh && chmod +x * && ./start-arch.sh")
