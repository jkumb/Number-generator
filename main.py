'''
read the value from the subfolder file.
Create a list to store the values from the generator
Iterate over the generator object and append the values to the list
Print the values in comma separated form
'''

import os
from generator import num_generator
cwd = os.getcwd()
file_path=os.path.join(cwd,'input','input.txt')
f=open(file_path,'r')
n = int(f.read())

values = []
generator = num_generator(n)

for i in generator:
    values.append(i)

print(*values,sep=',')
