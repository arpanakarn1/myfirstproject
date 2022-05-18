#function
# def function name():
#     pass
# 1. non parameterized
# 2. parameterized

# def add_np():
#     num1 = int(input('Enter first number'))
#     num2 = int(input('Enter second number'))
#     print(num1, '+', num2, '=', num1+num2)
# add_p()
# def add(num1,num2):
#     print(num1, '+', num2, '=', num1+num2)
# add(5,3)
# add(10,15)
# add(20,200)

# a = int(input('Enter first number'))
# b = int(input('Enter second number'))
# add_p(a,b)

# def sub_p('fn'=num1, sn=num2):
#      print(num1, '+', num2, '=', num1-num2)
#     a= int(input('Enter first number'))
#     b= int(input('Enter second number'))
#     sub_p(a, b)
   


# #Positional arguments &
# #Keyword arguments
# def sub_p()


# 1. Non return type
# 2. Return type
# def add_r(num1, num2):
#     return num1+num2
# def add(num1,num2):
#     print(num1, '+', num2, '=', num1+num2)

# a =int(input('Enter first number'))
# b =intinput('Enter second number')
# if add_r(a, b)>100:
#     print('sum is greater than 100')

 users = [
      {'name':'bigyan','username':'bigyan','password':'12345','balance':125000},
      {'name':'bini','username':'bini','password':'11111','balance':75000},
      {'name':'bhoomoksha','username':'bhoomi','password':'54321','balance':10000},
      {'name':'arpana','username':'arpana','password':'22222','balance':90000},
      {'name':'deepak','username':'deepak','password':'deepak1','balance':21500},
]
# def transaction():
#     option = input('Enter w withdrawal d for deposite')
#     amount = float(input('Enter amount'))
#     if option == 'w':
#         user['balance'] = user['balance']-amount
#     elif option == 'd':
#         user['balance']=user['balance']+amount
#     else:
#         print('invalid selection')
#      print('your balance is:', user['balance'])
#      transaction()
#      un = input('Enter username')
#      pw = input('Enter password')
#      for user in users:
#          if un==user['user'] and pw==user['password']:
#              print('Welcome', user['name'])
#              print('You balance is:', user['balance'])
#              transaction()
#              break
#      else   :
#          print('wrong credentials')
         

# def transaction(balance):
#     option = input('Enter w withdrawal d for deposite')
#     amount = float(input('Enter amount'))
#     if option == 'w':
#         balance =balance-amount
#     elif option == 'd':
#         balance = balance+amount
#     return balance
#     un = input('Enter username')
#     pw = input('Enter password')
#     for user in users:
#         if un==user['user'] and pw==user['password']:
#             print('Welcome', user['name'])
#             print('You balance is:', user['balance'])
#             user['balance']=transaction(user['balance'])
#             print('you balance is:', user['balance'])
#             transaction()
#             break
#     else:
#         print('wrong credentials')


#     #def menu_option():
#         op = input('Enter t for transaction e to exit')
#         if op == 'e'
#            print('You are logged out')
#         else op == 't':
#             transaction()
             
         
# words = ['apple','orange','grapes','banana','pineapple']
# index = 0
# def show_word():
#     global index
#     word = words[index]
#     word_list = list(word)
#     random.shuffle(word_list)
#     for i in word_list:
#         print(i, end='')
#     print()
#     ans = input('Enter correct word')
#     if ans == word:
#        print('correct')
#        if index < len(words)-1:
#        index += 1
#        show_word()
#        else:
#            print('You have completed all the words')
#     else:
#         print('Incorrect')
#         show_word()
# show_word()

# questions = [
#     'what is area of Nepal?',
#     'who is the first prime minister of Nepal?',
#     'population of Nepal acc. to census 2078 is:',
#     'what is the height of Mt.Everest?',
#     'Number of providence in Nepal:'
# ]
# answers = ['147181 sq km', 'Bhimsen Thapa', '29,140,000', '8848.8 m', '7']
# options = [
#     [ '147818 sq km', '157181 sq km', '147181 sq km', '157818 sq km'],
#     ['Bhimsen Thapa', 'Bhakti Thapa', 'Kalu pande', 'Janga B Rana'],
#     ['21,940,000', '24,110,000', '21,490,000','29,140,,000'],
#     ['8884.4 m ', '8848.8','8848.4 m','8884.8 m'],
#     ['5','6','7','8']
# ]
# q_no = 0
# score = 0
# def show_qn_options():
#     print(q_no+1, '.' questions[q_no])
#     for op in options[q_no]:
#         print(op)
#     print('a)', options[q_no][0])
#     print('b)', options[q_no][1])
#     print('c)', options[q_no][2])
#     print('d)', options[q_no][3])
#     ans = input('a/b/c/d: ')
#     if ans == answers[q_no]:
# show_qn_options()


# questions = [
#     'what is area of Nepal?',
#     'who is the first prme minister of Nepal?',
#     'population of Nepal acc. to census 2078 is:',
#     'what is the height of Mt.Everest?',
#     'Number of providence in Nepal:'
# ]
# answers = ['147181 sq km', 'Bhimsen Thapa', '29,140,000', '8848.8 m', '7']
# options = [
#     [ '147818 sq km', '157181 sq km', '147181 sq km', '157818 sq km'],
#     ['Bhimsen Thapa', 'Bhakti Thapa', 'Kalu pande', 'Janga B Rana'],
#     ['21,940,000', '24,110,000', '21,490,000','29,140,,000'],
#     ['8884.4 m ', '8848.8','8848.4 m','8884.8 m'],
#     ['5','6','7','8']
# ]
# q_no = 0
# score = 0
# def show_qn_options():
#     print(q_no+1, '.' questions[q_no])
#     for op in options[q_no]:
#         print(op)
#     print('a)', options[q_no][0])
#     print('b)', options[q_no][1])
#     print('c)', options[q_no][2])
#     print('d)', options[q_no][3])
#     ans = input('a/b/c/d: ')
#     if ans == answers[q_no]:
# show_qn_options()




