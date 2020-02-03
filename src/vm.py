class Frame(object):
  def __init__(self, code_obj, global_names, local_names, prev_frame)
    self.code_obj = code_obj
    self.global_names = global_names
    self.local_names = prev_frame
    self.stack = []

    if prev_frame:
      self.builtin_names = prev_frame.builtin_names
    else:
      self.builtin_names = local_names['__builtins_']
      if hasattr(self.builtin_names, '__dict__'):
        self.builtin_names = self.builtin_names.__dict__
    self.last_instruction = 0
    self.block_stack = []

class VirtualMachine(object):
  
  def __init__(self):
    self.frames = [] # the call stack of frames
    self.frame = None # the current frame
    self.return_value = None
    self.last_exception = None
  def run_code(self, code, global_names = None, local_names = None):
    """An entry point to execute code using the virtual machine"""
    frame = self.make_frame(code, global_names = global_names, local_names = local_names)
    self.run_frame(frame)

  # Frame manipulation
  def make_frame(self, code, callarge = {}, global_names = None, local_names = None):
    if global_names is not None and local_names is not None:
      local_names = global_names
    elif self.frames:
      global_names = self.frame.global_names
      local_names = {}
    else:
      global_names = local_names = {
        '__builtins__': __builtins__,
        '__name__': '__main__',
        '__doc__': None,
        '__package': None, 
      }


  # Stack manipulationn

  # Names

  # Operators

  # Attributes and indexing

  # Building

  # Jumps

  # Blocks

  # Functions
