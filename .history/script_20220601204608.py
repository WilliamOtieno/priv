import random
import subprocess

for i in range(30000):
    print(i)
    f = open('./demo.txt', 'w')
    num = random.randint(1, 9999)
    f.write(str(num))

    subprocess.run(['git' ''])
    subprocess.run([f"git commit -m {num} "])
