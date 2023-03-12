#age = 18
#if age <= 18 :
   # print('du bist noch joung')
#else:
    #print('ok')

benutzer = 'jihad'
if benutzer =='jihad':
    print('ok')

ziyad = 'aus remagen'
if ziyad == 'aus idleb':
    print('der ist aus syrian')

else:
     print('ok')

omer = 'gesund'
if omer == 'krank':
    print('der ist krank')
else:
     print('ja')

######### python if elif exampel
'''
x = 100
if x >  200 :
    print('x =200')
elif x == 150 :
    print('x =150')
elif X == 300 :
    print('X=300')
else:
    print('this is the defult option')
   print('rest of the code')
'''
'''
d = 150
if d >= 100 :
    print('yes')
elif d == 150 :
    print('ok')
else:
    print('yes')
    print('ok')
'''

'''
x = 5

if x > 500 :
    print('x > 500')

if x > 100 :
    print('x > 100')

if x > 700 :
    print('x > 700')

else:
    print(x)

pin_code = 1998
if pin_code == 1998:
    print('true')
    '''
#if with Boolean operators

'''
name ="jihad"
age = 31
if name == "jihad" and age == 31 :
    print("welcome jihad abdl")

if name == "jihad" or name == "ahmad" :
    print("you are not jihad")

username = "jihad"
password = 12345
if username == "jihad" and password == 12345:
    print('welcom')

username = "jihad"
password = 12345
if username == "jihad" or password == 123456:
    print('welcom')

else:
    print('login error')
'''
'''
x = 15
if x < 20 :
    print('jihAad')

#true condition  false   :ternary operater
print('welcome') if x > 10 else print('error')

age = 20
if age <= 10:
    print('das nicht genug')

if age <= 30 :
    print('das nicht genug')
else:
    print('error')
'''
# conditions best practices : exampel 1
'''
x =[1,2,3,4,5,6]
if 6 in x:
    print('JA')

x =[1,2,3,4,5,6]
if 7 not in x:
    print('yes')
'''
# conditions best practices : exampel 2
'''
x = 10
y = 7
z = 19
if x ==10 and y ==7 and z == 19:
    print('ok')

if all ([x ==10 , y ==7 , z == 19]):
    print('ok')

if x ==10 or y ==7 or z == 19:
    print('ok')

if any ([x ==10 , y ==7 , z == 19]):
    print('ok')
   '''
# conditions best practices : exampel 3
'''
a = 1
b = 2
if a == 1 and b == 2 :
    print('true')

if a == 0 or b == 2 :
    print('yes')
if not (a == 1 and b == 3):
    print('true')

if a != 0 and b != 3 :
    print('true')
'''
# conditions best practices : exampel 4
'''
x = 1
if x in (0,4,3):
    print('match')
else:
    print('not found')
''' 