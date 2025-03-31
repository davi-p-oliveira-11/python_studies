def message(name):
  print("Executing message")
  return f"Hi {name}"


def long_message(name):
  print("executing long message")
  return f"Hello how are you doing ? {name}"


def execute(function):
  print("executing execute")
  return function("John")


execute(message)