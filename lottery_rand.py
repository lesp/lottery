from random import *
import os
import time
numbers = []
for i in range(1,50):
    numbers.append(int(i))

#os.system('mpg123 lottery.mp3 &')
#Removed this due to copyright issues, but you can get the audio from the net, just google it :)
time.sleep(5)
print "What I believe are the winning lottery numbers for tonight are..."
time.sleep(3)
shuffle(numbers)
a = numbers[0]
b = numbers[1]
c = numbers[2]
d = numbers[3]
e = numbers[4]
f = numbers[5]
g = numbers[6]

print (a)
time.sleep(1)
print (b)
time.sleep(1)
print (c)
time.sleep(1)
print (d)
time.sleep(1)
print (e)
time.sleep(1)
print (f)

print "And the bonus ball is..."
time.sleep(3)
print g
