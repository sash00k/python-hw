import numpy as np
import matplotlib.pyplot as plt
from functools import wraps
from time import time
from copy import deepcopy

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print (f'took: {te-ts: .5} sec')
        return result
    return wrap

class Life:
    def __init__(self, size: int = 128, map_type: str = 'numpy array', random_seed: int = None):
        if random_seed:
            np.random.seed(seed=random_seed)
        self.size = size
        self.map = np.random.randint(0, 2, size=(size, size))
        if map_type == 'python list':
            self.map = self.map.tolist()

    def get_neighbours_sum(self, i: int, j: int) -> int:
        shifts = (-1, 1)
        result = 0
        for d_i in shifts:
            for d_j in shifts:
                try:
                    result += self.map[i+d_i][j+d_j]
                except IndexError:
                    pass
        return result

    def make_step(self):
        new_state = deepcopy(self.map)
        for i in range(self.size):
            for j in range(self.size):
                summa = self.get_neighbours_sum(i, j)
                if not self.map[i][j] and summa == 3:
                    new_state[i][j] = 1
                elif self.map[i][j] and summa not in (2, 3):
                    new_state[i][j] = 0
        self.map = new_state

    @timing
    def simulation(self, steps_num: int = 128):
        for i in range(steps_num):
            # if i % 8 == 0:
            #     print(f'{i: <3} steps done')
            self.make_step()
    @property
    def count_alive_ones(self) -> int:
        return sum(sum(self.map,[])) if isinstance(self.map, list) else self.map.sum()

    def show(self):
        plt.axis('off')
        plt.imshow(np.asarray(self.map) * 255, interpolation='none', cmap='Greys_r')

    def save_image(self, name: str = 'image'):
        self.show()
        plt.savefig(f'{name}.png', dpi=1024, bbox_inches='tight', pad_inches=0)

if __name__ == '__main__':
    for case in ('numpy array', ):
        life = Life(size=1024, map_type=case, random_seed=42)
        life.simulation(steps_num=128)
        print(life.count_alive_ones)
        life.save_image(name=f'15_{case}')

    # python list: 153.58 sec
    # numpy array: 270.89 sec