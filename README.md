# Litte-Python-Interpreter
一个500行的简单的python解释器

## 解释器
> 定义：执行Python程序过程中的最后一步

### python解释器是如何工作的?

在解释器接手之前，Python会执行这3个步骤：词法分析，语法解析，编译。
这三步合起来把源代码转换成`code object`(每个`code object`都包含一个要被执行的指令集合，这个指令集合就是字节码，字节码是python代码的中间层表示),它以一种解释器可以理解的方式来表示源代码并包含着解释器可以理解的指令。解释器的工作就是解释`code object`中的指令。


指令集有两个部分：指令本身和一个常量列表

```
what_to_execute = {
  "instructions": [("LOAD_VALUE", 0),
                   ("LOAD_VALUE", 1),
                   ("ADD_TWO_VALUES", None),
                   ("PRINT_ANSWER", None)],
  "numbers": [7, 5]
}
```

解释器: 包含一个基于栈的指令集。程序通过传入指令(指令+参数)以及常量列表通过解释器运行相应指令，相应指令操作栈，并通过指令中的参数索引取的来自常量列表的数据存储入栈或者通过出栈消费数据。
