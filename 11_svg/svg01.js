//Stefan Tan
//SoftDev2 pd8
//K11 -- Ask Circles [Change || Die] …While On The Go
//2019-03-15

var p = document.getElementById("vimage");

var clrbut = document.getElementById("but_clear");
var movbut = document.getElementById("but_move");
var spdbut = document.getElementById("but_speed");

var prevx;
var prevy;
var requestID = 0;
var isMoving = false;

var clear = function() {
    prevx=NaN;
    prevy=NaN;
    p.innerHTML=""
}

var circle = function(x, y) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", x);
    c.setAttribute("cy", y);
    c.setAttribute("r", 20);
    c.setAttribute("fill", "blue");
    c.setAttribute("stroke", "black");
    p.appendChild(c);
    c.addEventListener("click", function(e) {
	color(e, c);
    });
}

var color = function(e, c) {
    e.stopPropagation();
    if(c.getAttribute("fill") == "blue") {
	c.setAttribute("fill", "green");
    }
    else if (c.getAttribute("fill") == "green") {
	var newc = circle(Math.random() * 500, Math.random() * 500);
	p.removeChild(c);
	p.appendChild(newc);
    }
}

var move = function() {
    var children = p.childNodes; 
    window.cancelAnimationFrame (requestID);
    
    var height = parseInt(p.getAttribute('height'));
    var width = parseInt(p.getAttribute('width'));
    
    for (var i = 1; i < children.length; i++) {
	children[i].setAttribute('xVel', 1);
        children[i].setAttribute('yVel', 1);
    };
    
    isMoving = true; 
    
    var moving = function() {
	window.cancelAnimationFrame (requestID);
	for (var i = 1; i < children.length; i++) {
    	    var cx = parseInt(children[i].getAttribute('cx'));
	    var cy = parseInt(children[i].getAttribute('cy'));
	    var xVel = parseInt(children[i].getAttribute('xVel'));
	    var yVel = parseInt(children[i].getAttribute('yVel'));
            if (cx >= width || cx <= 0){
		xVel *= -1;
		children[i].setAttribute('xVel', xVel);
            };
            if (cy >= height || cy <= 0){
		yVel *= -1;
		children[i].setAttribute('yVel', yVel);
	    };
	    children[i].setAttribute('cx', cx + xVel);
            children[i].setAttribute('cy', cy + yVel);
	};
    	requestID = window.requestAnimationFrame(moving);
    };
    moving();
};

var speed = function(){
    var children = p.childNodes;
    for (var i = 1; i < children.length; i++) {
	var xVel = parseInt(children[i].getAttribute('xVel'));
	var yVel = parseInt(children[i].getAttribute('yVel'));
	if (Math.abs(xVel) == 1 && Math.abs(yVel) == 1) {
	    children[i].setAttribute('xVel', xVel * 4);
	    children[i].setAttribute('xVel', xVel * 4);
	}
	else {
	    children[i].setAttribute('xVel', xVel / 4);
	    children[i].setAttribute('xVel', xVel / 4);
	}
    }
};

var draw = function(e) {
    var x = e.offsetX;
    var y = e.offsetY;
    circle(x,y);
}

clrbut.addEventListener('click', clear);
p.addEventListener('click', draw);
spdbut.addEventListener('click', speed);
movbut.addEventListener('click', function(){
    if (!isMoving) {
	move();
    }
});


