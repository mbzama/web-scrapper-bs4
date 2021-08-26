import logging
import requests
from bs4 import BeautifulSoup
import xlwt

logging.basicConfig(level=logging.INFO)

###########################
# Reading content from the website
###########################
page = requests.get("https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm")
logging.info('Http Status: %s', page.status_code)

soup = BeautifulSoup(page.text, 'html.parser')

# Remove footer hyperlinks 
footerLinks = soup.find(class_='AlphaNav')
footerLinks.decompose()

body = soup.find(class_='BodyText') 
logging.debug(body)

anchorLinks = body.findAll('a')


###########################
# Writing to excelsheet
###########################
book = xlwt.Workbook()
ws = book.add_sheet('Artists')
ws.write(0, 0, 'Name')
ws.write(0, 1, 'Link')


index = 1
for link in anchorLinks:
    name = link.contents[0]
    href = 'https://web.archive.org' + link.get('href')
    logging.info('%s - %s', name, href)
    ws.write(index, 0, name)
    ws.write(index, 1, href)
    index = index+1

book.save("artists.xls")