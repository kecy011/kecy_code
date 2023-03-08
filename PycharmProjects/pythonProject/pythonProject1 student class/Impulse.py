class Impulse:

    def __init__(self, force,time, mass, velocity):
        self.force = force
        self.time = time
        self.mass = mass
        self.velocity = velocity

    def get_force(self, mass, acceleration): 
        return mass * acceleration 

    def get_time(self, velocity, initial_velocity, acceleration):
        time = (velocity -initial_velocity)/acceleration
        return time

    def get_mass(force, acceleration):
        return force/acceleration

    def get_velocity(self, u, a, t):
        return  u + (a*t)
                               

