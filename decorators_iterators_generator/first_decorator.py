def my_decorator(function):
  def envelope():
    print("do something before execution")
    function()
    print("do after the execution")

  return envelope


def hello_world():
  print("Hello World !")


hello_world = my_decorator(hello_world)
hello_world()

