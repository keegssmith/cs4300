import os
from task6 import count_words

# generate test functions based on filenames and test count_words function based on file and its expected word total
def generate_test_function(filename, total_words):
    test_name = f"test_{os.path.splitext(filename)[0]}" # change the name of the test function to represent "test_[filename]"
    
    def test_func():
        assert count_words(filename) == total_words
    
    test_func.__name__ = test_name  # dynamically change fxn name
    return test_func

# test text file and it's expected word total
test_file = generate_test_function("task6_read_me.txt", 104)