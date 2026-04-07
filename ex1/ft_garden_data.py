class Plant:
    name: str
    height: int
    age: int

    def show(self) -> None:
        print("=== Garden Plant Registry ===")
        print(f"{self.name}: {self.height}cm, {self.age} days old")
