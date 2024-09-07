import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    fname = "%s.txt" % os.getpid()
    with open(fname, "w") as f:
        f.write(results)
    return fname

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import numpy as np
import os
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
# set to highest available resolution (as recommended by tesseract)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files