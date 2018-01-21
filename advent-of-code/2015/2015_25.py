import numpy as np


#Referred to hints and solutions


def next_code(code):
    return code * 252533 % 33554393

column = 3083
row = 2978
code_at_column_start = np.sum(np.arange(2, column + 1)) + 1
code_number = code_at_column_start + np.sum(np.arange(column, column+row-1))

code = 20151125
for i in xrange(code_number - 1):
    code = next_code(code)

print code