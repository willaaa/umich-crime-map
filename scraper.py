import requests
from datetime import date
from datetime import timedelta
import csv
today = date.today()
print(today.strftime("%m/%d/%Y"))
columns = ["id", "date", "description", "location", "address", "disposition", "narrative", "status", "latitude", "longitude"]
calls = []
for i in range(150):
    pullDate = today - timedelta(days=i)
    pullDate = pullDate.strftime("%m/%d/%Y")
    print(pullDate)
    r = requests.get('https://www.dpss.umich.edu/api/GetCrimeLogCache?date=' + pullDate).json()
    calls += r["data"]

with open('log.csv','w') as out:
    writer = csv.DictWriter(out, fieldnames=columns)
    writer.writeheader()
    for data in calls:
        writer.writerow(data)


