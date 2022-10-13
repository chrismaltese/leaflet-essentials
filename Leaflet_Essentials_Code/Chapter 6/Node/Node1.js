require('http').createServer(function (req, res) {
	if ('/' == req.url){
		res.writeHead(200, { 'Content-Type': 'text/html' });
		require('fs').createReadStream('leafletessentials.html').pipe(res);
        }
}).listen(3000);
