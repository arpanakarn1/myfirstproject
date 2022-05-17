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

5. print multiples of a user given number up to user 
given boundary.
num=3 bound=20 output: 3,6,9,12,15,18

6. Print first 10 elements of Fibonacci series.
0 1 1 2 3 5 8 13 21 34 .....
'''

num = int(input('Enter a number'))

for i in range(2, num//2):
    if num%i == 0:
        print(i)
