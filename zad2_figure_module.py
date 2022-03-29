# źle __repr__ i __str__
class Figure:
    def __init__(self, color="#FF0000", is_filled=False):
        self.color = color
        self.is_filled = is_filled

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"Figure({self.color}, {self.is_filled})"


class Circle(Figure):
    def __init__(self, color, isfilled, radius) -> None:
        super().__init__(color, isfilled)
        self.radius = radius

    @property
    def area(self) -> float:
        return 3.14 * self.radius ** 2

    @property
    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius

    @property
    def diameter(self) -> float:
        return 2 * self.radius

    @property
    def radius(self) -> float:
        return self._radius

    @property.setter
    def radius(self, r) -> float:
        if r < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = r

    def __dict__(self) -> dict:
        return {"Radius": self.radius,
                "Diameeter": self.diameter,
                "Perimeter": self.perimeter,
                "Area": self.area}

    def __str__(self) -> str:

        return super().__str__()

    def __repr__(self) -> str:

        return super().__repr__()


class Rectangle (Figure):
    def __init__(self, color, isfilled, width, height) -> None:
        super().__init__(color, isfilled)
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    @property
    def width(self) -> float:
        return self._width

    @property.setter
    def width(self, w) -> float:
        if w < 0:
            raise ValueError("Width cannot be negative")
        self._width = w

    @property
    def height(self) -> float:
        return self._height

    @property.setter
    def height(self, h) -> float:
        if h < 0:
            raise ValueError("Height cannot be negative")
        self._height = h

    @property
    def diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def __dict__(self) -> dict:
        return {"Width": self.width,
                "Height": self.height,
                "Perimeter": self.perimeter,
                "Area": self.area,
                "Diagonal": self.diagonal}

    def __str__(self) -> str:

        return super().__str__()

    def __repr__(self) -> str:

        return super().__repr__()
