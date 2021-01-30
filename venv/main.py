import pyttsx3
import  PyPDF2
book = open('oop.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)

pages = pdfReader.numPages
print(pages)
for num in range(8,pages):

    speaker = pyttsx3.init()
    pages = pdfReader.getPage(7)
    text = pages.extractText()
    speaker.say(text)
    speaker.runAndWait()
