# l1="Banana"
# l2=[i for i in l1 if i.isupper()]
# print(l2)

# l1=[1,2,3,4,5]
# l2=[i**2 if i%2==0 else i**3  for i in l1  ]
# print(l2)

# l1=["kiran","mahesh","yesu"]
# l2=[i.upper() for i in l1 if len(i)>4 ]
# print(l2)
    
# l1=["ramu","gopi","hema"]
# l2=[i[: : -1] for i in l1 if len(i)]
# print(l2)

# l1="hello world"
# l2=["*" if i in "aeiou" else i for i in l1 ]
# print(l2)


# s1=list{ i**2 for i in range(1,10) }
# print(s1)


# s1="applebanana"
# s2={i for i in s1  }
# print(s2)

# s1=[1,2,2,3,3]
# s2={ i for i in s1 if s1.count(i)>1 }
# print(s2)
        
    
# s1={ i for i in range(1,20) if i%2==0}
# print(s1)


# s1="ThE sun risEs in thE East"
# s2={i   for i in s1 if i.lower() if i in "aeiou"}
# print(s2)
    
    
# s1=[11,22,33,44,11,55]
# s2={ i for i in s1 if i%11==0}
# print(s2)


# s1=["oxygen","union","ramesh","lokesh"]
# s2={ i for i in s1 if i[0] not in "aeiou"}
# print(s2)

     
# s1=[23,45,78,90679]
# s2={i%10 for i in s1  }   
# print(s2)

      
# s1=["apple","banana","orange","cherry"]
# s2=["apple","mango","tamato","cherry"]
# s3={ j for i in s1 for j in s2 if i==j }
# print(s3)


# s1=[[1,2],[3,4],[1,2],[5,6]]
# s2={ j for i in s1 for j in i}
# print(s2)

        
# d1={i:i**2 for i in range(1,6)}
# print(d1)
        

# d2={i:"even" for i in range(1,10) if i%2==0  }
# print(d2)


# d1={ i:"even" if i%2==0 else "odd" for i in range(1,20)}
# print(d1)


# d1=["ramesh","kotesh","merra"]
# d2={i:len(i) for i in d1}
# print(d2)


# d1=[("a",1), ("b",2),("c" ,2)]
# d2={i:j for i,j in d1 }
# print(d2)


# d="hema"
# s={i:ord(i)for i in d}
# print(s)


# t1=[[1,2],[3,4],[4,5]]
# t2=tuple(j for i in t1 for j in i)
# print(t2)

# t1=("python developer","django developer","tuple comprehension")
# t2=tuple("-".join(i.split())  for i in t1)
# print(t2)


# t1=("python developer","django developer","tuple comprehension")
# t2=tuple("-".join(i.title().split())  for i in t1)
# print(t2)


# n1=[3,4,5,6,7]
# n2=[1,2,3,4,5]
# n3={j for i in n1 for j in n2 if i==j}
# print(n3)


# s1=[["3","3","3"],["2","2"],["1"]]
# s2={tuple(int(j)for j in i) for i in s1 }
# print(s2)


# s1=[["3","3","3"],["2","2"],["1"],"345"]
# s2={sum(int(j)for j in i) for i in s1 }
# print(s2)


# c="myanmar"
# d={i:c.count(i) for i in c }
# print(d)

# c="america"
# d={c.index(i):i for i in c}
# print(d)


# g=(["eshwar","rudra","adhi"],["bhavani","parvathi","ardhanarri"],["ganesh","lambodhar","vinayaka"])
# r={g.index(i):tuple(j for j in i if j[0] in "aeiou") for i in g }
# prin


# begin = int(input("sdfs"))
# end = int(input("sdfs"))
  
# c = 1
# while c <8:
#     a = random.randint(100000,999999)
#     if int(str(a)[-1]) == 4:
#         print(a)
#         c +=1

