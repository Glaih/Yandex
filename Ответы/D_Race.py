from math import modf


class Carriage:
    def __init__(self, number, speed):
        self.number = number
        self.speed = speed

    def __str__(self):
        return f"{self.number} - {self.speed}"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.number}"


class Car(Carriage):
    def __init__(self, number, speed, fuel):
        super(Car, self).__init__(speed, number)
        self.fuel = fuel
        self.speed = speed
        self.number = number

    def ignite(self):
        if self.fuel == 98:
            return __class__(self.number, self.speed, self.fuel)
        else:
            self.speed = self.speed - (self.speed / 100 * 10) if self.fuel == 95 else self.speed - (self.speed / 100 * 20)
            return __class__(self.number, self.speed, self.fuel)


class Bike(Car):
    def ignite(self):
        if self.fuel == 98:
            return __class__(self.number, self.speed, self.fuel)
        else:
            self.speed = self.speed - (self.speed / 100 * 20) if self.fuel == 95 else self.speed - (self.speed / 100 * 40)
            return __class__(self.number, self.speed, self.fuel)


class Race:
    def __init__(self, racers_num, track_length, race_time):
        self.racers = racers_num
        self.length = track_length
        self.time = race_time

    def create_racers(self):
        racers = []
        for i in range(self.racers):
            data = list(map(int, input().split(' ')))
            v_type = data.pop(1)
            if v_type == 3:
                racers.append(Carriage(*data))
            elif v_type == 1:
                racers.append(Car(*data).ignite())
            elif v_type == 2:
                racers.append(Bike(*data).ignite())
        return racers

    def start(self):
        racers = self.create_racers()
        to_finish = 1
        winner = 1
        for racer in racers:
            if winner < racer.number:
                winner = racer.number
        for racer in racers:
            if round((modf(racer.speed * self.time / self.length))[0], 3) > 0.5:
                if 1 - round((modf(racer.speed * self.time / self.length))[0], 3) <= to_finish:
                    to_finish = 1 - round((modf(racer.speed * self.time / self.length))[0], 1)
                    if winner > racer.number:
                        winner = racer.number
            else:
                if round((modf(racer.speed * self.time / self.length))[0], 1) <= to_finish:
                    to_finish = round((modf(racer.speed * self.time / self.length))[0], 1)
                    if winner > racer.number:
                        winner = racer.number
        return winner


racers_num, track_length, race_time = map(int, input().split(' '))
race = Race(racers_num, track_length, race_time).start()
print(race)
