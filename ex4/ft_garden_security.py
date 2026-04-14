class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name: str = name
        self._height: float = height
        self._days: int = days

    def grow(self, growth: float) -> None:
        self._height += growth

    def age(self) -> None:
        self._days += 1

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        else:
            self._height = value
            print(f"Height updated: {self._height:g}cm")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        else:
            self._days = value
            print(f"Age updated: {self._days}")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def show(self) -> None:
        print(f"{self._name}: {self._height:g}cm, {self._days} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print("", end="\n")
    rose.set_height(25.0)
    rose.set_age(30)
    print("", end="\n")
    rose.set_height(-5.0)
    rose.set_age(-1)
    print("", end="\n")
    print("Current state: ", end="")
    rose.show()
