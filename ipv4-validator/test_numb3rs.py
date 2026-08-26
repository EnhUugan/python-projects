from numb3rs import validate

def test_true_cases():
    assert validate("1.2.3.4") == True
    assert validate("122.1.1.0") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_false_cases():
    assert validate("555.1.1.1") == False
    assert validate("1.1.1.1111") == False
    assert validate("122.33.001.1") == False
    assert validate("poop") == False
    assert validate("1.2.3") == False
    assert validate("1.1.1.1.1") == False
    assert validate("") == False
