/*
Team 3D D3 -- Puneet Johal & Stefan Tan
SoftDev2 pd8
K15 -- Scattered
2019-03-21
*/

var data = [
    [ 5, 20 ],
    [ 480, 90 ],
    [ 250, 50 ],
    [ 100, 33 ],
    [ 330, 95 ],
    [ 410, 12 ],
    [ 475, 44 ],
    [ 25, 67 ],
    [ 85, 21 ],
    [ 220, 88 ]
];


var margin = {top: 20, right: 15, bottom: 60, left: 60}
var width = 960 - margin.left - margin.right
var height = 500 - margin.top - margin.bottom;

var x = d3.scaleLinear()
    .domain([0, d3.max(data, function(d) { return d[0]; })])
    .range([ 0, width ]);

var y = d3.scaleLinear()
    .domain([0, d3.max(data, function(d) { return d[1]; })])
    .range([ height, 0 ]);

var chart = d3.select('body')
    .append('svg')
    .attr('width', width + margin.right + margin.left)
    .attr('height', height + margin.top + margin.bottom)
    .attr('class', 'chart')

var main = chart.append('g')
    .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')
    .attr('width', width)
    .attr('height', height)
    .attr('class', 'main')   

// draw the x axis
var xAxis = d3.axisBottom(x);

main.append('g')
    .attr('transform', 'translate(0,' + height + ')')
    .attr('class', 'main axis date')
    .call(xAxis);

// draw the y axis
var yAxis = d3.axisLeft(y);

main.append('g')
    .attr('transform', 'translate(0,0)')
    .attr('class', 'main axis date')
    .call(yAxis);

var g = main.append("g"); 

g.selectAll("dots")
    .data(data)
    .enter().append("circle")
    .attr("cx", function (d,i) { return x(d[0]); } )
    .attr("cy", function (d) { return y(d[1]); } )
    .attr("r", 5);
