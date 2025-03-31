def my_decorator(function):
  def envelope():
    print("do something before execution")
    function()
    print("do after the execution")

  return envelope

@my_decorator
def hello_world():
  print("Hello World !")


hello_world()

