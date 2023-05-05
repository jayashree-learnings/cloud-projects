a = 'int'
b = 7
c = False
d = "18.5"
print(f'the data type of a is,{type(a)}')
print(f'the data type of b is,{type(b)}')
print(f'the data type of c is,{type(c)}')
print(f'the data type of d is,{type(d)}')
# convert string 18.5 to float 18.5. When an int and float are added, it gives float as answer
x = b + float(d)
print (f'value of x is {x}')
x = b + d