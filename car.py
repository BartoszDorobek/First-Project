class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def is_fast(self):
        if self.speed > 100:
            return True
        else:
            return False

    def print_name(self):
        print(self.name)

