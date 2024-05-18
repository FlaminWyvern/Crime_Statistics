import csv
# Functions:

# => gen_dictionary: returns dictionary {'v': 0} if key inside data
def gen_dictionary(data, key):
  acc = {}
  for dict in data:
    if key in dict.keys():
      v = dict[key]
      acc[v] = 0
  return acc

# => total_matches: returns a float number if key and value of k,v pair in data
def total_matches(lod, k, v):
  acc = float(0)
  for dict in lod:
    if v in dict.values():
      if dict[k] == v:
        acc += 1
  return acc

# => total_matches_specific: returns a float if the first key and value of k,v pair in data and if the second key and value of k2,v2 pair in data
def total_matches_specific(lod, k, v, k2, v2):
  acc = float(0)
  for dict in lod:
    if v in dict.values():
      if dict[k] == v and dict[k2] == v2:
        acc += 1
  return acc

# => remove_min: takes items with values above minimum value and puts them in another dictionary
def remove_min(data, min):
  newDict = {}
  for key in data.keys():
    if data[key] > min:
      newDict[key] = data[key]
  return newDict

# Bar Chart
def bar_chart():
  with open("saved_data.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    acc = {}
    for row in reader:
      year = row[0]
      if year not in acc:
        acc[year] = 0
      acc[year] += 1
    acc = remove_min(acc, 20)
    return acc
# print(bar_chart())
# Pie Chart
def pie_chart():
  with open("saved_data.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    acc = {}
    for row in reader:
      day = row[4]
      if day not in acc:
        acc[day] = 0
      acc[day] += 1
    return acc

