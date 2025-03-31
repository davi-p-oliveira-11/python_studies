def father():
  print("Writing from father() function.")

  def son_1():
    print("Writing from son_1() function")

  def son_2():
    print("Writing from son_2() function")

  son_2()
  son_1()
  

father()