import requests
from bs4 import BeautifulSoup


def get_last_page_s(url):
    results = requests.get(url).text
    soup = BeautifulSoup(results, 'html.parser')
    pages = (soup.find_all(class_="s-pagination--item"))
    return int(pages[-2].text.strip())


def find_jobs_s(url):
    db = []
    results = requests.get(url).text
    soup = BeautifulSoup(results, 'html.parser')
    jobs = soup.find_all(class_="grid--cell fl1")
    for job in jobs:
        link = job.find("a")
        if link:
            title = link["title"]
            company = job.find(
                class_="fc-black-700 fs-body1 mb4").find("span").text.strip()
            url_link = "https://stackoverflow.com" + link["href"]
            db.append((title, company, url_link))
    return db
