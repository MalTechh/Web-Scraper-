import requests
from bs4 import BeautifulSoup
page =requests.get("https://careers.united.com/job-search-results/")
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find('a', attrs={'id': "job-result0"})
results = results.string
#results = soup.find(class_ = "jobTitle")
print(results)
#print(results.prettify())