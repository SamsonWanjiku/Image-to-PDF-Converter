from io import BytesIO
import os
import sys
import subprocess
from typing import List, Dict
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from PyPDF2 import PdfWriter, PdfReader
import datetime

def generate_pdf(image_dirs: List[str], template_file: str) -> None:
    with open(template_file, "r") as f:
        template = f.read()
    
    image_files: List[str] = []
    
    for image_dir in image_dirs:
        image_files += [
            os.path.join(image_dir,
            f) for f in os.listdir(image_dir) if f.endswith('.png')
        ]
    output_pdf = PdfWriter()
    image_width, image_height = (5440, 2824)
    margin = 3 * inch
    page_width = 6 * image_width + 7 * margin
    page_height = 3824 
    
    groups: Dict[str, Dict[str, List[str]]] = {}
    for image_file in image_files: 
        components = image_file.split("/")        
        filename = components[-1]
        if "By Group" in filename:
            filename_parts = filename.split(";")
            cv_ls_group = filename_parts[0]
            if len(filename_parts) >= 2:
                sorting_group = filename_parts[1].split(".")[0]
            else:
                sorting_group = filename_parts[0].split(".")[0]
        else:
            filename_parts = filename.split("\\")
            if len(filename_parts) >= 3:
                cv_ls_group = filename_parts[2].split(';')[-1]
                sorting_group = filename_parts[2].split(';')[0]
            else:
                cv_ls_group = filename_parts[1].split(";")[-1]
                sorting_group = filename_parts[1]
        if cv_ls_group not in groups:
            groups[cv_ls_group] = {}
        if sorting_group not in groups[cv_ls_group]:
            groups[cv_ls_group][sorting_group] = []
        groups[cv_ls_group][sorting_group].append(image_file)
    
    c = canvas.Canvas(BytesIO(),
                      pagesize=(page_width, page_height))
    x_offset = 35
    y_offset = page_height - margin - image_height
    
    for cv_ls_group in sorted(groups.keys()):
        for sorting_group in sorted(groups[cv_ls_group].keys()):
            for image_file in groups[cv_ls_group][sorting_group]:
                # Add header name for each image
                if 'By Group' in cv_ls_group:
                    header_name = template.strip().replace(
                        "{GroupName}",
                        cv_ls_group.split('By Group\\')[-1])
                else:
                    header_name = template.strip().replace(
                        "{GroupName}",
                        cv_ls_group.split(".")[0].replace("0", " "))
            
                padding = 40
                font_size = int((image_width - 2 * padding) * 0.75 / len(header_name))
                c.setFont('Helvetica', font_size)
                text_width = c.stringWidth(header_name, 'Helvetica', font_size)
                x_text = x_offset + (image_width - text_width) / 2
                c.drawString(
                    x_text, y_offset + image_height + 10 + padding, header_name
                    )


                c.rect(x_offset, y_offset, image_width, image_height)
                c.drawImage(image_file, x_offset + 5, y_offset + 5,
                            width=image_width - 10, height=image_height - 10)
                x_offset += image_width + 10
                if x_offset + image_width > page_width:
                    # Move to next row if current row is full
                    x_offset = 35
                    y_offset -= image_height + 50
                    
                    if y_offset < 0:
                        c.setFont('Helvetica', 60)
                        footer_text = "Generated on {} at {}".format(
                            datetime.datetime.now().strftime("%Y-%m-%d"),
                            datetime.datetime.now().strftime("%H:%M:%S"))
                        c.drawCentredString(page_width / 2.0, inch / 2.0, footer_text)
                        c.showPage()
                        output_pdf.add_page(
                            PdfReader(BytesIO(c.getpdfdata())).pages[0])
                        c = canvas.Canvas(BytesIO(),
                                          pagesize=(page_width, page_height))
                        x_offset = 35
                        y_offset = page_height - margin - image_height
                        
    
    with open("output.pdf", "wb") as f:
        output_pdf.write(f)


    # open the pdf generated
    platform = sys.platform
    #: windows
    if platform == "win32":
        subprocess.Popen(['output.pdf'], shell=True)
    #: linux
    elif platform == "linux" or sys.platform == "linux2":
        subprocess.Popen(['xdg-open','output.pdf'])
    #: macOS
    elif platform == "darwin":
        subprocess.Popen(['open','output.pdf'])
