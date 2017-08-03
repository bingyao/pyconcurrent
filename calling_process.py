import os
import sys

program = 'python'
arguments = ['called_process.py']

print('Calling process...')

arguments.insert(0, program)
print(arguments)


os.execvp(program, arguments)

print('Goode Bye!!')
