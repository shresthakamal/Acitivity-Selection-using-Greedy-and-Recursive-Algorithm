import unittest
from greedy_selector import greedy_algo

class AlgoTestCase(unittest.TestCase):

	def test_greedyalgo_iterative(self):
	    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
	    f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

	    ob=greedy_algo()

	    self.assertEqual(ob.greedy_selector(s,f),[1,5,8,12])


	def test_greedyalgo_recursive(self):
		s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
		f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
		ob=greedy_algo()
		self.assertEqual(ob.recursive_activity_selector(s,f,-1,len(s)),[1,5,8,12])


if __name__=='__main__':
	unittest.main()





	