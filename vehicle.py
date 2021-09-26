from environment import Environment


class Vehicle(object):
    def __init__(self,env,origin, destination, Vspeed):
        self.origin = origin
        self.destination = destination
        self.Vspeed = Vspeed
        self.location = None
        self.next_intersection = None
        self.trial = None
        self.env = env
        self.depart_time = 0
        self.arrive_time = 0
        self.success = False

    def update(self):
        self.update_next_intersection()
        self.update_location()
        self.save_trial()
        if self.location == self.destination:
            self.success = True

    def update_next_intersection(self):
        adjacent_Q = self.env.adjacent_Qtable()
        j = min(adjacent_Q)

