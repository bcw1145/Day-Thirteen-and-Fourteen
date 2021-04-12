import requests
from bs4 import BeautifulSoup


def find_jobs_w(url):
    db = []
    results = requests.get(url).text
    soup = BeautifulSoup(results, 'html.parser')
    links = soup.find_all("ul")
    for link in links:
        if link.find_all("a"):
            jobs = link.find_all("a")
            for job in jobs:
                if job.find(class_="title"):
                    title = job.find(class_="title").text.strip()
                    company = job.find(class_="company").text.strip()
                    url_link = "https://weworkremotely.com" + job["href"]
                    db.append((title, company, url_link))
    return db
