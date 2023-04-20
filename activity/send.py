import sys
import os

from termcolor import cprint
cprint(f"""
██████╗░██████╗░░█████╗░████████╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗░██║
██████╔╝██████╔╝██║░░██║░░░██║░░░██║░░██║██╔██╗██║
██╔═══╝░██╔══██╗██║░░██║░░░██║░░░██║░░██║██║╚████║
██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░╚███║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚══╝""", 'cyan')




"""
1 - node
2 - sender
3 - recipient
4 - amount
"""

node = sys.argv[1]
sender = sys.argv[2]
recipient = sys.argv[3]
amount = sys.argv[4]

print()
cprint(f">Send mode - Activate ",'green')
cprint(f">The node that will receive the request - {node} ", 'cyan')
cprint(f">Transaction sender - {sender} ", 'cyan')
cprint(f">Transaction recipient - {recipient} ", 'cyan')
cprint(f">Amount of main coin - {amount} ", 'cyan')
print()


text_gen = "{"
text_gen = text_gen + f' "sender": "{sender}", '
text_gen = text_gen + f' "recipient": "{recipient}", '
text_gen = text_gen + f' "amount": "{amount}" '
text_gen = text_gen + '}'


os.system(f"""curl -X POST -H "Content-Type: application/json" -d '{text_gen}' "http://{node}/transactions/new" | jq """)