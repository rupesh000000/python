# write a progarm to print Hello,world!
# a="Hello,world!"
# print(a)

# write a program to add two numbers
# a=30
# b=20
# print(a+b)

# calculate the area of circle
# pie=3.14
# r=9
# print(int((pie*r**2)))

# swap the  two variables without using third variable
# a=10
# b=20
# a=a+b
# b=a-b
# a=a-b
# print(a,b)

# convert celsius to farenheit
# t=50
# f=t-32*5/9
# print(f"{f}")

# convert fernheit to celsius
# t=30
# c=t*9/5+32
# print(c)

# check whether the number is even or odd
# n=8
# if n%2==0:
#     print("even")
# else:
#     print("odd")


# check whether the string is polindrome or not
# n="python"
# if n[::-1]==n:
#     print("polindrome")
# else:
#     print("not polindrome")


# if a number is positive and negative and Zero
# n=5
# if n>0:
#     print("positive")
# elif n<0:
#     print("negative")
# else:
#     print("non positve and non negative")


# check whether the year is leafyaer or not
# n=1800
# if n%4==0:
#     print(f"{n} is leaf year")
# else:
#     print(f"{n} is not leaf year") 


# check whether the string is anagram or not
# n="listen"
# m="slient"
# k=sorted(n)
# print(k)
# j=sorted(m)
# print(j)
# if k==j:
#     print("anagram")
# else:
#     print("not anagram")


# check whether the number is prime or not:
# n=int(input("enter the number:"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("prime number")
# else:
#     print("not a prime")


# check whether the number is armstrong or not
# n=int(input("enter the number:"))
# s=n
# m=str(n)
# b=len((m))
# sum=0
# for i in m:
#     r=n%10
#     n=n//10
    
#     sum=sum+r**b
# if s==sum:
#     print("armstrong")
# else:
#     print("not armstrong")


# create a simple calculator
# print("""----basic calculation-----
#       1.addition
#       2.subtraction
#       3.multiplication
#       4.division""")
# print()
# n1=eval(input("enter the the value:"))
# n2=eval(input("enter the value:"))
# op=input("choose the options to perform calculation:")
# if op=='1':
#     print(f"addition of the two numbers is:{n1+n2} ")
# elif op=='2':
#     print(f"subtraction of the two numbers is:{n1-n2}")
# elif op=='3':
#     print(f"multiplication of the two numbers is:{n1*n2}")
# elif op=='4':
#     print(f"division the two numbers is :{n1//n2}")
# else:
#     print("unkown option please check the option once")


# sum of the digits of a number
# n=12345
# m=str(n)
# sum=0
# for i in m:
#     r=n%10
#     n=n//10
#     sum=sum+r
# print(sum)


# factorial of the number
# n=int(input("enter the number:"))
# m=1
# for i in range(1,n+1):
#     m=m*i
# print(f"factorial of  {n} is: {m}")

# reverse of the number using loop
# n=12345
# m=str(n)
# rev=0
# for i in m:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# print(rev)


# check whether the number is polindrome or not
# n=12321
# rev=0
# s=n
# m=str(n)
# for i in m:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# if s==rev:
#     print("polindrome")
# else:
#     print("not polindrome")


# count the digits in a number
# n=123457788344
# count=0
# m=str(n)
# for i in m:
#    n=n//10
#    count=count+1
# print(count)

# calculate the multiplication of the table
# n=int(input("enter the number:"))
# for i in range(1,11):
#     print(n,'x',i,'=',i*n)


# sum of the natural numbers using loops
# n=10
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)


# fibnocci series by using loop
# n1=0
# n2=1
# sum=0
# for i in range(0,7):
#     print(sum,end=" ")
#     n1=n2
#     n2=sum
#     sum=n1+n2


# sum of n natural numbers with up to a limit
# n=int(input("enter the value:"))
# r=n*(n+1)/2
# print(int(r))


#factors of the given number
# n=int(input("enter the value"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")

 
# import calendar
# year=int(input("enter the year:"))
# month=int(input("enter the month:"))
# day=int(input("enter the day:"))
# res=calendar.month(year,month,day)
# print(res)

