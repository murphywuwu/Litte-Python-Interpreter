# 运行 -> 指令 -> 栈
class Interpreter:
  def __init__(self):
    self.stack = []
    self.enviroment = {}

  def STORE_NAME(self, name):
    val = self.stack.pop()
    self.enviroment[name] = val

  def LOAD_NAM(self, name):
    val = self.enviroment[name]
    self.stack.append(val)

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

  def parse_argument(self, instruction, argument, what_to_execute):
    # 分类指令
    numbers = ['LOAD_VALUE']
    names = ['LOAD_NAME', 'STORE_NAME']

    # 根据传入指令所属类别，取出相应数据
    if instruction in numbers:
      argument = what_to_execute["numbers"][argument]
    elif instruction in names:
      argument = what_to_execute["names"][argument]
    
    return argument
    

  def run_code(self, what_to_execute):
    instructions = what_to_execute['instructions']
    numbers = what_to_execute['numbers']

    for each_step in instructions:
      instruction, argument = each_step
      argument = self.parse_argument(instruction, argument, what_to_execute)

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
