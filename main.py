#coded by lamp in python 3
from dhooks import Webhook
import os
import time
import random
os.system("title Enter Login Code")
hook = Webhook("YOUR_WEBHOOK_LINK")
codes = random.randint(1,9999)
hook.send(f"Hello, The Login Code is {codes}")

print("Hello There! Please Enter The Login Code...")
code = int(input("Enter Code : "))
if code == codes:
    print("Valid Code!!!")
    time.sleep(5)
else :
    print("Wrong Code.")
    time.sleep(5)
    exit()
