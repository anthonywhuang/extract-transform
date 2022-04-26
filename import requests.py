#import selenium
#from selenium import webdriver
#driver = webdriver.Chrome(executable_path=r'C:\Users\antho\Desktop\python 3\Tableau Project\\chromedriver.exe')

#from selenium import webdriver
#options = webdriver.ChromeOptions() 
#options.add_argument("start-maximized")
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\antho\Desktop\python 3\Tableau Project\\chromedriver.exe')

import requests
from bs4 import BeautifulSoup



def extract(page): 
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q=mechanical%20engineer&l=Oakland%2C%20CA&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'job_seen_beacon')
    for item in divs: 
        title = item.find('h2', class_ = 'jobTitle').text.strip()
        print(title.replace('new',''))
        company = item.find('span', class_ ='companyName').text.strip()
        location = item.find('div', class_ ='companyLocation').text.strip()
        try:
            salary = item.find('span', class_ = 'estimated-salary').text.strip()
        except:
                salary = ''
        qualifications = [[i.text for i in b.find_all('li')] for b in soup.find(id="jobDescriptionText")]
        print(qualifications)
        #qualifications = [[i.text for i in b.find_all('li')] for b in soup.find('class_', {'id':'jobDescriptionText'}).find_all('ul')].text
        #print(qualifications)
    return

c = extract(0)
transform(c)