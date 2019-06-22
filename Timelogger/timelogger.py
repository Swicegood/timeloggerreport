from datetime import datetime,timedelta
import csv


path = "/Users/jaga/Google Drive/sleep-export.csv"
file = open(path, newline = '')
reader = csv.reader(file)

path = "/Users/jaga/Google Drive/aTimeLogger report"
file = open(path, newline = '')
reader2 = csv.reader(file)

def total_sleep(beginning_date, end_date, reader):
    data = []
    total_sleep = 0
    for row in reader:
        # Id	Tz	From	To	Sched	Hours	Rating	Comment	Framerate	Snore	Noise	Cycles	DeepSleep	LenAdjust	Geo (then specific data)
        try:
            date = datetime.strptime(row[2], '%d. %m. %Y %H:%M')
            hours = float(row[5])
            if beginning_date <= date <= end_date:
                data.append([hours])
                total_sleep = total_sleep + hours
        except:
            pass
    return total_sleep


header = next(reader2)

data2= []
firstrow = next(reader2)
end_date = datetime.strptime(firstrow[3], "%Y-%m-%d %H:%M")
# "Activity type","Duration","From","To","Comment"
while True:
    row = next(reader2)
    try:
        beginning_date = datetime.strptime(row[3], "%Y-%m-%d %H:%M")
    except:
        break



totals_header = next(reader2)

# "Activity type","Duration","%"

print("Time Spent: ",beginning_date, " to ", end_date)
print("Activity type         Duration  Percentage")
print("__________________________________________")

for row in reader2:
    if row[0] != "Untracked time":
        print("{0:22}{1:10}{2}%".format(row[0],row[1],row[2]))
    else:
        untracked_time = row[1].split(':')
        untracked_time = timedelta(hours=int(untracked_time[0]), minutes=int(untracked_time[1]))
        tot_sleep = total_sleep(beginning_date,end_date,reader)
        untracked_time = untracked_time - timedelta(hours=tot_sleep)
        row = next(reader2)
        total_time = row[1].split(':')
        total_time = timedelta(hours=int(total_time[0]), minutes=int(total_time[1]))
        print("Sleep{0:23}{1:8}%".format(tot_sleep.__round__(2), ((timedelta(hours=tot_sleep) / total_time) * 100).__round__(2)))
        print("Untracked time{0:13}{1:9}%".format(untracked_time.total_seconds()/3600, ((untracked_time.total_seconds()/ total_time.total_seconds()) *100).__round__(2)))
        print("________________________________")
        print("{0:22}{1:10}{2}%".format(row[0],row[1],row[2]))
        break