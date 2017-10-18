# Cognitev-Tasks
Python scripts, part of interviewing tasks at: http://www.cognitev.com/

**Task 1**
**Description:**

Write a python script (solution.py) that takes a list of file extensions and prints all the files from the
passed directory or current directory matching the extensions given.
The following extensions should be supported:
1. `c` should find and print all `.c` and `.h` file names
2. `py` should find and print all `.py` and `.pyc` file names
3. `pl` should find and print all `.pl` and `.pm` file names

```
Usage:
python solution.py c,py,pl /path/to/dir
```
```
Output:
py: ad.py, ad.pyc, campaign.py, campaign.pyc
pl: service.pl, service.pm
```
Bonus: You should be able to read extensions from configuration file.



**Task 2**
**Description:**

Please, optimize the function below:
```
def fib(n):
  if n <= 2:
    return 1
  else:
    return fib(n-1) + fib(n-2)
```
**Task 3**
**Description:**

Provided test file test_stack.py. Write the module required to make the test pass:

```
import unittest
from lib import mystack

class TestMyStack(unittest.TestCase):
	def setUp(self):
		mystack.add_item(10);
 		mystack.add_item(20);
 		mystack.add_item(22, 33);
 	def test_flow(self):
 		self.assertEqual(mystack.pop_item(), 33)
 		self.assertEqual(mystack.pop_item(), 22)
 		self.assertEqual(mystack.count_items(), 2)
 		while mystack.pop_item(): pass
		
 		self.assertEqual(mystack.count_items(), 0)
```
