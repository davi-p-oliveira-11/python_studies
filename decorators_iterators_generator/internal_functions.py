def main():
  print("Executing the main function")

  def internal_function():
    print("Executing internal function")

  def function_2():
    print("executing function 2")

    internal_function()
    function_2()


main()