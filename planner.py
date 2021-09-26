import random
from environment import Environment
from collections import OrderedDict


class Planner(object):
    def __init__(self,env,vehicle):
        self.env = env;
        self.vehicle = vehicle
        self.destination = None

    def next_intersection(self,d,k):
        q = {key: value for key, value in self.Q_table.item() if (abs(key[1]-k[0])+abs(key[2]-k[1]) == 1)}

        j = min(self.env.Q_table.get(d,k,k-1),self.env.Q_table.get(d,k,k+1),self.env.Q_table.get(d,k,k+1))



