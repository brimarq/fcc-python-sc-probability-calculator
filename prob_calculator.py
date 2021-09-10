import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = [
          color for color in kwargs for _ in range(kwargs[color]) 
        ]
        
    def draw(self, num_balls):
        drawn_balls = []

        if num_balls > len(self.contents): 
            return self.contents

        for _ in range(num_balls):
            drawn_balls.append(
                self.contents.pop(
                    self.contents.index(
                        random.choice(self.contents)
                    )
                )
            )
 
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    success = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        matching_drawn_balls = {
            k: drawn_balls.count(k) for k, v in expected_balls.items() if drawn_balls.count(k) >= v
        }

        if len(matching_drawn_balls) == len(expected_balls):
            success += 1

    return success / num_experiments
