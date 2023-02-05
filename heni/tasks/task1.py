from lxml import html
import pandas as pd
from datetime import datetime


#get html and tree
html_page_link = 'heni/resources/webpage.html'
doc = html.parse(html_page_link)
# parse artist name
name = doc.xpath("//h1[@class='lotName']/text()")[0].split("(")[0].strip()
#parse painting name
paint = doc.xpath("//h2[@class='itemName']/i/text()")[0]
#parse price GBP
price_gbp = doc.xpath("//span[@id='main_center_0_lblPriceRealizedPrimary']/text()")[0]
#parse price US
price_us = doc.xpath("//div[@id='main_center_0_lblPriceRealizedSecondary']/text()")[0]
#parse price GBP est
price_gbp_est = doc.xpath("//span[@id='main_center_0_lblPriceEstimatedPrimary']/text()")[0]
#parse price US est
price_us_est = doc.xpath("//span[@id='main_center_0_lblPriceEstimatedSecondary']/text()")[0]
#image link
image = doc.xpath("//img[@id='imgLotImage']/@src")[0]
#sale date
sale_date = doc.xpath("//span[@id='main_center_0_lblSaleDate']/text()")[0]

x = pd.DataFrame([[name,paint,price_gbp,price_us,price_gbp_est,price_us_est.replace("(","").replace(")",""),image,sale_date]], 
                    columns=['name','paint','price realised gbp','price realised usd', 'price estimated gbp', 'price estimated usd', 'image', 'sale date'])
x.to_csv("output_task1.csv", index=False)