//Stefan Tan
//SoftDev2 pd8
//K00 -- I See a Red Door...
//2019-01-30

var c = document.getElementById("slate");
var ctx = c.getContext("2d");

var clrbut = document.getElementById("clear");
var togbut = document.getElementById("toggle");

var isDot = false;

var clear = function() {
    ctx.clearRect(0, 0, c.width, c.height);
}

var toggle = function() {
    isDot = !isDot;
    if (isDot) {
	togbut.innerHTML = "Click for Boxes!";
    }
    else {
	togbut.innerHTML = "Click for Dots!";
    }
}

var box = function(x, y) {   
    ctx.fillStyle = "#ff0000";
    ctx.fillRect(x,y,100,200);
}

var dot = function(x, y) {
    ctx.beginPath();
    ctx.fillStyle = "blue";
    ctx.ellipse(x,y,5,5,0,0,2 * Math.PI);
    ctx.fill();
}

var draw = function(e) {
    var pageX = e.pageX;
    var pageY = e.pageY;
    var x = pageX - 8;
    var y = pageY - 122.21665954589844;
    if(isDot) {
	dot(x,y);
    }
    else {
	box(x,y);
    }
}   

clrbut.addEventListener('click', clear);
togbut.addEventListener('click', toggle);
c.addEventListener('click', draw);
