import math

def sqrt_command(command):
    sqrt, number_str = command.split()
    x = int(number_str)
    sqrt_x = math.sqrt(x)
    response = f'{x} ノ平方根ハ {sqrt_x} デス'
    return response
