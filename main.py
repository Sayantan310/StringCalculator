import re
import pytest

def add(numbers: str) -> int:
    if not numbers:
        return 0

    # Checking for custom delimiter
    delimiter = ","
    if numbers.startswith("//"):
        delimiter_part, numbers = numbers.split("\n", 1)
        delimiter = re.escape(delimiter_part[2:])

    # Replace newlines with delimiter for uniformity
    numbers = numbers.replace("\n", delimiter)

    # Split numbers by the delimiter
    number_list = re.split(delimiter, numbers)

    # Convert to integers and check for negatives
    negatives = [int(n) for n in number_list if n.startswith("-")]
    if negatives:
        raise ValueError(f"negative numbers not allowed {', '.join(map(str, negatives))}")

    return sum(int(n) for n in number_list if n)

# Test cases for TDD testing
def test_add_empty_string():
    assert add("") == 0

def test_add_single_number():
    assert add("1") == 1

def test_add_two_numbers():
    assert add("1,2") == 3

def test_add_multiple_numbers():
    assert add("1,2,3,4") == 10

def test_add_with_newlines():
    assert add("1\n2,3") == 6

def test_add_with_custom_delimiter():
    assert add("//;\n1;2") == 3
    assert add("//|\n1|2|3") == 6

def test_add_negative_numbers():
    with pytest.raises(ValueError, match="negative numbers not allowed -1"):
        add("-1,2,3")
    with pytest.raises(ValueError, match="negative numbers not allowed -1, -2"):
        add("-1,-2,3")
def finishingmessage():
    print("TEST CASES RUNNING COMPLETED!!!!!!!!!!!!!")
def test_cases_run_started_message():
    print("TEST CASES RUNNING STARTED!!!!!!!!!!!!!")

def test_add_ignore_empty_numbers():
    assert add("1,,2") == 3

# Running the test cases
test_cases_run_started_message()
test_add_empty_string()
test_add_single_number()
test_add_two_numbers()
test_add_multiple_numbers()
test_add_with_newlines()
test_add_with_custom_delimiter()
test_add_negative_numbers()
finishingmessage()