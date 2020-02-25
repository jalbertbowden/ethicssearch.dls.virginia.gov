import magic
import os

extpdf = 'application/pdf'
exthtml = 'text/html'

dir = 'test'

def getDirectoryFilesList(dir):
	fileslisted = os.listdir(dir)
	allFiles = list()
	for entry in fileslisted:
		fullPath = os.path.join(dir, entry)
		allFiles.append(fullPath)
	return allFiles

def createFileUpdate(file, ext):
	fileupdate = file + ext
	os.rename(file, file + ext)
	print('file update!')
	print(fileupdate)

def getFileMimeType(file):
	mime = magic.Magic(mime=True)
	return mime.from_file(file)

def writeFileExtension(mimet, extpdf, exthtml):
	if mimet == extpdf:
		ext = '.pdf'
		createFileUpdate(file, ext)
	if mimet == exthtml:
		ext = '.html'
		createFileUpdate(file, ext)

files = getDirectoryFilesList(dir)

for file in files:
	mimet = getFileMimeType(file)
	writeFileExtension(mimet, extpdf, exthtml)