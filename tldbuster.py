import os
import csv
with open("tld.csv") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = [r for r in reader]
def check_ping(url):
    response = os.system("ping -c 1 " + url)
    if response == 0:
        pingstatus = "Network Active"
        a = open('urls.txt', 'a')
        a.write(domain+i[0] + "\n")
        a.close()
    else:
        pingstatus = "Network Error"
        a = open('urlsnotfound.txt', 'a')
        a.write(domain+i[0] + "\n")
        a.close()
    return pingstatus

domain=raw_input("Enter Host Name :- ")

for i in (data):
    response=check_ping(domain+i[0])
print("done")
