# for(i=1; i<11; i += 4){}
# initialization, final condition, increment/decrement

# i = 10
# while i >= 1:
#     print(i)
#     i -= 1



'''
1. Print multiplication of a user given number.
num = int(input('Enter a number'))

for i in range(1, 11):
    print(num, 'x', i, '=', i*num)


2. print factorial of a user given number
5! = 5*4*3*2*1 = 1*2*3*4*5 = 120

1*1 = 1
1*2 = 2    #1*2
2*3 = 6    #1*2*3
6*4 = 24   #1*2*3*4
24*5 = 120 #1*2*3*4*5


num = int(input('Enter a number'))
fact = 1
for i in range(1, num+1):
    fact = fact * i

    print(fact)


3. check if a user given number is prime or composite.
num = int(input('Enter a number'))

if(num==4):
    print('Composite')

for i in range(2, num//2):
    if num%i == 0:
        print('Composite')
        break
else:
    print('Prime')

4. print factors of a user given number.
num = 20    output: 2, 4, 5, 10

num = int(input('Enter a number'))

for i in range(2, num//2):
    if num%i == 0:
        print(i)

5. print multiples of a user given number up to user 
given boundary.
num=3 bound=20 output: 3,6,9,12,15,18

num = int(input('Enter a number')) #5
bound = int(input('Enter a boundary')) #50

for i in range(bound, bound+1, num):
    print(i)

# i = 1
# while num*i <= bound:
#     print(num*i) 

# for i in range(1, 50):
#     if num*i <= bound:
#         print(num*i)
#     else:
#         break

# for i in range(1, bound//num + 1):
#     print(num*i)

6. Print first 10 elements of Fibonacci series.
0 1 1 2 3 5 8 13 21 34 .....

bound = 100
a = 0
b = 1
print(a)
print(b)
    

# for i in range(8):
#     c = a+b
#     print(c)
#     a = b
#     b = c

while a+b <= bound:
    c = a+b
    print(c)
    a = b
    b = c

'''


#nesting
'''
1*1=1 1*2=2 1*3=3 ..........  1*9=9 1*10=10
2*1=2 2*2=4 ....................... 2*10=20
...........................................
10*1=10 10*2=20 ................... 10*10=100
'''

for i in range(1, 11):
    for j in range(1, 11):
        print(i, 'x', j, '=', i*j, end=" ")
    print()


