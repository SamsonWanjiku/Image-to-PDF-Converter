# PDF Generation Script

This script generates a PDF document by combining multiple images into a grid layout. It uses the `reportlab` library to create the PDF and the `PyPDF2` library to merge the pages into a final PDF document.

## Prerequisites

Before running the script, make sure you have the following components set up:

1. Python: Make sure you have Python installed on your system. You can download it from the official Python website: https://www.python.org/downloads/

2. Required Libraries: Install the necessary libraries by running the following command:

   ```bash
   pip install reportlab PyPDF2
   ```

## Usage

To use the script, follow these steps:

1. Save the script as a Python file, e.g., `pdf_generator.py`, in a directory of your choice.

2. Prepare the following inputs:

   - `image_dirs` (List[str]): A list of directories containing the images you want to include in the PDF. Each directory should contain PNG images.
   - `template_file` (str): The path to a text file that contains the template for the header of each image. The template should include the placeholder `{GroupName}` that will be replaced with the corresponding group name.

3. Open a terminal or command prompt and navigate to the directory where the script is located.

4. Run the following command to generate the PDF:

   ```bash
   python pdf_generator.py
   ```

   The script will generate an `output.pdf` file in the same directory, which contains the combined images in a grid layout.

5. The generated PDF will be automatically opened with the default PDF viewer on your operating system. If the PDF viewer does not open automatically, you can manually open the `output.pdf` file.

## Notes

- The script assumes that the images are in PNG format. If your images are in a different format, you may need to modify the script accordingly.

- The script creates a grid layout for the images, arranging them in rows and columns. The number of images in each row depends on the image width and the page width. If the row is full, the script moves to the next row. If the page is full, a new page is added to the PDF.

- The script supports different operating systems (Windows, Linux, macOS) for opening the generated PDF. It uses subprocess to open the PDF with the default PDF viewer. If you encounter issues with opening the PDF on your system, you may need to modify the subprocess command accordingly.

- The generated PDF includes a footer with the date and time of generation.
