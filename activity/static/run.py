import os
from termcolor import cprint

os.system("python3 1.py")
os.system("python3 2.py")

cprint(f"""
██████╗░██████╗░░█████╗░████████╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗░██║
██████╔╝██████╔╝██║░░██║░░░██║░░░██║░░██║██╔██╗██║
██╔═══╝░██╔══██╗██║░░██║░░░██║░░░██║░░██║██║╚████║
██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░╚███║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚══╝""", 'cyan')

print()
cprint(f">Statistic Monitor - Activate ",'green')
cprint(f">Statistic Monitor 1 - True ", 'cyan')
cprint(f">Statistic Monitor 2 - True ", 'cyan')
cprint(f">Statistic Monitor 3 - False ", 'cyan')
print()