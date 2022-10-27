import unittest, os
from read import read


class TestRead(unittest.TestCase):
  def test_read_file(self):
    content = 'func content() {}'
    file_name = 'testfile.yh'
    file = open(file_name, 'w')
    file.write(content)
    file.close()
    
    result = read(file_name)
    self.assertEqual(content, result)
    
    os.remove(file_name)
    
