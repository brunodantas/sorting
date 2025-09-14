"""
Additional pytest-style tests for counting sort implementation
"""
import random
from countingsort import countingsort


class TestCountingSortPytest:
    """Pytest-style tests for countingsort function"""
    
    def test_empty_list(self):
        assert countingsort([]) == []
    
    def test_single_element(self):
        assert countingsort([42]) == [42]
    
    def test_basic_sorting(self):
        assert countingsort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    
    def test_already_sorted(self):
        assert countingsort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    def test_reverse_sorted(self):
        assert countingsort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
    def test_duplicates(self):
        assert countingsort([2, 2, 2, 2]) == [2, 2, 2, 2]
    
    def test_with_zero(self):
        assert countingsort([0, 3, 1, 0, 2]) == [0, 0, 1, 2, 3]

    def test_parametrized_cases(self):
        """Test multiple cases in a single test"""
        test_cases = [
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1], [1, 2, 3]),
            ([1, 3, 2], [1, 2, 3]),
            ([5, 1, 3, 9, 2], [1, 2, 3, 5, 9]),
            ([0, 0, 1, 1], [0, 0, 1, 1]),
        ]
        
        for input_list, expected in test_cases:
            assert countingsort(input_list) == expected
    
    def test_random_data_matches_builtin_sort(self):
        """Property test: countingsort should match built-in sort"""
        random.seed(42)
        for _ in range(10):  # Test multiple random cases
            # Generate random list of non-negative integers
            size = random.randint(1, 100)
            max_val = random.randint(0, 50)
            input_list = [random.randint(0, max_val) for _ in range(size)]
            
            expected = sorted(input_list)
            result = countingsort(input_list)
            assert result == expected
    
    def test_large_range_small_list(self):
        """Test efficiency concern: large range with few elements"""
        # This creates a large count array but should still work
        input_list = [0, 1000, 500]
        expected = [0, 500, 1000]
        assert countingsort(input_list) == expected
    
    def test_immutability(self):
        """Test that input list is not modified"""
        original = [3, 1, 4, 1, 5]
        input_copy = original.copy()
        result = countingsort(input_copy)
        assert input_copy == original  # Original should be unchanged
        assert result == [1, 1, 3, 4, 5]  # Result should be sorted
