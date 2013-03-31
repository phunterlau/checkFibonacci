'''
speed test for two algorithms to check if a number is a fibonacci number
Quora: http://www.quora.com/Algorithms/What-is-the-most-efficient-algorithm-to-check-if-a-number-is-a-Fibonacci-Number
'''
import anders
import john
import time

f_file = open('fib_list.txt','r')
head = f_file.readline()
fib_list = [int(l.strip().split('\t')[1]) for l in f_file.readlines()]
f_file.close()

#test anders' method speed

start = time.time()

for i in range(100):
  for f in fib_list:
		x = anders.isfib(f)

print 'Anders method:',time.time()-start

#test john's method speed

start = time.time()

for i in range(100):
	for f in fib_list:
		x = john.isfib(f)

print 'John method:',time.time()-start
