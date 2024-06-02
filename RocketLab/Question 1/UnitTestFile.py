#using unittest module for Unit Testing
import unittest


#importing the search_in_matrix function from the Source Code file having Matrix Class
from Source_code import search_in_matrix 


class UnitTestFile(unittest.TestCase):
    """
        Unit Test Class
    """
    

    def test_target_value_in_matrix(self):
        """
            Test function for the elements found in the matrix
        """
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ]

        #setting target values which are present in above matrix
        self.assertTrue(search_in_matrix(matrix, 3))

        self.assertTrue(search_in_matrix(matrix, 11))

        self.assertTrue(search_in_matrix(matrix, 60))

    def test_target_not_found(self):
        """
            Test case for element which are not present in the matrix
        """
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ]

        #setting target values which are not present in above matrix
        self.assertFalse(search_in_matrix(matrix, 114))

        self.assertFalse(search_in_matrix(matrix, 100))

    def test_search_matrix_empty(self):
        """
            Test case for matrix which are empty
        """
        #passing empty matrix
        self.assertFalse(search_in_matrix([], 1))
        
        self.assertFalse(search_in_matrix([[]], 1))

if __name__ == '__main__':
    unittest.main()
