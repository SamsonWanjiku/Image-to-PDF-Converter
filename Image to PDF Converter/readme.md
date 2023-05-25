Image to PDF Converter
This script converts a directory of PNG images into PDF files using a provided template. It utilizes the reportlab, PyPDF2, and PIL libraries to generate the PDFs.
Requirements
•	Python 3.x
•	reportlab library (pip install reportlab)
•	PyPDF2 library (pip install PyPDF2)
•	PIL library (pip install Pillow)
Usage
1.	Make sure you have the required libraries installed by running the commands mentioned in the "Requirements" section.
2.	Place the script in the same directory as the images you want to convert or specify the image directory using the image_dir variable.
3.	Create a text file named template.txt and provide the desired template content. The script will replace the {image} placeholder in the template with the corresponding image for each PDF.
4.	Run the script using python pdf_generator.py in your terminal or IDE.
How It Works
1.	The script retrieves a list of PNG image files in the specified image directory.
2.	It reads the template text from the template.txt file.
3.	For each image file, it opens the image, retrieves its dimensions, and creates a new PDF.
4.	The template text is added to the PDF using the drawString method from the canvas object.
5.	The image is then added to the PDF using the drawImage method.
6.	The resulting PDF is saved with a unique file name in the same directory as the images.
7.	The temporary PDF file created during the process is removed.
Note: Make sure to customize the image_dir and template_file variables in the script according to your specific directory structure and file names.

