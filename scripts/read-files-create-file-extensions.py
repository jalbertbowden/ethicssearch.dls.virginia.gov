import magic
import os

files = ['filing-id-4030-lr', 'filing-id-4594-lr', 'filing-id-4595-lr', 'filing-id-4597-lr', 'filing-id-4598-lr', 'filing-id-4599-lr', 'filing-id-4602-lr', 'filing-id-4759-lr', 'filing-id-10-ld', 'filing-id-4-ld', 'filing-id-5-ld', 'filing-id-6-ld', 'filing-id-7-ld', 'filing-id-8-ld', 'filing-id-9-ld']
extpdf = 'application/pdf'
exthtml = 'text/html'

def createFileUpdate(file, ext):
	fileupdate = file + ext
	os.rename(file, file + ext)
	print('file update!')
	print(fileupdate)
	# return fileupdate

def getFileMimeType(file):
	mime = magic.Magic(mime=True)
	# print(file)
	#fileupdated = file + '.pdf'
	#print(fileupdated)
	# print(mime.from_file(file))
	return mime.from_file(file)

def writeFileExtension(mimet, extpdf, exthtml):
	if mimet == extpdf:
		ext = '.pdf'
		createFileUpdate(file, ext)
		# print('File changed to PDF!')
	if mimet == exthtml:
		ext = '.html'
		createFileUpdate(file, ext)
		# print('File changed to HTML!')

for file in files:
	mimet = getFileMimeType(file)
	writeFileExtension(mimet, extpdf, exthtml)