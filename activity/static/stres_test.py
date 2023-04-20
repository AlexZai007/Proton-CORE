import sys
import os
from termcolor import cprint





a = 0

while True:
    text_gen = "{"
    text_gen = text_gen + f' "sender": "{a}", '
    text_gen = text_gen + f' "recipient": "{a}", '
    text_gen = text_gen + f' "amount": "100" '
    text_gen = text_gen + '}'


    for i in range(len(sys.argv) - 1):
        os.system(f"""curl -X POST -H "Content-Type: application/json" -d '{text_gen}' "http://{sys.argv[i+1]}/transactions/new" | jq """)

    a = a + 1



    cprint(a, 'cyan')



