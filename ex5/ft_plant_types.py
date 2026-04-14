class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name: str = name
        self._height: float = height
        self._days: int = days

    def grow(self, growth: float) -> None:
        self._height += growth

    def age(self) -> None:
        self._days += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._days} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 days: int, color: str) -> None:
        super().__init__(name, height, days)
        self._color = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 days: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, days)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("=== Tree")
    oak = Tree("Oak", 15.0, 10, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow(2.1)
        tomato.age()
    tomato.show()
