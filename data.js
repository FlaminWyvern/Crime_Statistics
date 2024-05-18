// GET request:
function ajaxGetRequest(path, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}

// POST request:
function ajaxPostRequest(path, data, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
  
}// GET data (bar and pie)
function getData(){
  ajaxGetRequest("/bar", displayBar);
  ajaxGetRequest("/pie", displayPie);
}
// Bar Graph open/config
function displayBar(resp){
  let bar = JSON.parse(resp);
  let trace = {};
  trace.x = Object.keys(bar);
  trace.y = Object.values(bar);
  trace.type = "bar";

  let layout = {
  "title": "Incident by Date",
  "xaxis": {"title": "Year"},
  "yaxis": {"title": "# of incidents"}
};

  let data = [trace];
  let bt = document.getElementById("bar");
  Plotly.newPlot(bt, data, layout);
}
// Pie Chart open/config
function displayPie(resp){
  let pie = JSON.parse(resp);
  let trace = {};
  trace.values = Object.values(pie);
  trace.labels = Object.keys(pie);
  trace.type = "pie";

  let layout = {"title": "Incident by Day of Week"}

  let data = [trace];
  let pt = document.getElementById("pie");
  Plotly.newPlot(pt, data, layout)
}
// POST data (line)
function getHourData(){
  let hourElement = document.getElementById("hour");
  let hour = hourElement["value"];
  hourElement["value"] = "";
  let data = { "hour": hour };
  let jsonData = JSON.stringify(data);
  ajaxPostRequest("/line", jsonData, displayLine);
}



// Line Graph open/config
function displayLine(resp){
  let hour = document.getElementById("hour")
  let line = JSON.parse(resp);
  let trace = {};
  trace.x = Object.keys(line);
  trace.y = Object.values(line);

  let layout = {
  "title":  "# of incidents at " + hour.value + ":00",
  "xaxis": {"title": "Year"},
  "yaxis": {"title": "# of incidents"}
};

  let data = [trace];
  let lt = document.getElementById("line");
  Plotly.newPlot(lt, data, layout)
}


