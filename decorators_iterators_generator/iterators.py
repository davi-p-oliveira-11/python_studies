class MyIterator:
   def __init__(self, numbers: list[int]):
      self.numbers = numbers
      self.counter = 0

   def __iter__(self):
      return self
   
   def __next__(self):
      try:
         number = self.numbers[self.counter]
         self.counter += 1
         return number * 2
      except IndexError:
         raise StopIteration


for i in MyIterator(numbers=[1, 2, 3]):
  print(i)