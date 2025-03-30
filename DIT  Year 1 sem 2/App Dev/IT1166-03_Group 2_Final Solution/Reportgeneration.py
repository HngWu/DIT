from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import matplotlib.pyplot as plt
import numpy as np

def generate_pdf_file():
    # Create a buffer to hold the generated PDF
    buffer = BytesIO()
    
    # Create a matplotlib figure and axes
    fig = plt.figure(figsize=(5,   4), dpi=100)
    ax = fig.add_subplot(111)
    
    # Create a pie chart
    labels = ['A', 'B', 'C', 'D']
    sizes = [15,   30,   45,   10]
    explode = (0,   0.1,   0,   0)
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    
    # Convert the matplotlib figure to a PNG image
    imgdata = BytesIO()
    fig.savefig(imgdata, format='png')
    imgdata.seek(0)  # rewind the data
    
    # Create a PDF canvas
    p = canvas.Canvas(buffer)
    
    # Add paragraphs above the pie chart
    p.setFont("Helvetica",  12)
    p.drawString(50,  720, "This is a paragraph about the pie chart.")
    p.drawString(50,  700, "Another paragraph explaining the data.")
    
    # Add the image to the PDF
    img = ImageReader(imgdata)
    p.drawImage(img,   50,   600, width=200, height=200)
    
    # Add paragraphs below the pie chart
    p.drawString(50,  500, "More information about the data.")
    p.drawString(50,  480, "Final thoughts on the pie chart.")
    
    # Finalize the PDF
    p.showPage()
    p.save()
    
    # Move to the beginning of the StringIO buffer
    buffer.seek(0)
    return buffer