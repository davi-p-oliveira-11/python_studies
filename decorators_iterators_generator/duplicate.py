def duplicate(func):
  def envelope(*args, **kwargs):
    func(*args, **kwargs)
    func(*args, **kwargs)

    return envelope
  
@duplicate
def learn(technology):
  print(f"I'm learning {technology}")

learn("Python")