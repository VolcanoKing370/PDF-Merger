from pypdf import PdfWriter

#Get the number of files to merge
print('How many files do you want to merge?')
n = int(input())
pdfs=[];
#Add the files loop
for i in range(n):
    print('File#'+str(i+1))
    pdf = input()
    pdfs.append(pdf)

#Merge the files
concatenator = PdfWriter()

for pdf in pdfs:
    concatenator.append(pdf)

concatenator.write("result.pdf")

#End program TYFUMP
concatenator.close()
print("Done merging! Please look for \'result.pdf\' to find your output. TYFUMP!")
