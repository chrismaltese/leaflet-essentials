import cherrypy
from pymongo import Connection,GEO2D

class mongocherry(object):
    

    def index(self):
	db=Connection().albuquerque
	output =[]
	output.append("<HTML><HEAD><TITLE>QUERY MONGODB</TITLE></HEAD><BODY><h1>Query MongoDB</h1><link rel='stylesheet' href='http://cdn.leafletjs.com/leaflet-0.7.2/leaflet.css' /><style> html, body, #map {padding: 0;margin: 0;height: 100%;}</style></head><body><script src='http://cdn.leafletjs.com/leaflet-0.7.2/leaflet.js'></script><div id='map'></div><script>var map = L.map('map',{center: [35.10418, -106.62987],zoom: 9});L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(map);")
	


	for x in db.publicart.find():
		output.append("L.marker(["+str(x["loc"][0])+","+str(x["loc"][1])+"]).addTo(map).bindPopup(\""+x["name"]+"<img src='"+x["popup"]+"'>\");")
	

	output.append('</SCRIPT></BODY></HTML>')
	i=0
	html=""
	while i<len(output):
		html+=str(output[i])
		i+=1

	return html 



	
    
    index.exposed = True



cherrypy.config.update({'server.socket_host': '127.0.0.1',
                         'server.socket_port': 8000,
                        }) 

cherrypy.quickstart(mongocherry())