class Machine():
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"Machine {self.name} is worked")

    def stop(self):
        print(f"Machine {self.name} is stopped")

class Excavator(Machine):
    def __init__(self, name):
        super().__init__(name)

class Buldozer(Machine):
    def __init__(self, name):
        super().__init__(name)

class Truck(Machine):
    def __init__(self, name):
        super().__init__(name)

Truck = Machine("truck")
Buldozer = Machine("buldozer")
Excavator = Machine("excavator")

machines = [Truck, Buldozer, Excavator]

for i in machines:
    i.work()
    i.stop()






