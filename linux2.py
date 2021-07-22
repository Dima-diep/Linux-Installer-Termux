#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os

os.system("cd ~/")
print("What Linux do you want install:")
print("1.Arch Linux")
print("2.Alpine Linux")
print("3.Fedora")
print("4.Kali Linux")
print("5.Ubuntu 20.04")
print("6.Parrot OS")
print("7.Void Linux")
print("8.Debian")
print("9.Manjaro")
print("Install OS:")
a = int(input())

if a == 1:
    print("Your system architecture?")
    print("1.amd64")
    print("2.armhf")
    print("If you are at arm64, please use armhf installer...")
    print("arm64 is the same as aarch64")
    # I'm using armhf Arch Linux system at my phone - arm64. I haven't got any problems...
    print("Architecture:")
    b = int(input())

    if b == 1:
        os.system("cat arch.linux | lolcat -S 65 -a -s 40 -i")
        print("Your desktop:")
        print("1.LXDE")
        print("2.XFCE")
        print("3.Install without desktop")
        print("Your desktop:")
        c = int(input())

        if c == 1:
            os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/amd64/arch-lxde.sh | bash")
        elif c == 2:
            os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/amd64/arch-xfce.sh | bash")
        elif c == 3:
            os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/amd64/arch.sh | bash")
    elif b = 2:
        print("Your desktop:")
        print("1.Awesome")
        print("2.i3/i3wm")
        print("3.LXDE")
        print("4.XFCE")
        print("5.openbox")
        print("6.Install without desktop")
        print("Your desktop:")
        d = int(input())

        if d == 1:
            os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-awesome.sh | bash")
        elif d == 2:
            os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-i3.sh | bash")
        elif d == 3:
            os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-lxde.sh | bash")
        elif d == 4:
            os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-xfce.sh | bash")
        elif d == 5:
            os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-openbox.sh | bash")
        elif d == 6:
            os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch.sh | bash")
elif a == 2:
    print("Your phone:")
    print("1.Android")
    print("2.iPhone/iPad")
    print("Your phone:")
    e = int(input())

    if e == 1:
        print("Your desktop:")
        print("1.XFCE")
        print("2.Install without desktop")
        print("Your desktop:")
        f = int(input())

        if f == 1:
            os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpinexfce.sh | bash")
        elif f == 2:
            os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpine.sh | bash")
    elif e == 2:
        print("Your desktop:")
        print("1.MATE")
        print("2.XFCE")
        g = int(input())

        if g == 1:
            os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpine-mate.sh && sh alpine-mate.sh")
        elif g == 2:
            os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpine-xfce.sh && sh alpine-xfce.sh")
elif a == 3:
    print("Your desktop:")
    print("1.Awesome")
    print("2.i3/i3-wm")
    print("3.openbox")
    print("4.LXDE")
    print("5.LXQT")
    print("6.XFCE")
    print("7.Install without desktop")
    h = int(input())

    if h == 1:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-awesome.sh | bash")
    elif h == 2:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-i3.sh | bash")
    elif h == 3:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-openbox.sh | bash")
    elif h == 4:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-lxde.sh | bash")
    elif h == 5:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-lxqt.sh | bash")
    elif h == 6:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-xfce.sh | bash")
    elif h == 7:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora.sh | bash")
elif a == 4:
    os.system("cat kali.linux | lolcat -S 55 -a -s 40 -i")
    os.system("toilet KALI -F crop -F border | lolcat -S 55 -a -s 40 -i") 
    print("Your desktop:")
    print("1.Awesome")
    print("2.i3/i3wm")
    print("3.openbox")
    print("4.LXDE")
    print("5.LXQT")
    print("6.XFCE")
    print("7.Install without desktop")
    i = int(input())

    if i == 1:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-awesome.sh | bash")
    elif i == 2:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-i3.sh | bash")
    elif i == 3:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-openbox.sh | bash")
    elif i == 4:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-lxde.sh | bash")
    elif i == 5:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-lxqt.sh | bash")
    elif i == 6:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-xfce.sh | bash")
    elif i == 7:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali.sh | bash")
elif a == 5:
    os.system("cat Ubuntu | lolcat -S 30 -a -s 40 -i")
    print("Your desktop:")
    print("1.Awesome")
    print("2.i3/i3wm")
    print("3.openbox")
    print("4.LXDE")
    print("5.LXQT")
    print("6.XFCE")
    print("7.el")
    print("8.Install without desktop")
    j = int(input())

    if j == 1:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-awesome.sh | bash")
    elif j == 2:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-i3.sh | bash")
    elif j == 3:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-openbox.sh | bash")
    elif j == 4:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-lxde.sh | bash")
    elif j == 5:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-lxqt.sh | bash")
    elif j == 6:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-xfce.sh | bash")
    elif j == 7:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-el.sh | bash")
    elif j == 8:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20.sh | bash")
elif a == 6:
    os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Parrot/parrot.sh | bash")
elif a == 7:
    print("Your desktop:")
    print("1.Awesome")
    print("2.i3/i3wm")
    print("3.openbox")
    print("4.LXDE")
    print("5.LXQT")
    print("6.XFCE")
    print("7.Install without desktop")
    l = int(input())

    if l == 1:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void-awesome.sh | bash")
    elif l == 2:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void-i3.sh | bash")
    elif l == 3:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void-openbox.sh | bash")
    elif l == 4:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void-lxde.sh | bash")
    elif l == 5:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void-lxqt.sh | bash")
    elif l == 6:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void-xfce.sh | bash")
    elif l == 7:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void.sh | bash")
elif a == 8:
    os.system("cat deb.ian | lolcat -S 40 -a -s 40")
    print("Your desktop:")
    print("1.Awesome")
    print("2.i3/i3wm")
    print("3.el")
    print("4.openbox")
    print("5.LXDE")
    print("6.LXQT")
    print("7.XFCE")
    print("8.Install without desktop")
    k = int(input())

    if k == 1:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-awesome.sh | bash")
    elif k == 2:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-i3.sh | bash")
    elif k == 3:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-el.sh | bash")
    elif k == 4:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-openbox.sh | bash")
    elif k == 5:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-lxde.sh | bash")
    elif k == 6:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-lxqt.sh | bash")
    elif k == 7:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-xfce.sh | bash")
    elif k == 8:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian.sh | bash")
elif a == 9:
    print("Your desktop:")
    print("1.Awesome")
    print("2.i3/i3wm")
    print("3.openbox")
    print("4.LXDE")
    print("5.LXQT")
    print("6.XFCE")
    print("7.Install without desktop")
    m = int(input())

    if m == 1:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro-awesome.sh | bash")
    elif m == 2:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro-i3.sh | bash")
    elif m == 3:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro-openbox.sh | bash")
    elif m == 4:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro-lxde.sh | bash")
    elif m == 5:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro-lxqt.sh | bash")
    elif m == 6:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro-xfce.sh | bash")
    elif m == 7:
        os.system("curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro.sh | bash")
