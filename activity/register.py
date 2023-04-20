import sys
import os
import time

from termcolor import cprint
cprint(f"""
██████╗░██████╗░░█████╗░████████╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗░██║
██████╔╝██████╔╝██║░░██║░░░██║░░░██║░░██║██╔██╗██║
██╔═══╝░██╔══██╗██║░░██║░░░██║░░░██║░░██║██║╚████║
██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░╚███║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚══╝""", 'cyan')

"""
1 - node 1
2 -  node 2
"""

node1 = sys.argv[1]
node2 = sys.argv[2]


print()
cprint(f">Register mode - Double ",'green')
cprint(f">Ip of the first node - {node1} ", 'cyan')
cprint(f">Ip of the first node - {node2} ", 'cyan')

print()

gen1 = '{"nodes": ["'
gen1 = gen1 + f'http://{node1}"]'
gen1 = gen1 + '}'

gen2 = '{"nodes": ["'
gen2 = gen2 + f'http://{node2}"]'
gen2 = gen2 + '}'

node1 = sys.argv[2]
node2 = sys.argv[1]

print(gen1, node1)
print(gen2, node2)

os.system(f"""curl -X POST -H "Content-Type: application/json" -d '{gen1}' "http://{node1}/nodes/register" | jq""")
time.sleep(1)
os.system(f"""curl -X POST -H "Content-Type: application/json" -d '{gen2}' "http://{node2}/nodes/register" | jq """)
time.sleep(1)

