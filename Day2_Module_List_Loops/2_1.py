import math as m
#1
def cal_area_of_circle(radius):
    area=m.pi*radius**2
    area=round(area,2)
    return area

print(cal_area_of_circle(5))

#2
def cal_hypo(x,y):
    z=m.sqrt(x**2+y**2)
    z=round(z,2)
    return z

print(cal_hypo(3,4))

#3
def degrees_to_radians(degree):
    radian=m.radians(degree)
    return radian

print(degrees_to_radians(180))


#4
def factorial(n):
    return m.factorial(n)

print(factorial(5))


#5
def logarithm(val,base): #log는 항상 val먼저임! 즉 log2의 16을 쓰고 싶으면 m.log(16,2) 써야한다!
    return m.log(val, base)

print(logarithm(100,10))


