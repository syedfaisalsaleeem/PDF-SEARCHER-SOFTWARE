import io
import pdfplumber
import PyPDF2
import pytesseract
from tkinter import *
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image

from pdfviewer.config import *
from pdfviewer.hoverbutton import HoverButton
from pdfviewer.helpbox import HelpBox
from pdfviewer.menubox import MenuBox
from pdfviewer.display_canvas import DisplayCanvas


import os


ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
BACKGROUND_COLOR = '#303030'
HIGHLIGHT_COLOR = '#558de8'
from pdfviewer import PDFViewer


def main():
    root = Tk()
    PDFViewer()
    root.mainloop()


if __name__ == '__main__':
    main()