# from random import *
# for i in range(7):
#     number=uniform(3,9)
#     print(f"{number:.3f}")

    
# for i in range(5,0,-1):
#     for j in range(i):
#         print(i,end="")
#     print("")
   

# sub=lambda x:x**3 
# print(sub(20))

# max=lambda x,y:x  if x<y else y
# print(max(10,4))

# even=lambda x:"even" if x%2==0 else "odd"
# print(even(5)

# num=lambda x: f"{x} is positive"  if x>0  else  f"{x} is non positive and non negative"if x==0 else f"{x} is negative"
# print(num(0)) 

# num=lambda list1:[i**2  for i in list1]
# print(num([1,2,3,4,5]))
 
# is_palindrome=lambda s:"polindrome"    if s==s[:: -1]  else "not polindrome"
# print(is_palindrome("vivo"))


# even=lambda x,y: [ i for i in range(x,y+1) if i%2==0]
# print(even(2,20))




# words=list(filter(lambda x: len(x)>3  and x[0] in ("AEIOUaeiou"),["taj maha","austrich","esha","umesh"]))
# print(words)

# dict={"1st":6089,"2nd":9876,"3rd":2017,"4th":1900,"5th":2096}
# years=list(filter(lambda x:  x%400==0 or (x%4==0 and x%100!=0),{"1st":6089,"2nd":9876,"3rd":2017,"4th":1900,"5th":2096}.values()))
# print(years)

# squares = list(map(lambda x : x.upper() ,['Harish','TCS','hyderabad']))
# print(squares)

# n=12345
# count=0
# if n==0:
#     count=1        #length of the digit without using built in functions
# else:
#     while n!=0:
#         n=n//10
#         count +=1
# print(count)



# l1=[1,2,3]
# l2=[5,6,7]
# print(list(zip(l1,l2)))


# s="""Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are"""
# print(s)


# s="trinesh rao"
# print(s[::-1])


# n=7

# if n%2==0:
#     print(True)
# else:
#     print(False)


# def even_odd(n):
#     if n%2==0:
#         print(True)
#     else:
#         print(False)
# even_odd(5)


# n=2
# for i in range(1,11):
#     print(i,"x",n,"=",i*n)


# sum=0
# for i in range(1,7):
#      if i**3:
#       print(sum)
#       sum+=i
     

# n=7
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# x=4
# print(isinstance(x,int))


# for i in range(20,50):
#      for j in range(2,i):
#        if i%j==0:
          
#           break
#      else:
#         print("prime is",i)



# n=5
# factorial=1
# i=1
# while i<=n:
#     factorial*=i
#     i+=1
# print(factorial)


# l1=[60,4,9,16,25,90,500]
# largest=0
# for i in l1:
#     if i>largest:
#         largest+i
        #   largest=i
# print(largest)


# level=input("please enter the levels easy/hard:").lower()
# if level=="easy":
#     level=10
# elif level=="hard":
#     level=5
# from  random import *
# num=randint(1,100)
# n=5
# while n<=level:
#         guessnum=int(input("guess the number"))
#         if guessnum<num:
#             print("your guess is lessthan guessnumber" )
#         elif guessnum==num:
#             print("your guess is sucessfully guess number")
#         else:
#             print("your guess number is higher than the guess number")
#         n+=1


# for i in range (1,10):
#     if i%2==0:
#         print(i)


# n=6
# if n%2==0:
#     print("even")
# else:
#     print("odd")



# even_sum=0
# odd_sum=0
# for i in range(1,10):
#     if i%2==0:
#         even_sum+=i
#     else:
#         odd_sum+=i
# print("sum of the even numbers:",even_sum)
# print("sum of the odd numbers:",odd_sum)



# even_sum=0
# odd_sum=0
# n=[22,1,1,4,5,6,1]
# for i in n:
#     if i%2==0:
#         even_sum+=i
#     else:
#         odd_sum+=i
# print("sum of the even numbers is:",even_sum)
# print("sum of the odd numbers is:",odd_sum)


    


    
    





    





