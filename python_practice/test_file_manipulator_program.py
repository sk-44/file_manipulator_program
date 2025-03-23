import os
import tempfile
import pytest
from python_practice import file_manipulator_program as fmp

@pytest.fixture
def temp_files():
    test_dir = tempfile.TemporaryDirectory()
    input_file = os.path.join(test_dir.name, "test.txt")
    output_file = os.path.join(test_dir.name, "output.txt")

    with open(input_file, "w", encoding="utf-8") as f:
        f.write("Hello World!!")
    
    yield input_file, output_file

    test_dir.cleanup()


def test_reverse_file(temp_files):
    input_file, output_file = temp_files
    fmp.reverse_file(input_file, output_file)

    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert content == "!!dlroW olleH"

def test_copy_file(temp_files):
    input_file, output_file = temp_files
    fmp.copy_file(input_file, output_file)

    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert content == "Hello World!!"

def test_duplicate_contents(temp_files):
    input_file, _ = temp_files
    fmp.duplicate_contents(input_file, 2)

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert content == "Hello World!!Hello World!!Hello World!!"

def test_replace_string(temp_files):
    input_file, _ = temp_files
    fmp.replace_string(input_file, "World", "Python")

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert content == "Hello Python!!"

def test_duplicate_contents_invalid_n(temp_files):
    input_file, _ = temp_files
    result = fmp.duplicate_contents(input_file, 0)

    assert result is False