# questions = [
#     'what is area of Nepal?',
#     'who is the first prme minister of Nepal?',
#     'population of Nepal acc. to census 2078 is:',
#     'what is the height of Mt.Everest?',
#     'Number of providence in Nepal:'
# ]
# answers = ['147181 sq km', 'Bhimsen Thapa', '29,140,000', '8848.8 m', '7']
# options = [
#     [ '147818 sq km', '157181 sq km', '147181 sq km', '157818 sq km'],
#     ['Bhimsen Thapa', 'Bhakti Thapa', 'Kalu pande', 'Janga B Rana'],
#     ['21,940,000', '24,110,000', '21,490,000','29,140,,000'],
#     ['8884.4 m ', '8848.8','8848.4 m','8884.8 m'],
#     ['5','6','7','8']
# ]
# q_no = 0
# score = 0
# def show_qn_options():
#     print(q_no+1, '.' questions[q_no])
#     for op in options[q_no]:
#         print(op)
#     print('a)', options[q_no][0])
#     print('b)', options[q_no][1])
#     print('c)', options[q_no][2])
#     print('d)', options[q_no][3])
#     ans = input('a/b/c/d: ')
#     if ans == answers[q_no]:
# show_qn_options()

questions = [
    'what is area of Nepal?',
    'who is the first prme minister of Nepal?',
    'population of Nepal acc. to census 2078 is:',
    'what is the height of Mt.Everest?',
    'Number of providence in Nepal:'
]
answers = ['147181 sq km', 'Bhimsen Thapa', '29,140,000', '8848.8 m', '7']
options = [
    [ '147818 sq km', '157181 sq km', '147181 sq km', '157818 sq km'],
    ['Bhimsen Thapa', 'Bhakti Thapa', 'Kalu pande', 'Janga B Rana'],
    ['21,940,000', '24,110,000', '21,490,000','29,140,,000'],
    ['8884.4 m ', '8848.8','8848.4 m','8884.8 m'],
    ['5','6','7','8']
]
q_no = 0
score = 0
def show_qn_options():
    print(q_no+1, '.' questions[q_no])
    for op in options[q_no]:
        print(op)
    print('a)', options[q_no][0])
    print('b)', options[q_no][1])
    print('c)', options[q_no][2])
    print('d)', options[q_no][3])
    ans = input('a/b/c/d: ')
    if ans == answers[q_no]:
show_qn_options()




questions = [
    'what is area of Nepal?',
    'who is the first prme minister of Nepal?',
    'population of Nepal acc. to census 2078 is:',
    'what is the height of Mt.Everest?',
    'Number of providence in Nepal:'
]
answers = ['147181 sq km', 'Bhimsen Thapa', '29,140,000', '8848.8 m', '7']
options = [
    [ '147818 sq km', '157181 sq km', '147181 sq km', '157818 sq km'],
    ['Bhimsen Thapa', 'Bhakti Thapa', 'Kalu pande', 'Janga B Rana'],
    ['21,940,000', '24,110,000', '21,490,000','29,140,,000'],
    ['8884.4 m ', '8848.8','8848.4 m','8884.8 m'],
    ['5','6','7','8']
]
q_no = 0
score = 0
def show_qn_options():
    print(q_no+1, '.' questions[q_no])
    for op in options[q_no]:
        print(op)
    print('a)', options[q_no][0])
    print('b)', options[q_no][1])
    print('c)', options[q_no][2])
    print('d)', options[q_no][3])
    ans = input('a/b/c/d: ')
    if ans == answers[q_no]:
show_qn_options()
questions = [
    'what is area of Nepal?',
    'who is the first prme minister of Nepal?',
    'population of Nepal acc. to census 2078 is:',
    'what is the height of Mt.Everest?',
    'Number of providence in Nepal:'
]
answers = ['147181 sq km', 'Bhimsen Thapa', '29,140,000', '8848.8 m', '7']
options = [
    {'a':'147818 sq km', 'b':'157181 sq km', 'c':'147181 sq km', 'd':'157818 sq km},
    {'a':'Bhimsen Thapa', 'b':'Bhakti Thapa', 'c':'Kalu pande', 'd':'Janga B Rana},
    {'a':'21,940,000', 'b':'24,110,000', 'c':'21,490,000', 'd':'29,140,,000'},
    {'a':'8884.4 m ', 'b':'8848.8', 'c':'8848.4 m', 'd':'8884.8 m},
    {'a':'5','b':'6', 'c':'7', 'd':'8'},
]
q_no = 0
score = 0
def show_qn_options():
    print(q_no+1, '.' questions[q_no])
    for op in options[q_no]:
        print(op, ')',
    print('a)', options[q_no][0])
    print('b)', options[q_no][1])
    print('c)', options[q_no][2])
    print('d)', options[q_no][3])
    ans = input('a/b/c/d: ')
    if ans == answers[q_no]:
show_qn_options()













