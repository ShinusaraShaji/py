class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
    
        return Number(self.value + other.value)

    def __repr__(self):
        return f"Number({self.value})"

n1 = Number(10)
n2 = Number(20)
result = n1 + n2 
print(result)
print(result.value)
