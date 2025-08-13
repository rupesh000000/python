# class Person():
#     name="bike"    
#     def bike_parts(self):
#         print("r15")
#         print("bullet")
#     def bike_working(self):
#         print("moving front side")
#         print("moving back side ")
    
# m1=Person()
# m1.bike_parts()
# m2=Person()
# m2.bike_parts()
# m1.name
# m3=Person()
# m3.bike_working()
    
    
    
# class Amazon():
#     products=id,"name","price","company"
#     def add_products(self):
#         print("pid=234")
#         print("pname=vivomobile")
#         print("price=30000")
#         print("comp any=vivo")
#     @classmethod
#     def add_products(self):
#         print("pid=234")
#         print("pname=vivomobile")
#         print("price=30000")
#         print("company=vivo")
    
# m1=Amazon()
# m1.add_products()
# m2=Amazon()
# m2.add_products()
# m3=Amazon()
# m3.add_products()


# class calculator():
#     @staticmethod
#     def add(*args):
#         adds=0
#         for i in args:
#             adds=adds+i
#         return adds
#     @staticmethod
#     def sub(*args):
#         subs=0
#         for i in args:
#             subs=subs-i
#         return subs
#     @staticmethod
#     def multiple(*args):
#         multiples=1
#         for i in args:
#             multiples=multiples*i
#         return multiples
#     @staticmethod
#     def div(*args):
#         division=args
#         for i in args[1:]:

# print(f"sum is:{calculator.add(20,50,70)}")
# print()
# print(f"subtraction is:{calculator.sub(20,70,50,60)}")
# print()
# print(f"multiplication is:{calculator.multiple(3,4,2,2)}")



# class Triangle():
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def area(self,base,height):
#         return 0.5*(base*height)
#     def perimeter(self):
#         return self.a+self.b+self.c
#     def pythagoras_therom(self):
#         sides=sorted([self.a,self.b,self.c])
#         return sides[2]**2==sides[0]**2+sides[1]**2
# t=Triangle(3,4,8)
# print("area of triangle is:",t.area(3,4))
# print()
# print("perimeter of triangle is:",t.perimeter())
# print()
# print("pythagoras therom is:",t.pythagoras_therom())


# class Circle():
#     def __init__(self,radius,diameter):
#         self.a=radius
#         self.b=diameter
#     def area(self):
#         return 3.14*self.a**2
#     def circumference(self):
#         return 2*3.14*self.a
#     def arc_lenght(self,lenght,angle_redians):
#         lenght=self.a*angle_redians
#         return lenght
# c=Circle(4,60)
# print("area of circle is:",c.area())
# print()
# print("circumference of a circle is:",c.circumference())
# print()
# print("arclenght of a circle is:",c.arc_lenght(4,60))


# class Rectangle():
#     def __init__(self,lenght,breadth):
#         self.lenght=lenght
#         self.breadth=breadth
#     def area(self):
#         return self.lenght*self.breadth
#     def perimeter(self):
#         return 2*(self.lenght+self.breadth)
#     def diagonal(self):
#         return (self.lenght**2+self.breadth**2)**0.5
# r=Rectangle(4,5)
# print("area of rectangle is:",r.area())
# print()
# print("perimeter of a rectangle is:",r.perimeter())
# print()
# print("diagonal of the rectangle is:",r.diagonal())


# class Square():
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side**2
#     def perimeter(self):
#         return 4*self.side
#     def diagonal(self):
#         return self.side*2**0.5
# s=Square(5)
# print("area of square is",s.area())
# print()
# print("perimeter of a square is",s.perimeter())
# print()
# print("diagonal of square is:",s.diagonal())
# print()


# class Eyeglasses:
#     a="we have two glasses" 
#     def __init__(self,colour,range):
#         self.colour=colour
#         self.range=range
#     def printing(self):
#         print(self.colour)
#         print(self.range)
#         print(self.a)
        

# c=Eyeglasses("black",1.5)
# print("how many glasses for the eyeglasses:",c.a)
# print("the colour of the eyeglass",c.colour)
# c1=Eyeglasses("white",3.6)
# print("the colour of a eyeglass is:",c1.colour)
# print("the range of eyesite  is:",c1.range)
# c3=Eyeglasses("blue",3.9)
# c3.printing()


# class Mobile:
#     asspeaker=True
#     def __init__(self,mname,mcompany,mprice):
#         self.mname=mname
#         self.mcompany=mcompany
#         self.mprice=mprice
#     def mobile_uses(self):
#         print("communicate with to another person in",self.mname)
#         print("to see the movies and music in",self.mname)
#         print("to see the youtube vidoes in",self.mname)
#     @classmethod
#     def product1(cls, type):
#         type.mname = "Realme"
#         print(cls.asspeaker)

#     # @staticmethod
#     # def product2
        
    
# m=Mobile("vivo mobile","vivo company",30000)
# m.mobile_uses()
# print(m.mname)
# m.product1(m)
# print(m.mname)

# class Eyeglasses:
#     def __init__(self,range):
#         self.range=2.5       
# class Coolglasses(Eyeglasses):
#     def __init__(self,coolglass,range):
#         super(). __init__(self.range)
#         print("coolglasses cools the eyes")
# class Sunglasses(Eyeglasses):
#     def product2(self):
#         super().product1()
#         print("sunglasses are used in outdoor")
# glasses=Coolglasses()
# # glasses.product1()
# glasses.product2()


#over loading example:
# from multipledispatch import dispatch
# class Addition:
#     @dispatch(int,int)
#     def add(self, a, b):
#         print(a+b)
#     @dispatch(int,int,int)
#     def add(self, a,b,c):
#         print(a+b+c)
#     @dispatch(str,str)
#     def add(self,x,y):
#         print(x+y)
# m1=Addition()
# m1.add(1,2)
# m1.add(1,2,3)
# m1.add("python","developer")








    









    




