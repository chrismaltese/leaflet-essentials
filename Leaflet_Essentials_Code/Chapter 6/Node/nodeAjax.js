require('http').createServer(function (req, res) {
	if ('/' == req.url){
		res.writeHead(200, { 'Content-Type': 'text/html' });
		require('fs').createReadStream('leafletessentialsAjax.html').pipe(res);
        } else if ('/getpoints'==req.url){
		res.writeHead(200, { 'Content-Type': 'application/json' });
		res.end(JSON.stringify([{"lat":35,"long":-106}]));
	} else {
		res.writeHead(404);
		res.end('The page you requested '+req.url+' was not found');
	}
}).listen(3000);

