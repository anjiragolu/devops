#1.Write a Python program to print the following string in a specific format
# res ="Twinkle, twinkle, little star, \n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t \tLike a diamond in the sky.\n Twinkle, twinkle, little star,\n\t How I wonder what you are"
# print(res)


#2. Write a Python program to get the Python version you are using.
# import sys
# print('current version of python :',sys.version)
#             (or)
# from platform import python_version
# print(python_version())


#3.Write a Python program to display the current date and time.
# from  datetime import datetime
# today =datetime.today()
# print(today)
#            (or)
# import datetime
# now  =datetime.datetime.now()
# print(now)


#4.Write a Python program which accepts the radius of a circle from the user and compute the area.
# from math import pi
# r =float(input('enter the value'))
# print("area of the circle :",pi*r**2)
# print("peremeter of circle :",2*pi*r)


#5. Write a Python program which accepts the user's first and last name 
#print them in reverse order with a space between them.
# first =str(input('enter first name'))
# second =str(input('enter second name'))
# print(second + first)


#6.Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and
#a tuple with those numbers.
# numbers =input('enter the numbers :')
# list1 =numbers.split(",")
# tup =tuple(list1)
# print(list1)
# print(tup)


#7.Write a Python program to accept a filename from the user and print the extension of that.
# filename =input('enter file name with extension')
# res =filename.split(".")
# print(res[-1])


#8.Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
# print('%s %s'%(color_list[0],color_list[-1]))


#9.Write a Python program to display the examination schedule
# exam_st_date = (24, 6, 2014)
# print("%i / %i / %i"%exam_st_date)


#10.Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
# n =int(input('enter the number'))
# n1 =int('%s'%n)
# n2 =int('%s%s'% (n,n))
# n3 =int('%s%s%s'%(n,n,n))
# print(n1+n2+n3)


#11.Write a Python program to print the calendar of a given month and year.
# import calendar
# y  =int(input('enter the year'))
# m =int(input('enter month'))
# print(calendar.month(y,m))


#12.Write a Python program to calculate number of days between two dates.
# from datetime import date
# date1 =date(2022,6,24)
# date2 =date(2022,7,12)
# res =date2 -date1
# print(res)


#13.Write a Python program to get the volume of a sphere with radius 6.
# from math import pi
# r =6**3
# print(4/3*pi*r)


#14.Write a Python program to get the difference between a given number and 17, 
#if the number is greater than 17 return double the absolute difference
# def difference(n):
#     if n <= 17:
#         return (17-n)
#     else:
#         return(n-17) *2
# print(difference(22))
# print(difference(9))


#15.Write a Python program to test whether a number is within 100 of 1000 or 2000






#16.Write a Python program to calculate the sum of three given numbers
#if the values are equal then return three times of their sum
# def sum_num(x,y,z):
#     sum =x + y + z
#     if x== y == z:
#        sum = sum*3
#     return sum
# print(sum_num(3,3,3))


#19. Write a Python program to get a new string from a given string where "Is" has been added to the front.
#If the given string already begins with "Is" then return the string unchanged.
#string1 ='Write a Python program to Is read a Python program to'
# def new_str(str1):
#     if str1[:2] == 'Is':
#         return str1
#     #else:
#     return 'Is'+' '+ str1
# print(new_str('arrary'))
# print(new_str('Is python'))


#20.Write a Python program to get a string which is n (non-negative integer) copies of a given string.
# def string(str,num):
#     str =str*num
#     return str
# print(string('PYTHON',3))
# print(string('.py',3))
#          (or)

# def string(str,n):
#     new =""
#     for i in range(n):
#         new = new + str
#     return new
# print(string('python',3))


#21.Write a Python program to find whether a given number (accept from the user) is even or odd.
#print out an appropriate message to the user
# number=int(input('enter your number'))
# if number % 2 == 0:
#     print('this number is even')
# else:
#     print('this number is odd')


#22. Write a Python program to count the number 4 in a given list.
#list1 =[1,2,4,5,6,4,6,8,4,8,4,6,4]
# list2 =dict()
# for i in list1:
#     list2[i]=list1.count(i)
# print(list2)
#          (or)
# count = 0
# for i in list1:
#     if i == 4:
#         count =count + 1
# print(count)


#23.Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. 
#Return the n copies of the whole string if the length is less than 2
# def copy(str,n):
#     if len(str) > 2 :
#         return str[:2] *n
#     else:
#         return str*n
# print(copy('python',3))
# print(copy('ab',6))


#24.Write a Python program to test whether a passed letter is a vowel or not.
# def check(vowels,letter):
#     if letter in vowels:
#         return 'yes'
#     else:
#         return 'no'
# print(check('a,e,i,o,u','u'))
# print(check('a,e,i,o,u','t'))
#          (or)
# def is_vowel(char):
#     vowel ='a','e','i','o','u'
#     return  char in vowel
# print(is_vowel('a'))


#25.Write a Python program to check whether a specified value is contained in a group of values.
# def group(list,num):
#     return num in list
# print(group([1,2,3,6,5],9))
#         (or)
# def new_group(list,num):
#     for i in list:
#         if i == num:
#             return True
#     else:
#         return False
# print(new_group([1,5,6,8,9,7],1))


#26.Write a Python program to create a histogram from a given list of integers
# def histogram(num):
#     for i in num:
#         new =' '
#         times = i
#         while(times > 0):
#             new =new +"*"
#             times =times - 1
#         print(new)
# histogram([2,3,4,5,6])

#27.Write a Python program to concatenate all elements in a list into a string and return it.
# def conc(list):
#     new =''
#     for i in list:
#         new =new +str(i)
#     return new
# print(conc([4,6,8,10]))


#28.Write a Python program to print out all even numbers from a given numbers list in the same order and
#stop the printing if any numbers that come after 237 in the sequence.
# list =[386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527]
# for i in list:
#     if i ==237:
#         print(i)
#         break
#     elif i % 2 ==0:
#         print(i)


#29.Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])        
# print(color_list_1.difference(color_list_2))   
#print(color_list_2.difference(color_list_1))  


#30.Write a Python program that will accept the base and height of a triangle and compute the area
# hight =int(input('enter hight :'))
# length =int(input('enter length :'))
# res =hight*length/2
# print(res)


#31.Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.Write a Python program to sum of three given integers. 
#However, if two values are equal sum will be zero.
# def sum_of_num(x,y,z):
#     if x == y or y==z or z==x:
#         sum =0
#     else:
#         sum =x+y+z
#     return sum
# print(sum_of_num(1,2,1))


#32.Write a Python program to sum of two given integers. 
# However, if the sum is between 15 to 20 it will return 20
# def sum_two(x,y):
#     sum = x+y
#     if sum in range(15,20) :
#         return 20 
#     else:
#          return sum
    
# print(sum_two(10,6))


#33.
 
    
