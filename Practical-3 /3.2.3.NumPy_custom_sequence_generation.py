#Write a Python program that takes the following inputs from the user:

Start value: The starting point of the sequence.
Stop value: The sequence should end before this value.
Step value: The increment between each number in the sequence.
The program should then generate a sequence using numpy based on these inputs and print the generated sequence.

  # code :

  import numpy as np

# Take user input for the start, stop, and step of the sequence
start = int(input())
stop = int(input())
step = int(input())

Seq = np.arange(start,stop,step)

print(Seq)
