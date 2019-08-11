from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input = PdfFileReader(open("/home/pi/Downloads/XIN-2019-08.pdf", "rb"))

# print how many pages input1 has:
pageCount = input.getNumPages()

#output.addPage(input1.getPage(1).rotateClockwise(90))
zine = output.addBlankPage(11 * 72, 8.5 * 72)
scale = 0.31
ph = 8.5*72
pw = 11*72
m = 5 # margin

# each page should be 2.75 x 4.25
# scaled up to roughly 8.5 x 11, that's 8.5 x 13.13 (just shy of legal size)

#zine.mergeRotatedScaledTranslatedPage(input1.getPage(0), 180, scale, scale*pw*2, pw/2)
zine.mergeRotatedScaledTranslatedPage(input.getPage(1), 0, scale, (3*pw/4)+m, (ph/2)-m)
zine.mergeRotatedScaledTranslatedPage(input.getPage(2), 0, scale, 2*pw/4, (ph/2)-m)
zine.mergeRotatedScaledTranslatedPage(input.getPage(3), 0, scale, pw/4, (ph/2)-m)
zine.mergeRotatedScaledTranslatedPage(input.getPage(4), 0, scale, 0, (ph/2)-m)

zine.mergeRotatedScaledTranslatedPage(input.getPage(0), 0, scale, 3*pw/4, -m)
zine.mergeRotatedScaledTranslatedPage(input.getPage(5), 0, scale, 0, -m)
zine.mergeRotatedScaledTranslatedPage(input.getPage(6), 0, scale, pw/4, -m)
if pageCount > 7:
    zine.mergeRotatedScaledTranslatedPage(input.getPage(7), 0, scale, 2*pw/4, -m)

# finally, write "output" to document-output.pdf
outputStream = open("zine.pdf", "wb")
output.write(outputStream)