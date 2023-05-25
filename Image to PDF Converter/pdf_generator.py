import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
from reportlab.lib.pagesizes import A4

# Retrieve the saved images
image_dir = 'F:/path'
image_files = [f for f in os.listdir(image_dir) if f.endswith('.png')]

# Use a template file to generate the PDFs
template_file = 'template.txt'

with open(template_file, 'r') as f:
    template_text = f.read()

# modify the template for each PDF
for image_file in image_files:
    # open the image file and get its dimensions
    image_path = os.path.join(image_dir, image_file)
    with Image.open(image_path) as img:
        img_width, img_height = img.size

    # create a new PDF and add the template
    output_pdf = PdfWriter()
    print(os.getcwd())
    c = canvas.Canvas("batch_plots.pdf", pagesize=A4)
    c.drawString(inch, inch, template_text)
    c.drawImage(image_path, inch, 2*inch, width=img_width, height=img_height)
    c.save
    print(os.getcwd())
    image_pdf = PdfReader(open("temp.pdf", "rb"))
    output_pdf.addPage(image_pdf.getPage(0))

    # save the PDF with a unique file name
    output_file = os.path.join(image_dir, f"{image_file[:-4]}.pdf")
    with open(output_file, 'wb') as f:
        output_pdf.write(f)

    os.remove("temp.pdf")
