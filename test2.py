#Exercise 1
# import datetime
# name = input("Enter your name:")
# age = input("Enter your age:")
# x = 100 - int(age)
# y = 2023 + x 
# now = datetime.datetime.now()
# now.year
# print(y)


#Exercise 2
# user_num = int(input("Enter a num:"))
# if user_num % 2 == 0:
#     print("This number is Even")
# else: 
#     print("This number is Odd")
    

#Exercise 3
# a = [1,1,2,3,5,8,13,21,34,55,89]
# b = []
# for i in a:
#     if i <= 5:
#         b.append(i)
# print(b)


#Exercise 4
# user = int(input("Enter a num:"))
# l_ist = []
# for i in range(2,25):
#     if user % i == 0:
#         l_ist.append(i)
# print(l_ist)


#Exercise 5
# A = [1,2,3,5,8,13]
# B = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# C = []
# for i in A:
#      for j in B:
#          if i == j :
#               C.append(i)
# print(C)
        
 
 #Exercise 6  
# user_a = input("Enter your name please:")
# if user_a[0:len(user_a)-1] in user_a[::-1]:
#         print("The string is a palindrome")
        
# else:
#         print("Not palindrome")


#Exercise 7
# a = [1,4,9,16,25,36,49,64,81,100]
# b = []
# for i in a:
#     if i % 2 == 0:
#         b.append(i)
# print(b)


#Exercise 8



import random
num = random.randint(1,9)
guess = 0

while guess != num:
      guess = int(input("guess a num(1 , 9):")) 
      if guess <num :
         print("guess higer!")
      elif guess >num:
          print("guess lower!")
      else:
          print("you won")
      
      


    


