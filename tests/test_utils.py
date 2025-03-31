import os
import sys
import shutil
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import convert_heic_to_jpg, create_output_folder

# Sample test HEIC file path
TEST_IMAGE = "example_images/test.heic"

@pytest.fixture(scope="module")
def setup_output_folder():
    folder = create_output_folder("test_output")
    yield folder
    shutil.rmtree(folder)  # Clean up after test

def test_output_folder_created(setup_output_folder):
    assert os.path.exists(setup_output_folder)

def test_convert_valid_heic(setup_output_folder):
    if not os.path.exists(TEST_IMAGE):
        pytest.skip("No test .heic image found.")
    output_path, success = convert_heic_to_jpg(TEST_IMAGE, setup_output_folder)
    assert success is True
    assert os.path.exists(output_path)