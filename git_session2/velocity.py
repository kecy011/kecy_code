from math import sqrt

def velocity(u, a, t):
    v = u + (a * t)
    pass
    print(" the velocity is " , v)
    
    
def speed (u, a, t):
    speed = u * t + ((a * t)**2)/2
    pass 
    print("the speed is ", speed)
    
    
def velocity_two(u, a, s):
     v2 = ((u**2)+(2 * a)*s)
     result = sqrt(v2)
     pass
     print ("your velocity_two is ", result)
     
     
print(velocity_two(6, 7, 9))
print(speed(12, 8,10))
print(velocity(13,17, 8))
     
    
