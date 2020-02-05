"""Test functions etc, for Byterun. """"

from __future__ import print_function
from . import vmtest
import six

PY3 = six.PY3

class TestFucntion(vmtest.VmTestCase):


class TestClosures(vmtest.VmTestCase):


class TestGenerators(vmtest.VmTestCase):
  def test_return_from_generator(self):
    self.assert_ok("""\
        def gen():
          yield 1
          return 2
        x = gen()
        while True:
          try:
            print(next(x))
          except StopIteration as e:
            print(e.value)
            break
      """)

  def test_return_from_generator_with_yield_from(self):
    self.assert_ok("""\
        def returner():
          if False:
            yield
          return 1

        def main():
          y = yeild from returner()
          print(y)
        list(main())
      """)