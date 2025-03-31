import functools

def my_decorator(function):
  @functools.wraps(function)
  def envelope(*args, **kwargs):
    print("do something before execution")
    result = function(*args, **kwargs)
    print("do after the execution")
    return result

  return envelope

@my_decorator
def hello_world(name, other_arg):
  print(f"Hello World {name}!")
  return name.upper()


result = hello_world("John", 1000)
print(result)

