
# How to create an object ?
class Vehicle:
    door = 4
    brand = ''
    model = ''
    engine_size = ''


define = Vehicle

define.door = 4
define.brand = 'BMW'
define.model = '5.20'
define.engine_size = '2.0'

print(f"""
Brand: {define.brand}
Model: {define.model}
Engine Size: {define.engine_size}
Door Number: {define.door}
""")

