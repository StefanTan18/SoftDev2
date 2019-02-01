//Team Jam Sandwich - Derek Song & Stefan Tan
//SoftDev2 pd8
//K01 -- ...and I want to Paint It Better
//2019-01-31

//e.preventDefault(); was not used but the default action is not performed when this is called

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
}

var box = function(x, y) {   
    ctx.fillStyle = "#ff0000";
    ctx.fillRect(x,y,100,200);
}

var dot = function(x, y) {
    ctx.beginPath(); //When called, it resets the path, clearing all the previous calls
    ctx.fillStyle = "blue";
    ctx.ellipse(x,y,5,5,0,0,2 * Math.PI);
    ctx.fill();
}

var draw = function(e) {
    var x = e.offsetX; //The value of the x coordinate relative to the canvas (upper left corner)
    var y = e.offsetY; //The value of the y coordinate relative to the canvas (upper left corner)
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
