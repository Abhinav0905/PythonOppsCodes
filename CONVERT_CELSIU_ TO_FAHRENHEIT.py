# CONVERT CELSIUS TO FAHRENHEIT

x = int(input("Enter the temperature in Celsius: "))  # input the temperature in Celsius


class Temperature:
    def __init__(self, x:int):
        self.x = x

    def convert(self):
        far = (self.x *9/5) + 32
        return far


t = Temperature(x)

print("The temperature in Fahrenheit is: ", t.convert())  # print the temperature in Fahrenheit


