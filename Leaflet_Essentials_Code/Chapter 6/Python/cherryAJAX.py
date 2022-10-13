import cherrypy
from pymongo import Connection,GEO2D
from cherrypy import tools
import json

class mongocherry(object):
    
    @cherrypy.expose
    def index(self):
	db=Connection().albuquerque
	output =[]
	output.append("<HTML><HEAD><TITLE>QUERY MONGODB</TITLE></HEAD><BODY><h1>Query MongoDB</h1><link rel='stylesheet' href='http://cdn.leafletjs.com/leaflet-0.7.2/leaflet.css' /><style> html, body, #map {padding: 0;margin: 0;height: 100%;}</style></head><body><script src='http://cdn.leafletjs.com/leaflet-0.7.2/leaflet.js'></script><div id='map'></div><script>var lat; var lon; var map = L.map('map',{center: [35.10418, -106.62987],zoom: 9});L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(map);map.on('click',function(e){var a=String(e.latlng).split(\",\");lat=a[0].split(\"(\");lon=a[1].split(\")\");var xhReq = new XMLHttpRequest();var s=\"getdata?x=\";var s2=String(lat[1]);var s3=\"&y=\";var s4=String(lon[0]);var url=s.concat(s2,s3,s4); xhReq.open(\"GET\", url, false); xhReq.send(null); var serverResponse = xhReq.responseText; var d=JSON.parse(serverResponse);L.marker([d[0].lat,d[0].long]).addTo(map);L.marker([d[1].lat,d[1].long]).addTo(map);L.marker([d[2].lat,d[2].long]).addTo(map);});")
	
	
	

	output.append("</SCRIPT></BODY></HTML>")
	i=0
	html=""
	while i<len(output):
		html+=str(output[i])
		i+=1

	return html 
    @cherrypy.expose
    @tools.json_out()
    def getdata(self,x,y):
	db=Connection().albuquerque
	data=[]
	lat=float(x)
	long=float(y)
	for doc in db.publicart.find({"loc": {"$near": [lat, long]}}).limit(3): 
		data.append({'lat':str(doc["loc"][0]),'long':str(doc["loc"][1])})
	return data	
	
    


cherrypy.config.update({'server.socket_host': '127.0.0.1',
                         'server.socket_port': 8000,
                        }) 

cherrypy.quickstart(mongocherry())