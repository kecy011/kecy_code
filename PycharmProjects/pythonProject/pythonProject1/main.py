
print __name__
def mometum():
    mass=(float(input("enter your mass:")))
    velocity=(float(input("enter your velocity")))
    print(mass * velocity)

def impulse():
    force = float(input("enter the given force: "))
    time = float(input("enter the given time: "))
    print(force * time)

def velocity():
    u = float(input("enter your initial velocity given:"))
    a = float(input("enter the time given:"))
    t = float(input("enter the time given:"))
    print(u + (a * t))

def speed():
    u = float(input("enter the initial velocity given: "))
    t = float(input("enter the time given: "))
    a = float(input("enter the given acceletration: "))
    print((u * t) + ((a * (t**2))/2))

physics_problem = input("enter a problem to solve : ")
if physics_problem == mometum:
    mometum()
elif physics_problem == velocity:
    velocity()
elif physics_problem == impulse:
    impulse()
else:
    speed()








