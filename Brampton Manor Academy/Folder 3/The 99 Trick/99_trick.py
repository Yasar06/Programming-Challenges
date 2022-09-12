import unittest

from 99_trick import *


class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')

    def test_custom_num_list(self):
        self.assertEqual(len(create_list(10)), 10)

if __name__ == '__main__':
    unittest.main()

answer = int(input("Enter the answer between 10-49: "))
num = int(input("Enter a num between 50-99: "))
   

def trick(anwer,num):
    factor = 99 - answer
    num2  = factor + num
    digit = num[0]
    num - digit * 100 + digit
    answer = num - num2
    return answer


print(trick(answer, num))
