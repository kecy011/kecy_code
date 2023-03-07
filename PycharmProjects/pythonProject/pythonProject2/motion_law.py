
from math import sqrt

def velocity(u,a,t):
    return u + (a*t)


def distance(u, t, a):
    return u * t + ((a*t) ** 2)/2


def velocity_two(u, a, s):
    v2 = u**2 + 2*(a * s)
    result = sqrt(v2)
    return result
#if __name__ == "__main__":
    #print(velocity(5, 3, 4))
   # print(distance(9, 7, 5))
    #print(velocity_two(10, 12, 7))

