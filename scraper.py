import requests
from datetime import date
from datetime import timedelta
import csv
import concurrent.futures


def get_crime_log(date):
    r = requests.get('https://www.dpss.umich.edu/api/GetCrimeLogCache?date=' + date).json()
    return r["data"]


def write(calls):
    # with open('log.csv', 'w') as out:
    with open('testLog.csv', 'w') as out:
        writer = csv.DictWriter(out, fieldnames=columns)
        writer.writeheader()
        for data in calls:
            writer.writerow(data)


today = date.today()
print(today.strftime("%m/%d/%Y"))
columns = ["id", "date", "description", "location", "address", "disposition", "narrative", "status", "latitude",
           "longitude"]
calls = []

with concurrent.futures.ThreadPoolExecutor() as executor:
    for i in range(1,10):
        pullDate = today - timedelta(days=i)
        pullDate = pullDate.strftime("%m/%d/%Y")
        for future in concurrent.futures.as_completed([executor.submit(get_crime_log, pullDate)]):
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (pullDate, exc))
            else:
                calls += data
        # calls += executor.submit(get_crime_log, pullDate).result()
write(calls)
# for i in range(36):
#     pullDate = today - timedelta(days=i)
#     pullDate = pullDate.strftime("%m/%d/%Y")
#     write(get_crime_log(pullDate))
#
#     # print(pullDate)
#     # r = requests.get('https://www.dpss.umich.edu/api/GetCrimeLogCache?date=' + pullDate).json()
#     # calls += r["data"]
