require('http').createServer(function (req, res) {
	if ('/' == req.url){
		res.writeHead(200, { 'Content-Type': 'text/html' });
		require('fs').createReadStream('leafletessentialsAjax.html').pipe(res);
        } else if ('/getpoints'==req.url){
		res.writeHead(200, { 'Content-Type': 'application/json' });
		var lat=Math.random()*(36-35)+35;
		var lon=Math.random()*(-107+106)-106;
		res.end(JSON.stringify([{"lat":lat,"long":lon}]));
	} else {
		res.writeHead(404);
		res.end('The page you requested '+req.url+' was not found');
	}
}).listen(3000);