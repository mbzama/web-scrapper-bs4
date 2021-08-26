import xlwt
from datetime import date

descriptions = ['d1','d2','d3']
urls = ['u1','u2','u3']
predictions = ['p1','p2','p3']


book = xlwt.Workbook()
ws = book.add_sheet('Companies')
ws.write(0, 0, 'URL')
ws.write(0, 1, 'Description')
ws.write(0, 2, 'Prediction')
length = len(descriptions)

for index in range(length):
    ws.write(index + 1, 0, urls[index])
    ws.write(index + 1, 1, descriptions[index])
    ws.write(index + 1, 2, predictions[index])
             
book.save("test.xls")