import requests
from bs4 import BeautifulSoup


def find_jobs_r(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }

    db = []
    results = requests.get(url, headers=headers).text
    soup = BeautifulSoup(results, 'html.parser')
    links = soup.find_all(class_="company position company_and_position")
    for link in links:
        if link.find("h2"):
            url_link = "https://remoteok.io" + link.find("a")["href"]
            title = link.find("h2").text
            company = link.find("h3").text
            db.append((title, company, url_link))
    return db
