class Plant:
    name: str
    height: float
    days: int
    growth: float

    def grow(self) -> None:
        self.height += self.growth

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.days = 30
    rose.growth = 0.8
    count: float = 0
    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 8):
        print(f"Day {i}")
        count += rose.growth
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {count:.1f}cm")
