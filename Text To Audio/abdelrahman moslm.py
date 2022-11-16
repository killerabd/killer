import pyttsx3
import PyPDF2
 

pdf_file = open('cat.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)
number_of_pages = read_pdf.getNumPages()
engine = pyttsx3.init()

for i in range(0, number_of_pages ):
    page = read_pdf.getPage(i)
    page_content = page.extractText()
    
    newrate=200
    engine.setProperty('rate', newrate)
    newvolume=200
    engine.setProperty('volume', newvolume)
    
    engine.say(page_content)
    engine.save_to_file(page_content , "audio.wav")
    

    engine.runAndWait()
