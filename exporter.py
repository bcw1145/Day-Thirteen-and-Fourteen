import csv


def save_to_file(word, jobs):
    f_name = f"{word}.csv"
    file = open(f_name, mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "link"])
    for job in jobs:
        writer.writerow(job)
    return f_name
