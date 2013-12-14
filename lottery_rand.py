from random import *
import os
import time
#Below is an empty list called numbers
numbers = []
#We now use a for loop to create the numbers 1 to 49 in our list
for i in range(1,50):
    numbers.append(int(i))

#os.system('mpg123 lottery.mp3 &')
#time.sleep(5)
print "What I believe are the winning lottery numbers for tonight are..."
time.sleep(3)
#Now we shuffle the numbers stored in the list called "numbers"
shuffle(numbers)
#We slice out the first 7 numbers from the list
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
