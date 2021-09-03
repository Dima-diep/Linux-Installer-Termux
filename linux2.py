#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
from prettytable import PrettyTable

os.system("cd ~/ && clear")
print("What Linux do you want install?") 
x = PrettyTable()
x.field_names = ["N", "System"]
x.add_rows(
    [
        [1, "Arch Linux"],
        [2, "Alpine Linux"],
        [3, "Fedora"],
        [4, "Kali Linux"],
        [5, "Ubuntu 20.04"],
        [6, "Parrot OS"],
        [7, "Void Linux"],
        [8, "Debian"],
        [9, "Manjaro"],
    ]
)
print(x)
print("Install OS:")
a = int(input())

if a == 1:
    os.system("clear")
    x = PrettyTable()
    x.field_names = ["N", "Desktop"]
    x.add_rows(
        [
            [1, "Awesome"],
            [2, "i3/i3wm"],
            [3, "LXDE"],
            [4, "XFCE"],
            [5, "openbox"],
            [6, "Install without desktop"],
        ]
    )
    print(x)
    print("Your desktop:")
    d = int(input())

    if d == 1:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-awesome.sh | bash")
    elif d == 2:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-i3.sh | bash")
    elif d == 3:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-lxde.sh | bash")
    elif d == 4:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-xfce.sh | bash")
    elif d == 5:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch-openbox.sh | bash")
    elif d == 6:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch.sh | bash")
elif a == 2:
    os.system("clear")
    x = PrettyTable()
    x.field_names = ["N", "Desktop"]
    x.add_rows(
        [
            [1, "MATE"],
            [2, "XFCE"],
            [3, "Install without desktop"],
        ]
    )
    print("Your desktop:")
    g = int(input())

    if g == 1:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpine-mate.sh && bash alpine-mate.sh")
    elif g == 2:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpine-xfce.sh && bash alpine-xfce.sh")
    elif g == 3:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpine.sh | bash")
elif a == 3:
    os.system("clear")
    x = PrettyTable()
    x.field_names = ["N", "Desktop"]
    x.add_rows(
        [
            [1, "Awesome"],
            [2, "i3/i3wm"],
            [3, "openbox"],
            [4, "LXDE"],
            [5, "LXQT"],
            [6, "XFCE"],
            [7, "Install without desktop"],
        ]
    )
    print(x)
    print("Your desktop:")
    h = int(input())

    if h == 1:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-awesome.sh | bash")
    elif h == 2:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-i3.sh | bash")
    elif h == 3:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-openbox.sh | bash")
    elif h == 4:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-lxde.sh | bash")
    elif h == 5:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-lxqt.sh | bash")
    elif h == 6:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora-xfce.sh | bash")
    elif h == 7:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora.sh | bash")
elif a == 4:
    os.system("clear && cat kali.linux | lolcat -S 55 -a -s 40 -i")
    os.system("toilet KALI -F crop -F border | lolcat -S 55 -a -s 40 -i")
    x = PrettyTable()
    x.field_names = ["N", "Desktop"]
    x.add_rows(
        [
            [1, "Awesome"],
            [2, "i3/i3wm"],
            [3, "openbox"],
            [4, "LXDE"],
            [5, "LXQT"],
            [6, "XFCE"],
            [7, "Install without desktop"],
        ]
    )
    print(x)
    print("Your desktop:")
    i = int(input())

    if i == 1:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-awesome.sh | bash")
    elif i == 2:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-i3.sh | bash")
    elif i == 3:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-openbox.sh | bash")
    elif i == 4:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-lxde.sh | bash")
    elif i == 5:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-lxqt.sh | bash")
    elif i == 6:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-xfce.sh | bash")
    elif i == 7:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali.sh | bash")
elif a == 5:
    os.system("clear && cat Ubuntu | lolcat -S 30 -a -s 40 -i")
    x = PrettyTable()
    x.field_names = ["N", "Desktop"]
    x.add_rows(
        [
            [1, "Awesome"],
            [2, "i3/i3wm"],
            [3, "openbox"],
            [4, "LXDE"],
            [5, "LXQT"],
            [6, "XFCE"],
            [7, "el"],
            [8, "Install without desktop"],
        ]
    )
    print(x)
    print("Your desktop:")
    j = int(input())

    if j == 1:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-awesome.sh | bash")
    elif j == 2:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-i3.sh | bash")
    elif j == 3:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-openbox.sh | bash")
    elif j == 4:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-lxde.sh | bash")
    elif j == 5:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-lxqt.sh | bash")
    elif j == 6:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-xfce.sh | bash")
    elif j == 7:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20-el.sh | bash")
    elif j == 8:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20.sh | bash")
elif a == 6:
    os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Parrot/parrot.sh | bash")
elif a == 7:
    os.system("clear")
    x = PrettyTable()
    x.field_names = ["N", "Desktop"]
    x.add_rows(
        [
            [1, "Awesome"],
            [2, "i3/i3wm"],
            [3, "openbox"],
            [4, "LXDE"],
            [5, "LXQT"],
            [6, "XFCE"],
            [7, "Install without desktop"],
        ]
    )
    print(x)
    print("Your desktop:")
    l = int(input())

    if l == 1:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void-awesome.sh | bash")
    elif l == 2:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void-i3.sh | bash")
    elif l == 3:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void-openbox.sh | bash")
    elif l == 4:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void-lxde.sh | bash")
    elif l == 5:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void-lxqt.sh | bash")
    elif l == 6:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void-xfce.sh | bash")
    elif l == 7:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void.sh | bash")
elif a == 8:
    os.system("clear && cat deb.ian | lolcat -S 40 -a -s 40")
    x = PrettyTable()
    x.field_names(
        [
            [1, "Awesome"],
            [2, "i3/i3wm"],
            [3, "el"],
            [4, "openbox"],
            [5, "LXDE"],
            [6, "LXQT"],
            [7, "XFCE"],
            [8, "Install without desktop"],
        ]
    )
    print(x)
    print("Your desktop:")
    k = int(input())

    if k == 1:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-awesome.sh | bash")
    elif k == 2:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-i3.sh | bash")
    elif k == 3:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-el.sh | bash")
    elif k == 4:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-openbox.sh | bash")
    elif k == 5:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-lxde.sh | bash")
    elif k == 6:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-lxqt.sh | bash")
    elif k == 7:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian-xfce.sh | bash")
    elif k == 8:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian.sh | bash")
elif a == 9:
    os.system("clear")
    x = PrettyTable()
    x.field_names = ["N", "Desktop"]
    x.add_rows(
        [
            [1, "Awesome"],
            [2, "i3/i3wm"],
            [3, "openbox"],
            [4, "LXDE"],
            [5, "LXQT"],
            [6, "XFCE"],
            [7, "Install without desktop"],
        ]
    )
    print(x)
    print("Your desktop:")
    m = int(input())

    if m == 1:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro-awesome.sh | bash")
    elif m == 2:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro-i3.sh | bash")
    elif m == 3:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro-openbox.sh | bash")
    elif m == 4:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro-lxde.sh | bash")
    elif m == 5:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro-lxqt.sh | bash")
    elif m == 6:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro-xfce.sh | bash")
    elif m == 7:
        os.system("clear && curl -LO https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro.sh | bash")
