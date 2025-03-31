def my_decorator(function):
  def envelope(*args, **kwargs):
    print("do something before execution")
    function(*args, **kwargs)
    print("do after the execution")

  return envelope

@my_decorator
def hello_world(name):
  print(f"Hello World {name}!")


hello_world()

