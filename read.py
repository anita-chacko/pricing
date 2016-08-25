import csv
import sys

#print 'Number of arguments', len(sys.argv)
#print '2nd argument', sys.argv[1]

if len(sys.argv)<3:
    print "Invalid arguments"
    print "Example read.py filename.csv price"
    sys.exit(0)

file_name=sys.argv[1]
price=int(sys.argv[2])

with open(file_name) as csvfile:
   readCSV=csv.reader(csvfile, delimiter= ',')
   next(readCSV,None)
   for columns in readCSV:
    type=columns[1]
    address=columns[2]
    city=columns[3]
    if columns[6]=='':
       columns[6]=0
    listprice=int(columns[6])
    if columns[7]=='':
       columns[7]=0
    beds=float(columns[7])
    if columns[8]=='':
       columns[8]=0
    baths=float(columns[8])
    if columns[10]=='':
       columns[10]=0
    sqft=int(columns[10])
    if columns[11]=='':
       columns[11]=0
    lotsize=int(columns[11])
    if columns[12]=='':
       columns[12]=0
    year=int(columns[12])
    if columns[13]=='':
       columns[13]=0
    parking=int(columns[13])
    if columns[15]=='':
       columns[15]=0
    days=int(columns[15])
    status=columns[16]
    url=columns[24]

    if status=="Active" and listprice<=price:
         print type, '$',listprice, "bed", beds, "baths", baths, "sqft",sqft, "lot size", lotsize, "year" , year, "parking",parking, "days" ,days, "url", url
