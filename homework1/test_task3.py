from task3 import if_statement, for_loop, while_loop

def test_positive():
    assert if_statement(1) == "Value is Positive"

def test_negative():
    assert if_statement(-1) == "Value is Negative"

def test_zero():
    assert if_statement(0) == "Value is Zero"

def test_for_loop():
    assert for_loop() == [2,3,5,7,11,13,17,19,23,29]

def test_while_loop():
    assert while_loop() == 5050