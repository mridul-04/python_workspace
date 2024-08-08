import csv
newFile=open('d:\\example.csv','w',  newline='')
newFileWriter =csv.writer(newFile)
newFileWriter.writerow(['Name','Score'])
newFileWriter.writerow(['Hrithik',3])
newFileWriter.writerow(['Mridul',3])
newFile.close()

newFile=open('d:\\example.csv','r')
newFileReader =csv.reader(newFile)
for row in newFileReader:
    print (row)
newFile.close()