class Rectangle:
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height

    def __str__(self) -> str:
        return f'Rectangle with length {self.length} and height {self.height}'

    def __repr__(self) -> str:
        return f'Rectangle({self.length}, {self.height})'


class Cuboid (Rectangle):
    def __init__(self, length, height, width):
        super().__init__(length, height)
        self.width = width

    def area(self):
        return 2*super().area() + 2*self.width*self.height + 2*self.width*self.length

    def volume(self):
        return super().area() * self.height

    def __str__(self) -> str:
        return f'Cuboid with width {self.width}, length {self.length} and height {self.height}'

    def __repr__(self) -> str:
        return f'Cuboid({self.width}, {self.length}, {self.height})'


class InvalidData(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

    def __repr__(self):
        return f'InvalidData({self.message})'


def is_float(element) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False


def getdata(line):
    data = line.split(" ")

    if data[0] == '1':
        if len(data) != 3:
            raise InvalidData(
                "Invalid data, expected 3 arguments but got "+str(len(data)))

        if False in [is_float(d) for d in data[1:]]:
            raise InvalidData("Invalid data, expected numbers")

        if False in [float(d) > 0 for d in data[1:]]:
            raise InvalidData("Invalid data, expected positive numbers")

        return Rectangle(float(data[1]), float(data[2]))

    elif data[0] == '2':

        if len(data) != 4:
            raise InvalidData(
                "Invalid data,expected 4 arguments but got "+str(len(data)-1))

        if False in [is_float(d) for d in data[1:]]:
            raise InvalidData("Invalid data, expected numbers")

        if False in [float(d) > 0 for d in data[1:]]:
            raise InvalidData("Invalid data, expected positive numbers")

        return Cuboid(float(data[1]), float(data[2]), float(data[3]))
    else:
        raise InvalidData(
            "Invalid data, expected 1 or 2 but got "+str(data[0]))


def main():
    with open('zad4.txt', 'r') as f:
        data = f.readlines()
        data = reversed(data)

    data = [x.strip() for x in data]

    for line in data:
        try:
            obj = getdata(line)
            print(obj)
            print(f'Area = {obj.area()}')
            if isinstance(obj, Cuboid):
                print(f'Volume = {obj.volume()}')
        except InvalidData as e:
            print(e)


if __name__ == '__main__':
    main()