# determine the number of days in two dates
# from datetime import date
# start_date=date(2002,7,1)
# end_date=date(2025,7,1)
# res=end_date-start_date
# print(res)


#reverse a string
# reverse a string
# n="python"
# r=n[::-1]
# print(r)



# write a function to calculate the factorial of the number
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# print(factorial(5))
# print(factorial(7))
# print(factorial(8))


# write the function check whether the number is prime or not
# def is_primes(n):
#     count=0
#     for i in range(1,n+1):
#        if n%i==0:
#         count=count+1
#     if count==2:
#         return("prime")
#     else:
#        return("not prime")
# print(is_primes(5))
# print(is_primes(10))
# print(is_primes(17))
       

# def is_primes(n):
#     l1=[]
    
#     for i in range(1,n+1):
#         if i>2:
#          for j in range(2,i):
#             if i%j==0:
#                 break
#          else:
#           l1.append(i)
#     return l1
# print(is_primes(10))


# count the number of vowels in a string
# n="aeroplane"
# m=[]
# count=0
# for i in n:
#     if i in "aeiou":
#         count+=1
#         m.append(i)
# print(count)

 

# lenght of the string:
# n="ramesh"
# m=len(n)
# print(m)


# convert the string into lowercase
# n="RUPESH"
# m=n.lower()
# print(m)


# concatenate the strings
# n="python"
# m="developer"
# d=n+" "+m
# print(d)

# write the program to print element and count in a tuple in a list
# l1=[1,2,1,3,1,4,5,2,6]
# l2=[]
# l3=[]
# for i in l1:
#     if i not in l2:
#         l2+=[i]
# for x in l2:
#     count=0
#     for y in l1:
#         if x==y:
#             count+=1
#     l3+=[(x,count)]
# print(l3)


# write a program to print the numbers in first and all the zeroes in end in a list
# def list_items(l1):
#       l2=[]
#       l3=[]
#       for i in l1:
#         if i!=0:
#            l2+=[i]
#         else:
#             l3+=[i]
#       return(l2+l3)
# print(list_items([1,0,4,2,0,6,3,0,5]))


# write the program to print unique element in a first position in a list
# l1=[5,1,2,1,3,4,2,4,3,6]
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2+=[i]
# for x in l2:
#     count=0
#     for y in l1:
#         if x==y:
#          count+=1
#         if count==1:
#            print(x)
#         break


# write the program  to combine the first element in first list and first element in second list in a tuple
# l1=[1,2,3,4]
# c=0
# l2=[5,6,7,8]
# l3=[]
# for i in l1:
#     c+=1
# i=0
# while i<c:
#     l3+=[(l1[i],l2[i])]
#     i+=1
# print(l3)
    


# write the program to print string into integer without using  built in functions
# def count(s):
#     c=0
#     for i in s:
#         c+=1
#     return c
# def string_to_integer(s):
#     digits = {
#         '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
#         '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
#     }

#     result = 0
#     i = 0

#     while i< count(s):
#         dig = digits[s[i]]

#         result = result * 10 + dig  #45
#         i += 1

#     return result

# s="456"
# print(string_to_integer)



# print the program to print reverse of the list without using built in functions
# l1=[1,2,3,2,5]
# l2=[]
# c=0
# for i in l1:
#     c+=1
# # print(c)
# v=c-1
# while v>=0:
#     l2+=[l1[v]]
#     v-=1
# print(l2)


# n="rup*#esh@1345"
# l1=""
# l2=""
# l3=""
# dict={}
# for i in n:
#     if i in "abcdefghifklmnopqrstuvwxyz":
#         l1+=i
#     elif i in "123456789":
#         l2+=i
#     else:
#         l3+=i
# dict["alpha"]=l1
# dict["dig"]=l2
# dict["symbol"]=l3
# print(dict)

# write the program to print count of the string
# s="rupesh"
# count=0
# for i in s:
#     count+=1
# print(count)


# count the number of occurance of the character in a string
# n="aeroplane"
# m={}
# for i in n:
#     if i in m:
#         m[i]+=1
#     else:
#         m[i]=1
# print(m)


# count the number of words in a sentence
# n="the sun rises in the east"
# b=n.split()
# count=0
# for i in b:
#     count+=1
# print(count)


