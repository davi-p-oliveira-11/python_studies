def say_hi(name):
  return f"Hi {name}"

def encourage_learn(name):
  return f"Hi {name}, let's learn python together"

def message_to_john(function_message):
  return function_message("John")

message_to_john(say_hi)
message_to_john(encourage_learn)