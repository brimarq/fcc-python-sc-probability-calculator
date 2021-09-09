import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        # Nested list comprehensions are NOT intuitive! 
        # for/if clauses nest in the same order as if written 
        # with for loops and if statements. See PEP 202: 
        # https://www.python.org/dev/peps/pep-0202/#the-proposed-solution
        self.contents = [
          key for key in kwargs for _ in range(kwargs[key]) 
        ]
        
        



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass

hat = Hat(black=6, red=4, green=3)
print(hat.contents)