# convert the list of strings into upper case
# n=["ramresh","yesu","eagle"]
# for i in n:
#     print(i.upper())



# write the program to distrubute the 14 pens to 3 numbers and remaining is 2
# n=14
# m=3
# b=n//m
# print("pens for each student is",b)
# c=n%m
# print("remaining pens is",c)


# check whether the email is valid
# email="kokkiligaddarupesh@gmail.com"
# if email=="kokkiligaddarupesh@gmail.com":
#     print("valid email")
# else:
#     print("invalid email")


# average of the list
# n=[1,2,3,4,5,6,7]
# sum=0
# for i in n:
#     sum+=i
#     c=0
# for j in  n:
#     c+=1
#     b=sum//c
# print(b)



# write the program for factorial of the number
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# print(factorial(5))


# write the program to fibnocci series
# fibnocci series of the number
# a,b=0,1
# n=10
# for i in range(0,n+1):
#         if i==n-1:
#           print(a,end=" ")
#         a,b=b,a+b



# def max_num(l1):
#     largest=l1[0]
#     for i in l1:
#         if i>largest:
#           largest=i
#     return largest
# l1=[1,9,2,3,4,5,6,7,10,0]
# print(max_num(l1))


#print year is leaf year or not
# year=int(input("enter the year:"))
# if year%4==0 and year%400==0 or year%100!=0:
#     print(f"{year} is leaf year")
# else:
#     print(f"{year} is not leaf year")


#retrive the leaf years from the list
# l1=[1900,2000,2100,2024,2030]
# for i in l1:
#     if i%4==0 and i%400==0 or i%100!=0:
#         print(i)

#reverse of the number
# n=123
# m=str(n)
# rev=0
# for i in m:
#     r=n%10
#     n=n//10
#     rev=rev*10+r
# print(rev)


#sum of the digits of the numbers
# n=1234
# m=str(n)
# sum=0
# for i in m:
#     r=n%10
#     n=n//10
#     sum=sum+r
# print(sum)



# count the no of digits in a value
# n=123456
# m=str(n)
# c=0
# for i in m:
#     r=n%10
#     n=n//10
#     c+=1
# print(c)


#reverse the every number in list
# l1=[123,345,6789,987]
# for i in l1:
#     m=str(i)
#     rev=0
#     for j in m:
#         r=i%10
#         i=i//10
#         rev=rev*10+r 
#     print(rev)


#retrive the number is polindrome or not
# n=int(input("enter the value:"))
# s=n
# m=str(n)
# rev=0
# for i in m:
#     r=n%10
#     n=n//10
#     rev=rev*10+r
# if s==rev:
#     print("polindrome")
# else:
#     print("not polindrome")


# l1=[1234,12321,161,145,154,151]
# for i in l1:
#     m=str(i)
#     rev=0
#     for j in m:
#         r=i%10
#         i=i//10
#         rev=rev*10+r
    
#     if i==rev:
#            print(f"{j:rev}")



# print the magic number
# n=1234
# m=str(n)
# sum=0
# for i in m:
#     r=n%10
#     n=n//10
#     sum=sum+r
# v=str(sum)
# c=0
# for j in v:
#     b=sum%10
#     sum=sum//10
#     c=c+b
# print(c)
# if c==1:
#      print("magic number")
# else:
#      print("not magic number")






# prime numbers with in the range:
# --------------------------------
# n = 10
# for i in range(2, n+1):
    
#     for j in range(2, i):
#         if i % j == 0:
            
#             break
#     else:
#         print(i,end="")


# fibinocci series
# n1=0
# n2=1
# sum=0
# for i in range(1,10):
#     print(sum,end=" ")
#     n1=n2
#     n2=sum
#     sum=n1+n2


# n1=0
# n2=1
# sum=0
# for i in range(1,10):
#     print(sum,end=" ")
#     n1=n2
#     n2=sum
#     sum=n1+n2
    
    
#     if i==3:
#         print("the given number is in fibinocci series")
#     else:
#        print("the given number is not there in fibinocci series")


n=1689
print(n)
print()
print(hex(n))


    











     



    


        

    
    
     
       




        



            

        



    







    


    
        

