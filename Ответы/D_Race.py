from math import modf
from collections import defaultdict


class Carriage:
    def __init__(self, number, speed):
        self.number = number
        self.speed = speed

    def __repr__(self):
        return f"{self.__class__.__name__} - {self.number}"


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


def race(num, time, length):
    to_finish_dict = defaultdict(list)
    closest_to_finish = 1
    for _ in range(num):
        data = list(map(int, input().split(' ')))
        vehicle_type = data.pop(1)
        if vehicle_type == 3:
            racer = Carriage(*data)
        elif vehicle_type == 1:
            racer = Car(*data)
        elif vehicle_type == 2:
            racer = Bike(*data)

        current_circle = modf(racer.speed * time / length)

        if round(current_circle[0], 3) > 0.5:
            to_finish = round(1 - current_circle[0], 1)
        else:
            to_finish = round(current_circle[0], 1)

        to_finish_dict[to_finish].append(racer.number)

        if to_finish >= closest_to_finish:
            continue

        closest_to_finish = to_finish

    return min(to_finish_dict[closest_to_finish])


print(race(racers_num, race_time, track_length))
