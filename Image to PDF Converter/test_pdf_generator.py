import os
from PyPDF2 import PdfReader
import pytest
import sys
sys.path.append('F:\\remote\\ImagetoPDFConverter')


from pdf_generator import generate_pdf


template_file = os.path.join("template_file.txt")


def test_generate_pdf_with_empty_template_file():
    image_dir1 = os.path.join('test_pngs/By Group')
    # Create an empty template file
    with open('empty_template.txt', 'w') as f:
        pass
    with pytest.raises(ZeroDivisionError):
        generate_pdf([image_dir1], 'empty_template.txt')


def test_generate_pdf_no_dirs():
    # Test that an error is raised if no image directories are provided
    with pytest.raises(TypeError):
        generate_pdf()


def test_generate_pdf_missing_dir():
    # Test that the function correctly handles missing image directories
    non_existent_dir = 'non_existent_dir'
    with pytest.raises(FileNotFoundError):
        generate_pdf([non_existent_dir], template_file)


def test_generate_pdf_save_location():
    # Test that the function saves the generated PDF file in the correct location
    image_dir = os.path.join('test_pngs/By Group')
    pdf_path = os.getcwd()
    generate_pdf([image_dir], template_file)
    assert os.path.exists(pdf_path)




def test_generate_pdf_expected_contents():
    # Test that the generated PDF file contains the expected images and text
    image_dir1 = os.path.join('test_pngs/By Group')
    image_dir2 = os.path.join('test_pngs/By Sorting Order')
    generate_pdf([image_dir1, image_dir2], template_file)
    with open(os.path.join('output.pdf'), 'rb') as f:
        pdf_reader = PdfReader(f)
        page = pdf_reader.pages[0]
        text = page.extract_text()
        assert len(pdf_reader.pages) == 6
       

    
