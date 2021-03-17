from math import modf


class Carriage:
    def __init__(self, number, speed):
        self.number = number
        self.speed = speed


class Car(Carriage):
    def __init__(self, number, speed, fuel):
        Carriage.__init__(self, number, speed)
        self.fuel = fuel
        if self.fuel != 98:
            self.speed = self.speed - (self.speed / 100 * 10) if self.fuel == 95 else self.speed - (
                    self.speed / 100 * 20)


class Bike(Car):
    def __init__(self, number, speed, fuel):
        Car.__init__(self, number, speed, fuel)
        self.speed = speed
        if self.fuel != 98:
            self.speed = self.speed - (self.speed / 100 * 20) if self.fuel == 95 else self.speed - (
                    self.speed / 100 * 40)


racers_num, track_length, race_time = map(int, input().split(' '))


def add_racer(num):
    starting_field = []

    for _ in range(num):
        data = list(map(int, input().split(' ')))
        vehicle_type = data.pop(1)
        if vehicle_type == 3:
            starting_field.append(Carriage(*data))
        elif vehicle_type == 1:
            starting_field.append(Car(*data))
        elif vehicle_type == 2:
            starting_field.append(Bike(*data))

    return starting_field


def race(racers, time, length):
    to_finish = 1
    winner = 1

    for racer in racers:
        if winner < racer.number:
            winner = racer.number

    for racer in racers:
        if round((modf(racer.speed * time / length))[0], 3) > 0.5:
            if 1 - round((modf(racer.speed * time / length))[0], 3) <= to_finish:
                to_finish = 1 - round((modf(racer.speed * time / length))[0], 1)
                if winner > racer.number:
                    winner = racer.number
        else:
            if round((modf(racer.speed * time / length))[0], 1) <= to_finish:
                to_finish = round((modf(racer.speed * time / length))[0], 1)
                if winner > racer.number:
                    winner = racer.number

    return winner


print(race(add_racer(racers_num), race_time, track_length))
