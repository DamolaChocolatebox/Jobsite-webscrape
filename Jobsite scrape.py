

import requests
from bs4 import BeautifulSoup

url = 'https://www.jobgurus.com.ng/jobs?search_keyword=graphic+designer&specialization=&work_level='
response = requests.get(url)

html_codes = response.text

soup = BeautifulSoup(html_codes, 'html.parser')
jobsite = soup.find_all('div', class_= 'panel-body')
jobdatepost = soup.find_all('div', class_= 'panel-footer clearfix')

for job in jobsite:
    job_title = job.h2.text
    job_link = job.h2.a['href']
    
for date in jobdatepost:
    dated = date.span.text
        # print(dated)
   
    
    print(f'{job_title}\nvisit link below to apply\n {job_link} \ndeadline\n {dated}')
