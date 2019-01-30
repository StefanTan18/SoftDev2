//Stefan Tan
//SoftDev2 pd08
//K00 -- I See a Red Door...
//2019-01-30

var clrb = document.getElementById("clear");
var togb = document.getElementById("toggle");



var box = function(e) {
    var c = document.getElementById("slate");
    var ctx = c.getContext("2d");
    ctx.fillStyle = "ff0000";
    ctx.fillRect(50,50,100,200);
}
