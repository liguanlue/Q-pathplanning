import time
from environment import Environment


class simulator(object):
    def __init__(self, env, update_dalay=1.0):
        self.env = env
        self.size = env.grid_size

        self.quit = False
        self.start_time = None
        self.current_time = 0.0
        self.last_update = 0
        self.update_delay = update_dalay

    def run(self, n_trial=10):
        self.start_time = time.time()
                                          #create vehicles

        while True:
            try:
                self.current_time = time.time() - self.start_time
                if self.current_time - self.last_update > self.update_delay:
                    self.env.step()
                    self.last_update = self.current_time

            except KeyboardInterrupt:
                self.quit = True
            finally:
                if self.quit:
                    break
            if self.quit:
                break
