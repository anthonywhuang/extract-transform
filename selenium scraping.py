from socket import timeout
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Chrome("./chromedriver")

dataframe = pd.DataFrame(columns=["Title","Location","Company","Salary","Qualifications","Requirements"])

driver.get("https://www.indeed.com/jobs?q=mechanical%20engineer&l=Oakland%2C%20CA&start=10")
driver.implicitly_wait(4)

all_jobs = driver.find_elements_by_class_name('result')

for job in all_jobs:

    result_html = job.get_attribute('innerHTML')
    soup = BeautifulSoup(result_html, 'html.parser')

    try:
        title = soup.find("h2",class_="jobTitle").text.replace('/n','')
    except: 
        title = 'None'
    print(title.replace('new',''))

    try:
        location = soup.find('div', class_ ='companyLocation').text
    except:
        location = 'None'
    print(location)

    try:
        company = soup.find('span', class_ ='companyName').text
    except:
        company = 'None'
    print(company)

    try:
        salary = soup.find('span', class_ = 'estimated-salary').text
    except:
        salary = ''
    print(salary)


driver.quit()