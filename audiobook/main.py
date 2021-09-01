# this program is to convert pdf to audio books

# firstly install this kit in terminal 

import pyttsx3
import PyPDF3

book =open('oop.pdf', 'rb')
pdfReader = PyPDF3.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker =pyttsx3.init()
page = pdfReader.getPage(7)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()