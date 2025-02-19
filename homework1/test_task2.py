from task2 import task_int, task_float, task_string, task_bool

def test_int():
    assert isinstance(task_int(), int) == True

def test_float():
    assert isinstance(task_float(), float) == True

def test_str():
    assert isinstance(task_string(), str) == True

def test_bool():
    assert isinstance(task_bool(), bool) == True
