var express = require('express');
var router = express.Router();
var path = require('path');
const fs = require('fs');
var exec = require('child_process').exec;

/* GET home page. */
router.get('/', function(req, res, next) {
	
	var filename = '/Users/sam/Desktop/ASD/final/respberry-PMS5003T/finalDemo/AWS_IoT/test_sub.py'
	// exec('python3'+' '+filename,function(err,stdout,stderr){
	// 	console.log("!!!!")
	// });            
	// if(stdout){
	//     console.log("py success", stdout);
	    
	//     if(err){console.log("py fail", err);}
	// }
	// });

	fs.readFile('data.json', (err, data) => {  
	    if (err) throw err;
	    sensor = JSON.parse(data);
	    console.log(sensor);
	    humidity = sensor['humidity']
	    temperature = sensor['temperature']
	    PM25 = sensor['PM2.5']
	    PM1 = sensor['PM1.0']
	    PM10 = sensor['PM10']
	    res.render('index2', { humidity: humidity, temperature: temperature, PM25: PM25, PM1: PM1, PM10: PM10 });
	});
});

router.post('/ajax_update', (req, res, next) => {
	fs.readFile('data.json', (err, data) => {  
	    if (err) throw err;
	    sensor = JSON.parse(data);
	    res.json({
	    	humidity: sensor['humidity'],
	    	temperature: sensor['temperature'],
	    	PM25: sensor['PM2.5'],
	    	PM1: sensor['PM1.0'],
	    	PM10: sensor['PM10']
	    });
	});
});

router.get('/plugin', function(req, res, next) {
  res.render('plugin', { title: 'Express' });
});

router.get('/result', function(req, res, next) {
  res.render('show', { title: 'Express' });
});

router.get('/get_file/:filename', (req, res, next) => {
	var tar_file = req.params.filename;	
	res.sendFile(path.join(__dirname, '../public/images', tar_file));

});

module.exports = router;
