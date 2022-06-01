import random
import subprocess

for i in range(10):
    print(i)
    f = open('./demo.txt', 'a')
    num = random.randint(1, 9999)
    f.write(str(num))
    f.close()

    subprocess.run(['git', 'add', '.'])
    subprocess.run(["git", "commit", "-m", f"{num}"])
