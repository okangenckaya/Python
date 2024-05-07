
class PC:

    def __init__(self, cpu, gpu, ram, disk):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.disk = disk

# We will take instance here:

pc_data = PC(cpu='i3 1200F', gpu='RX 6600', ram='16 GB DDR4', disk='WD Blue SN70 500GB')

print(f"""
CPU: {pc_data.cpu}
GPU: {pc_data.gpu}
RAM: {pc_data.ram}
Disk: {pc_data.disk}
""")
