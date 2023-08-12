import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import numpy as np
from urllib.request import urlopen


result = requests.get("https://reliefweb.int/jobs?advanced-search=%28C226%29")
src = result.content
soup = bs(src,"lxml")
contentee = soup.find_all("article",{"class":"rw-river-article--card rw-river-article rw-river-article--job"},"a")
bs.prettify(contentee[0])
j_title = contentee[0].findAll("h3",{"class":"rw-river-article__title"})
# code to show job tilte of carrer
j_title[0].text
# code to show the org
org = contentee[0].findAll("a",{"class":"rw-entity-meta__tag-link"})
org[0].text
# here open pst date 
open_date = contentee[0].findAll("dd",{"class":"rw-entity-meta__tag-value rw-entity-meta__tag-value--posted rw-entity-meta__tag-value--date"})
open_date[0].text
# here colsing post date
closing_date = contentee[0].findAll("dd",{"class":"rw-entity-meta__tag-value rw-entity-meta__tag-value--closing-date rw-entity-meta__tag-value--date rw-entity-meta__tag-value--last"})
closing_date[0].text
# write the file 
f= open("UN1111_J.csv","w")
headrer = "j_title,org,open_date,closeing_date\n"
f.write(headrer)


for contentee in contentee :
    j_title = contentee.findAll("h3",{"class":"rw-river-article__title"})
    job_name = j_title[0].text.strip()
    org = contentee.findAll("a",{"class":"rw-entity-meta__tag-link"})
    org_name=org[0].text.strip()
    open_date = contentee.findAll("dd",{"class":"rw-entity-meta__tag-value rw-entity-meta__tag-value--posted rw-entity-meta__tag-value--date"})
    open_date_p=open_date[0].text.strip()
    closing_date = contentee.findAll("dd",{"class":"rw-entity-meta__tag-value rw-entity-meta__tag-value--closing-date rw-entity-meta__tag-value--date rw-entity-meta__tag-value--last"})
    c_date = closing_date[0].text.strip()
    f.write(job_name +","+ org_name + "," +open_date_p +","+c_date+ "\n")
    
f.close()

    