import csv

filename = 'data/sitka_weather_2018_full.csv'
with open(filename) as f: 
  reader = csv.reader(f)
  header_row = next(reader)
  
  # Get high temperatures from this file.
  highs = []
  for row in reader:
    high = int(row[5])
    highs.append(high)

print(highs)


  
  