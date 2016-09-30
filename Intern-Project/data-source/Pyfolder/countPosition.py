# -*- coding: utf-8 -*-
import sys
from unidecode import unidecode

def remove_non_ascii(text):
    return unidecode(unicode(text, encoding = "utf-8"))

s = """SL5637144590;CO16000015TD;01.01.2016;01.01.2016;28.01.2016;Sales Order;
Invoiced;141916D;;Ruprecht-Karls-Universit?t Heidelberg IWR - Interdisziplin?r;
Sach Felix 000059;5637144634;td;TD;HPC;NULL;NULL;1.3.1 Dual CPU;Target A;10;62000;
customer;2015-03-01 00:00:00.000;WS-2800T-A;1;5.032.660.000;0.000000;5.032.660.000;
4.783.353.710;249.306.290;0.0000000000000000;0.0000000000000000;oschmidt;LYX;;
"1 x Nanoxia Deep Silence 5 Workstation chassis:,- Form factor: Mini-ITX, Micro - ITX, 
ATX, XL-ATX, E-AT,x- FANs:,2x 140 mm (Front) - 2x installed,1x 140 mm (Back) -
1x installed,2x 120/140 mm (Top),1x 120/140 mm (Bottom),- Slots:,4x 5.25 inch
(external), 1x 3.5 inch (external, in 5.25 slot),5x 3.5 inch (internal),6x 2.5
inch (internal),- Expansion slots: 10,- I/O panel:,2x USB 3.0,2x USB 2.0,1x
audio,1x mic,- Measurements: 232 x 550 x 550 mm (WxHxD),- Material: Aluminium,-
Weight: approx. 16.5 kg,- Colour: black, - without PSU,1 x 850 Watt PSU, Enermax
Revolution87+, 100-240 V, 80 PLUS� Gold,1 x 1 x X10DAI mainboard,Intel� C612
chipset,2x R3 processor sockets,Max. 1024 GB memory, 16x DDR4 DIMM slots,Intel�
PCH C612 SATA Controller onboard,Dual Gigabit Ethernet LAN onboard (Intel� I210)
,Fast Ethernet LAN onboard (Nuvoton WP450R dedicated for IPMI),Winbond� WPCM450R
BMC IPMI 2.0 server management with virtual media over LAN and KVM-over-LAN
onboard support,-,Extension slots CPU1: 2x PCI Express 3.0 x16,, 1x PCI Express
3.0 x4(in x8) ,Extension slots CPU2:, 1x PCI Express 3.0 x16x, 2x PCI Express
3.0 x8,Rear ports: 1x VGA, 4x USB 2.0, 1x serial, 3x RJ45,Internal ports: 7x USB
2.0, 1x serial,2 x Intel� Xeon� processor E5-2698v3,(16 cores, 40 MB L3 cache,
2.3 GHz, 9.6 GT/s, DDR4-1600/1866/2133 MHz, Hyper-Threading, Turbo Boost 2.0,
vPro, VT-x, VT-d, 135W),8 x 8 GB DDR4 DIMM, 2133 MHz, registered, ECC,1 x 1 x
Samsung� Solid-State Drive 850 EVO Series,500 GB, 6Gb/s SATA III,2.5"",3D
VNAND,2 x 1 x Constellation ES.3, 4 TB, SATA/600, 128 MB, 7200 rpm, 3.5"",1 x 1
x DVD burner, SATA, black,1 x NVIDIA Quadro� K620 graphics card,2 GB DDR3
dedicated memory,active cooling (single slot),Ports: 1x display port, 1x DVI-I
(incl. 2 adapter: DP->DVI-D, DVI->VGA),1 x Realtek� ALC889 High Definition Audio
onboard,,1 x Cherry eVolution STREAM XT G85-23100 keyboard, black,1 x Logitech
USB Optical Wheel Mouse, 3 keys, black,,1 x 1 x transtec360 - 3-year 10x5
BUSINESS on-site service (NBD),Th";;;;;;;;;;;;;;;;;"""

print len(s)
print s[2390:2400]
print s[-10:-1]
#===============================================================================
# for i in range(len(s)):
#     if s[i] not in "^[ \t\v]*#.*?coding[:=][ \t]*([-_.a-zA-Z0-9]+)":
#         print s[i]
#===============================================================================
