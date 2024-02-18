
'''
Define a generator function that takes n as an argument
loop the values from 0 to n value
Check each value from range is divisible by both 5 and 7
Yield the value from the generator

'''

def num_generator(n):
    for i in range(n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i


