import unittest

from number_trick import *


class MyFirstTests(unittest.TestCase):

    def test_trick(self):
        self.assertEqual(trick(15,72), 15)



if __name__ == '__main__':
    unittest.main()

answer = int(input("Enter the answer between 10-49: "))
num = int(input("Enter a num between 50-99: "))
   

def trick(anwer,num):
    factor = 99 - answer
    num2  = factor + num
    num2 = num2 - 100 + 1
    answer2 = num - num2
    return answer2

print(trick(answer, num))

if __name__ == '__main__':
    main()
