# 运行 -> 指令 -> 栈
class Interpreter:
  def __init__(self):
    self.stack = []
  def LOAD_VALUE(self, number):
    self.stack.append(number)
  
  def ADD_TWO_VALUES(self):
    first_num = self.stack.pop()
    second_num = self.stack.pop()
    total = first_num + second_num
    self.stack.append(total)
  
  def PRINT_VALUES(self):
    answer = self.stack.pop()
    print(answer)
  
  def run_code(self, what_to_execute):
    instructions = what_to_execute['instructions']
    numbers = what_to_execute['numbers']

    for each_step in instructions:
      instruction, argument = each_step

      if instruction == 'LOAD_VALUE':
        number = numbers[argument]
        self.LOAD_VALUE(number)
      elif instruction == 'ADD_TWO_VALUES':
        self.ADD_TWO_VALUES()
      elif instruction == 'PRINT_VALUES':
        self.PRINT_VALUES()

what_to_execute = {
  "instructions": [("LOAD_VALUE", 0),
                   ("LOAD_VALUE", 1),
                   ("ADD_TWO_VALUES", None),
                   ("PRINT_VALUES", None)],
  "numbers": [7, 5]
}

interpreter = Interpreter()
interpreter.run_code(what_to_execute)
