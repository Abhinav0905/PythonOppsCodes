# swap two variables

x = int(input("Enter the first number: "))  # input the first number
y = int(input("Enter the second number: "))  # input the second number


class Swap:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

    def swap(self):
        self.x, self.y = self.y, self.x
        return self.x, self.y


a = Swap(x, y)

print(f"The first number is: {x} and the second number is: {y}")
print(f"the Swapped number is {a.swap([0])} and {a.swap([1])}")  # print the swapped numbers


