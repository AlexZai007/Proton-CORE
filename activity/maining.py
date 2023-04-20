import os
import time as t
from termcolor import cprint
import sys

"""
1 - time
2 - node
3 - max_mine
"""


time = int(sys.argv[1])
node = sys.argv[2]


max_mine = int(sys.argv[3])

cprint(f"""
██████╗░██████╗░░█████╗░████████╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗░██║
██████╔╝██████╔╝██║░░██║░░░██║░░░██║░░██║██╔██╗██║
██╔═══╝░██╔══██╗██║░░██║░░░██║░░░██║░░██║██║╚████║
██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░╚███║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚══╝""", 'cyan')

print()
cprint(f">Mining mode - Activate ",'green')
cprint(f">Waiting between different blocks - {time} ", 'cyan')
cprint(f">Node ID - {node} ", 'cyan')
cprint(f">Max Mining - {max_mine} ", 'cyan')
print()

i = 0
while i != max_mine:
    os.system(f"curl -X GET http://{node}/mine | jq")
    t.sleep(time)
    i = i + 1


cprint(f">Mining mode - Disactivate ",'red')
