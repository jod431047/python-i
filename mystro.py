'''
def func_name(x,y):  
    body
    return result
'''
'''
def mysum(x,y):
    total = x + y
    return total

print(mysum(5.5,10))


print(mysum(15,100))

'''
'''
#def mysum(x=0,y=0):
#    total = x + y
#  return total

#print(mysum(5,10))
'''
'''
mysum = lambda x,y  : x+y

print(mysum(10,20))
'''
'''
x = (lambda x,y : x+y)(4,5)
'''
'''
f = 0
print(f)

def do():
    f = 5
    print(f)

do()
print(f)
'''
'''
f = 0
print(f)

def do():
    global f
    f = 5
    print(f)

do()
print(f)
'''
'''
int
float
bool

str
list
tuple
dict
'''
'''
name = 'jihad'
print('my name is name')
print(f'my name is {name}')
'''
'''
c = 'jihad'
f = 'ziyad'

print(c*3)
print( c + f)
print(c+' '+f)
print(f"{c} {f}")
'''
'''
d = {'ahmad': 50, 'ali': 60, 'jiahd': 100}
for v in d:
    print(v)

d = {'ahmad': 50, 'ali': 60, 'jiahd': 100}
for v in d.values():
    print(v)
    '''
'''
d = {'ahmad': 50, 'ali': 60, 'jiahd': 100}
for v in d:
    print(v)

d = {'ahmad': 50, 'ali': 60, 'jiahd': 100}
for k,v in d.items():
    print(f"{k}      :      {v}")
'''