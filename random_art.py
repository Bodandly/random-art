import random
from math import pi, sin, cos, tan, e
# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


class Expression:
    def __init__(self):
        self.commands = []

    def evaluate(self, x, y):
        value = 1
        for (command, coord, exp) in self.commands:
            if command == "sin" and coord == "x" and exp == "**1" :
                value *= sin(self.random_element(x, y) * x)
            elif command == "sin" and coord == "x" and exp == "**2":
                value *= sin(self.random_element(x, y) * x)
            elif command == "sin" and coord == "y" and exp == "**1":
                value *= sin(self.random_element(x, y) * y)
            elif command == "sin" and coord == "y" and exp == "**2":
                value *= sin(self.random_element(x, y) * y)
            elif command == "cos" and coord == "x" and exp == "**1":
                value *= cos(self.random_element(x, y) * x)
            elif command == "cos" and coord == "x" and exp == "**2":
                value *= cos(self.random_element(x, y) * x)
            elif command == "cos" and coord == "y" and exp == "**1":
                value *= cos(self.random_element(x, y) * y)
            elif command == "cos" and coord == "y" and exp == "**2":
                value *= cos(self.random_element(x, y) * y)
            elif command == "tan" and coord == "x" and exp == "**1":
                value *= (sin(x)/cos(x))
            elif command == "tan" and coord == "x" and exp == "**2":
                value *= (sin(x)/cos(x))
            # elif command == "tan" and coord == "y" and exp == "**1":
            #     value *= (sin(y)/cos(y))
            # elif command == "tan" and coord == "y" and exp == "**2":
            #     value *= (sin(y)/cos(y))

        return value

    def random_element(self, x, y):
        random_value = random.random()
        if random_value > 0.9:
            return cos(y * self.random_element(x, y))
        if random_value > 0.8:
            return cos(x)
        if random_value > 0.7:
            return pi * self.random_element(x, y)
        if random_value > 0.6:
            return sin(y)
        if random_value > 0.5:
            return cos(y * self.random_element(x, y))
        if random_value > 0.4:
            return sin(x)
        if random_value > 0.25:
            return cos(cos(pi * self.random_element(x, y)* x)* y)
        else:
            return sin(sin(pi *y)* x)


    def __str__(self):
        return str(self.commands)



def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    expr = Expression()
    for _ in range(random.randint(3, 5)):
        if random.random() > 0.5:
            x_or_y = "x"
        else:
            x_or_y = "y"

        rand_val = random.random()
        if rand_val > 0.5:
            sin_cos_tan = "sin"
        else:
            sin_cos_tan = "cos"




        exponent = "**" + str(random.randint(1,2))

        expr.commands.append([sin_cos_tan , x_or_y, exponent])

    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr.evaluate(x, y)
