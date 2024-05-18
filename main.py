# Import(s)
import bottle
import process
import csv
import json
import os.path
import data 

# FETCHING & CACHING
def startup( ):
  csv_file = 'saved_data.csv'
  if not os.path.isfile(csv_file):
    url = 'https://data.buffalony.gov/resource/d6g9-xbgu.json?$limit=50000'
    info = data.json_loader(url)
    data.fix_data(info,"incident_datetime")
    heads = ['year','month','hour_of_day','incident_type_primary','day_of_week']
    data.save_data(info, heads, csv_file)
    
# Routes and Functions (WEB SERVER)
@bottle.route("/")
def serve_html():
  return bottle.static_file("chart.html", root=".")

@bottle.route("/data.js")
def serve_javascript():
  return bottle.static_file("data.js", root = ".")

@bottle.get("/bar")
def json_bar_data():
  bar = process.bar_chart()
  json_bar = json.dumps(bar)
  return json_bar

@bottle.get("/pie")
def json_pie_data():
  pie = process.pie_chart()
  json_pie = json.dumps(pie)
  return json_pie

@bottle.post("/line")
def json_line_data():
  json_receive = bottle.request.body.read().decode()
  hour_dic = json.loads(json_receive)
  hr = hour_dic["hour"]
  with open("saved_data.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    acc = {}
    for row in reader:
      hour = row[2]
      year = row[0]
      if hour == hr:
        if year not in acc:
          acc[year] = 0
        acc[year] += 1
    acc = process.remove_min(acc, 20)
    json_line = json.dumps(acc)
    return json_line

bottle.run(host="0.0.0.0", port = 8080)
  