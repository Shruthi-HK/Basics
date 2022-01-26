# 1 to n
# n=1
# while n<=10:
#     print(n)
#     n+=1
#10 to 1
# n=10
# while n>0:
#     print(n)
#     n-=1
#-1 to -10
# n =-1
# while n>-10:
#     print(n)
# n = 1
# while n<= 50:
#     print(n)
#     n+=2
# n=1
# while n <= 50:
#     if n % 2 == 0:
#         print(n)
#     n += 1

# str = "python"
# i = 0
#
# while i < len(str):
#     print(str[i])
#     i += 1

# list_ = [1, 2, 3]
# i = 0
#
# while i < len(list_):
#     print(list_[i])
#     i += 1

# tup = (1, 2, 3, 4, 5)
# i = 0
# while i < len(tup):
#     print(tup[i])
#     i += 1

#for loop
# num = 1
# for num in range (1,11,1):
#     print(num)

# num = 10
# for num in range(10,0,-1):
#     print(num)

# num = -1
# for num in range(-1,-11,-1):
#     print(num)

#** -10 to -1
# num = -10
# for num in range (-10,0,1):
#     print(num)

#even numbers from 1 to 10
# for num in range(1, 11, 1):
#     if (num % 2 == 0):
#         print(num)

#** traversing  through string **
# string = "python"
# for item in range (len(string)):
#     print(string[item])

# for char in string:
#     print(char)

# list_ = [1, 2, 3, 4]
# for item in range (len(list_)):
#     print(list_[item], end = "\n")
#
# tup = (1, 2, 3,"hai")
# for item in range (len(tup)):
#     print(tup[item], end = " ")
# traverse through dictionary
# d = {"one":1,"two":2,"three":3}
# for key in d:
#     print(d[key],sep=" -->")

# s = "hello"
# for item in range (len(s)):
#     print(item,s[item])

# s = "hello"
# for index,item in enumerate(s):
#     print(index ,"-->"item)

#unpacking an iterable

# #write a program to traverse through a string in reverse order
# string = "hai"
# for item in range(len(string)-1,-1,-1):
#     print(string[item],end = " ")
# print()
#
# for char in string[::-1]:
#     print(char, end =" ")
#
# print()
#
# for item in reversed(string):
#     print(item, end =" ")
#
# string1 = "hello world"
# 
# count = 0
# for item in string1:
#     count += 1
# print(count)
# 
# 
# printing even index
name = "hello world"
for item in range (0,len(name),2):
    print(name[item])

for ele in name[::2]:
    print(ele)

