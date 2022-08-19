from pdf2image import convert_from_path
import numpy as np
from PIL import Image
import base64
from PyPDF2 import PdfReader
#Convert PDF to images
def helloworld (input1, input2):
    images1 = convert_from_path(input1)           #convert the pages of first PDF into images
    reader_1 = PdfReader(input1)
    number_of_pages_1 = len(reader_1.pages)       #get the number of pages of first PDF
    for i in range(len(images1)):
        imgs_comb_11 = np.vstack(images1)         #vertical stacking of pages

    images2 = convert_from_path(input2)           #convert the pages of second PDF into images
    reader_2 = PdfReader(input2)
    number_of_pages_2 = len(reader_2.pages)       #get the number of pages of second PDF
    difference =(number_of_pages_1 - number_of_pages_2)   # get the difference between the number of pages of first vs second PDF

    for i in range(len(images2)):
        imgs_comb_22 = np.vstack(images2)         #vertical stacking of pages

    number = abs(difference)                      #number is the number of blank pages needed
    if difference < 0:                            #if difference is negative, the first PDF has less number of pages
        h,w,c = imgs_comb_11.shape                #imgs_comb_11 is the vertically stacked array. Divide it by number of pages to get size of single page
        h = int(h/number_of_pages_1)
        w = int(w)
        blank_image1 = number*(255 * np.ones(shape=(h,w,c), dtype=np.uint8))   #create blank pages
        imgs_comb_11 = np.vstack([imgs_comb_11,blank_image1])                  #Vertical stack the blank pages with the first PDF
        #imgs_comb_1 = Image.fromarray(imgs_comb_111)
    else:                                         #if difference is positive, the second PDF has less number of pages
        h,w,c = imgs_comb_22.shape                #imgs_comb_22 is the vertically stacked array. Divide it by number of pages to get size of single page
        h = int(h/number_of_pages_2)
        w = int(w)
        blank_image2 = number*(255 * np.ones(shape=(h,w,c), dtype=np.uint8))   #create blank pages
        imgs_comb_22 = np.vstack([imgs_comb_22,blank_image2])                  #Vertical stack the blank pages with the second PDF
        #imgs_comb_2 = Image.fromarray(imgs_comb_222)


    imgs_final = np.hstack([imgs_comb_11,imgs_comb_22])                        #horizontal stack the PDF pages
    imgs_final_final = Image.fromarray(imgs_final)                             #convert the array to image object
    return imgs_final_final

