# Calculator class

class Calculator:
    def __init__(self, input1, input2):
       self.input1 = input1
       self.input2 = input2

    def adder(self):
        return self.input1 + self.input2
    def subtractor(self):
        return self.input1 - self.input2
    def multiplier(self):
        return self.input1 * self.input2
    def divider(self):
        return self.input1 / self.input2
    def clear(self):
        self.input1 = 0
        self.input2 = 0

input1 = float(input("Enter input1: "))
input2 = float(input("Enter input2: "))
calc = Calculator(input1,input2)

print("Input1: ", calc.input1)
print("Input2: ", calc.input2)
print("Addition: ", calc.adder())
print("Subtraction: ", calc.subtractor())
print("Multiplication: ", calc.multiplier())
print("Division: ", calc.divider())
print("Clearing...")
calc.clear()
print("Input1: ", calc.input1)
print("Input2: ", calc.input2)
