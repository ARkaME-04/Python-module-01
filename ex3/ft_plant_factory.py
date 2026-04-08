class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days

    def grow(self, growth: float) -> None:
        self.height += growth

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    garden = [Plant("Rose", 25, 30),
              Plant("Oak", 200, 365),
              Plant("Cactus", 5, 90),
              Plant("Sunflower", 80, 45),
              Plant("Fern", 15, 120),]
    for i in garden:
        print("Created: ", end="")
        i.show()
