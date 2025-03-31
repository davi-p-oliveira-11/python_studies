def calculate(operation):
  def sum(a, b):
    return a + b
  
  def subtract(a, b):
    return a - b
  
  if operation == "+":
    return sum
  else:
    return subtract
  
result = calculate("+")(1, 3)
print(result)