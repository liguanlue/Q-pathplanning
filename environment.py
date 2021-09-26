from collections import OrderedDict
import random


class TrafficLight(object):
    valid_state = [True, False]   # True = NS open, False = EW open

    def __init__(self,state=None,period=None):
        self.state = state if state is not None else random.choice(self.valid_state)
        self.period = period if period is not None else random.choice([3,4,5])
        self.last_update = 0

    def reset(self):
        self.last_update = 0

    def update(self,t):
        if t-self.last_update>self.period:
            self.state = not self.state
            self.last_update = t


class Environment(object):

    def _init_ (self,grid_size=(8,6),origins=None,destinations=None):
        self.grid_size = grid_size
        self.intersections = OrderedDict()
        self.Q_table = OrderedDict()
        self.dij = 1000
        self.flowspeed = 10
        self.origins = origins
        self.destinations = destinations
        self.alpha = 0.5
        self.gamma = 0.5
        self.epsilon = 0.5
        self.t = 0
        self.vehicles = OrderedDict()
        for x in range (1,self.grid_size[0]+1):
            for y in range (1,self.grid_size[1]+1):
                self.intersections[(x,y)] = TrafficLight()     #路口
        for d in range(self.destinations):
            for i in range(self.intersections):
                for j in range (self.intersections):
                    if (abs(i[0]-j[0]) + abs(i[1]-j[1])) == 1:
                        self.Q_table[(d, i, j)] = 0
                    if j == d and (abs(a[0]-d[0]) + abs(a[1]-d[1])) == 1:
                        self.Q_table[d, i, j] = self.dij/self.flowspeed      #初始化Q表

    def set_q(self, destinations):
        for d in destinations:
            for a in self.intersections:
                for b in self.intersections:
                    if (abs(a[0]-b[0]) + abs(a[1]-b[1])) == 1:
                        self.Q_table[d,a,b] = 0
                    if b == d and (abs(a[0]-d[0]) + abs(a[1]-d[1])) == 1:
                        self.Q_table[d,a,b] = self.dij/self.flowspeed

    def update_q_congestion(self, d, i, j, k, ct, etij):   #congestion 字典
        self.Q_table[d, i, j] = self.Q_table[d, i, j] + self.alpha * (
                ct-etij+self.Q_table[d, j, k]-self.Q_table[d,i,j])

    def update_q_no_congestion(self, d, i, j, k, tij):
        self.Q_table[d, i, j] = self.Q_table[d, i, j] + self.alpha * (
                    tij + self.Q_table[d, j, k] - self.Q_table[d, i, j])

    def step(self):
        for intersections, traffic_light in self.intersections.interitems():
            traffic_light.update(self.t)

        for vehicle in self.vehicles.interkeys():
            vehicle.update(self.t)

    def adjacent_Qtable(self,intersckey):
        if intersckey












