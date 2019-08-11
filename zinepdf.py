#!/usr/bin/python

# This script takes a 7 or 8 page legal size pdf and makes a one-page foldable zine

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

if len(sys.argv) < 2:
    print('Usage: zinepdf.py <inputFile> (<outputFile>)')
    quit()

inputFile = sys.argv[1]

print('Opening %s' % inputFile)
input = PdfFileReader(open(inputFile, "rb"))

output = PdfFileWriter()
outputFile = "zine.pdf"
if len(sys.argv) > 2:
    outputFile = sys.argv[2]    

pageCount = input.getNumPages()

zine = output.addBlankPage(11 * 72, 8.5 * 72)
scale = 0.31
ph = 8.5*72
pw = 11*72

# each page should be 2.75 x 4.25
# scaled up to roughly 8.5 x 11, that's 8.5 x 13.13 (just shy of legal size)
# see http://experimentwithnature.com/02-found/experiment-with-paper-how-to-make-a-one-page-zine/attachment/content-1/

zine.mergeRotatedScaledTranslatedPage(input.getPage(1), 180, scale, pw, ph)
zine.mergeRotatedScaledTranslatedPage(input.getPage(2), 180, scale, 3*pw/4, ph)
zine.mergeRotatedScaledTranslatedPage(input.getPage(3), 180, scale, 2*pw/4, ph)
zine.mergeRotatedScaledTranslatedPage(input.getPage(4), 180, scale, pw/4, ph)

zine.mergeRotatedScaledTranslatedPage(input.getPage(0), 0, scale, 3*pw/4, 0)
zine.mergeRotatedScaledTranslatedPage(input.getPage(5), 0, scale, 0, 0)
zine.mergeRotatedScaledTranslatedPage(input.getPage(6), 0, scale, pw/4, 0)
if pageCount > 7:
    zine.mergeRotatedScaledTranslatedPage(input.getPage(7), 0, scale, 2*pw/4, 0)

# write to zine.pdf
print('Writing to %s' % outputFile)
outputStream = open(outputFile, "wb")
output.write(outputStream)