# from replit import audio

# source = audio.play_file('cheer.mp3')
# source.set_loop(10)
# print(source)



import random

num = 4

chance = random.randint(1,num)
if chance == 1 or 4:
    print("it was 1")
elif chance == 2:
    print("it was 2")
elif chance == 3:
    print("3")
else:
    print('other')

from dataclasses import dataclass

@dataclass
class Number:
    one:int
    two: int
    three: int

new = Number(662,260,2811)

print(f"{new.one}-{new.two}-{new.three}")
import sys
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
    print (u"\u001b[0m")
