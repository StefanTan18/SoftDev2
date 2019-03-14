//Stefan Tan
//SoftDev2 pd8
//K10x -- Ask Circles [Change || Die]
//2019-03-13

var p = document.getElementById("vimage");

var clrbut = document.getElementById("but_clear");

var prevx;
var prevy;

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
    if(c.getAttribute("fill") == "blue") {
	c.setAttribute("fill", "green");
    }
    else if (c.getAttribute("fill") == "green") {
	var newc = circle(Math.random() * 500, Math.random() * 500);
	p.removeChild(c);
	p.appendChild(newc);
    }
}

var draw = function(e) {
    var x = e.offsetX;
    var y = e.offsetY; 
    circle(x,y);
}

clrbut.addEventListener('click', clear);
p.addEventListener('click', draw);
