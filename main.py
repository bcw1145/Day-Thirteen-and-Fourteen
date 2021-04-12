import os
from flask import Flask, render_template, request, redirect, send_file
from stackoverflow import get_last_page_s, find_jobs_s
from wwr import find_jobs_w
from remoteok import find_jobs_r
from exporter import save_to_file

app = Flask("RemoteJobs")
os.system('clear')
url_s = "https://stackoverflow.com/jobs?r=true&q="
url_w = "https://weworkremotely.com/remote-jobs/search?term="
url_r = "https://remoteok.io/remote-"
keywords = [
    'python', 'ruby', 'c', 'c++', 'django', 'go', 'java', 'swift', 'docker',
    'frontend', 'backend', 'react', 'git', 'sql', 'nosql', 'linux', 'windows',
    'scala', 'database', 'node.js', 'agile', 'mongodb', 'algorithm',
    'embedded', 'cloud', 'kotlin', 'kubernetes', 'devops', 'graphics', 'ui'
]


def get_jobs(word):
    db = []
    last_page_s = get_last_page_s(url_s + word)
    for page in range(last_page_s):
        url = url_s + word + f"pg={page+1}"
        db = db + find_jobs_s(url)
    db = db + find_jobs_w(url_w + word)
    db = db + find_jobs_r(url_r + word + "-jobs")
    return db


data = {}


@app.route("/")
def home():
    return render_template("search.html", keywords=keywords)


@app.route('/search')
def search():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = data.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            data[word] = jobs

    else:
        return redirect("/")
    return render_template("report.html",searchingBy=word,resultNumber=len(jobs),jobs=jobs)


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = data.get(word)
        print(jobs)
        if not jobs:
            raise Exception()
        return send_file(save_to_file(word, jobs))
    except:
        return redirect('/')


app.run(host="0.0.0.0")

if __name__ == '__main__':
    app.run(debug=True)
