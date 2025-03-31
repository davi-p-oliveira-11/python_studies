def calculate(operation):
  def sum(a, b):
    return a + b
  
  def sub(a, b):
    return a - b
  
  def mul(a, b):
    return a * b
  
  def div(a, b):
    return a / b
  
  match operation:
    case "+":
       return sum
    case "-":
       return sub
    case "*":
       return mul
    case "/":
       return div
    

op = calculate("+")
print(op(2,2))
op = calculate("-")
print(op(2,2))
op = calculate("*")
print(op(2,2))
op = calculate("/")
print(op(2,2))


 
  