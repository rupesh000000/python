
# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# s=is_even(9)
# print(s)
# if s==True:
#     print("successful")
# else:
#     print("unsuccessfull")



# def factors(n):
#     m=[]
#     for i in range(1,n+1):
    
#         if n%i==0:
#             m.append(i)
#     return m
# s=factors(21)
# print(s)
# for i in s:
#       if i%2==0:
#             print(True)
#       else:
#             print(false)


# def perfect(n):
#     sum=0
#     for i in range(1,n):
#         if n%i==0:
#             sum+=i
#     return sum
# s=perfect(496)
# print(s)
# if s==perfect(s):
#     print("perfect number")
# else:
#     print("not prefect")

    
# m=[]
# for i in range(1,11):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
        
#         else:
#             m.append(i)  
# print(m)


# def even_odd(n):
#     if n%2==0:
#         return(n,"is even")
#     else:
#         return(n,"is odd")
# n=5
# print(even_odd(n))



# def even_odd(n):
#  for i in range(1,n+1):
#     if i%2==0:
#         print(i,"is even")
#     else:
#         print(i," is odd")
# even_odd(21)


# def fizz_buzz(n):
#  for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         print(i,"fizzbuzz")
#     elif i%3==0:
#         print(i,"fizz")
#     elif i%5==0:
#         print(i,"buzz")
#     else:
#         print(i)
# fizz_buzz(50)



# n=153
# t=n
# sum=0
# count=0
# x=n
# while n>0:
#     k=n%10
#     n=n//10
#     count+=1
# # print(n)
# # print(count)
# while t>0:
#     h=t%10
#     sum=sum+h**count
#     t=t//10
#     # print(sum)
# # print(t)
# if x==sum:
#         print("armstrong number")
# else:
#         print("not a armstrong number")



# i=1
# fact=1
# while i<=7:
#     fact=i*fact
#     i+=1
# print(fact)



# l1=[2,5,9,4,10,90,70,80]
# largest=l1[0]
# for i in l1:
#     if i>largest:
#         largest=i
# print(largest)


# n=12321
# k=n*10
# m=k//10
# if n==m:
#     print("is polindrome")
# else:
#     print("is not polindrome")


# fact=1
# n=5
# for i in range(1,n+1):
#     fact*=i
# print(fact)


# n=3
# for i in range(1,n+1):
#     print("*"*3)


# n=5
# for i in range(1,n+1):
#     print(i*"*")


n=4
t=n-1
for i in range(1,n+1):
    print(" "*t, i*" *")
    t-=1



# k="apple"
# j="leapp"
# h=" "
# for i in k:
#     h+=j
#     if i in h:
#         print("anargram")
#     else:
#         print("not anargram")


# my_list = [1, 2, 3, 4, 5]

# # Get length of the list
# n = len(my_list)

# # Swap elements in place
# for i in range(n // 2):
#     temp = my_list[i]
#     my_list[i] = my_list[n - 1 - i]
#     my_list[n - 1 - i] = temp
# print(my_list)


# numbers = [2, 4, 3, 5, 7, 8, 1]
# target = 9
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#              print(f"Pair found: ({numbers[i]}, {numbers[j]})")


# n=4
# t=n-1
# for i in range(1,n+1):
#     print(" "*t, i*" *")
#     t-=1
# n=4
# t=0
# for i in range(n-1,-1,-1):
#     print(" "*t,i*" *")
#     t+=1

# calendar of the year
# import  calendar
# year=int(input("enter the year:"))
# res=calendar.calendar(year)
# print(res)


# import calendar
# year=int(input("enter the year:"))
# month=int(input("enter the month:"))
# day=int(input("enter the day:"))
# res=calendar.month(year,month,day)
# print(res)


# m="abcabc"
# n=list(set(m)) 
# print(n)


# name = "Iam a Django Developer"
# print("===Before Operation===")
# print("The Value is ;",name)
# print()
# print("Count of name is :",len(name))
# print("===After Operation===")
# req = name.split()
# print("The value is :",req)
# print()
# print("Count of req is :",len(req))



# n=int(input("enter the number:"))
# def factors(n):
#     l=[]
#     for i in range (1,n+1):
#         if n%i==0:
#             l.append(i)
#     return l
# print(factors(n))
# l1=[]
# for i in factors(n):
#     if i>1:
#      for j in range(2,i):
#         if i%j==0:
#             break
#      else:
#         l1.append(i)
# print(l1)



# l1=[12321,121,4554,154]

# l2=[]
# for i in l1:
#     rev=0
#     s=i
#     while i!=0:
#       r=i%10
#       rev=rev*10+r
#       i=i//10
# if s==rev:
#    l2.append(rev)
#    print(l2)




# n=[3,0,2,0,1,3,4]
# m=[]
# for i in n:
#     if i not in m:
#      m.append(i)
# print(m)


# def count(s):
#     c=0
#     for i in s:
#         c+=1
#     return c
# def string_to_integer(s):
#     i=0
#     result=0
#     digit={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#     while i<count(s):
#         dig=digit[s[i]]
#         result=result*10+dig
#         i+=1
#     return result
# s="456"
# print(string_to_integer(s)


























        



            

        



    







    


    
        




            





