//Example script to place and manipulate "datapoints
// this uses the

function run(){

    // generate random data set
    var dataset = [];
    for( var i = 0; i< 25; i++) {
        dataset.push( Math.random()*30 )
    }


    d3.select("body").select("#pageContent").append("div")
        .selectAll("div")
        .data(dataset)
        .enter()
        .append("div")
        .attr("class", "bar")
        .style( "height", function(d) {
            var barHeight = d * 5;
            return barHeight + "px"
        })


    var interact = [1,2,3,4];

    var force = d3.layout.force()
        .charge(-120)
        .linkDistance(30)
        .size([800, 200])

    var svgContainer = d3.select("body").select("#pageContent")
        .append("svg")
        .attr("width", 800)
        .attr("height", 200);

    var circles = svgContainer.selectAll("circle")
        .data(interact)
        .enter().append("circle")
        .attr("cx", function(d) { return 60*d + 25; })
        .attr("cy", function(d) { return 100; })
        .attr("r", 25)
        .call(force.drag);

    force
        .nodes(circles)
        .start();



}

window.onload = run;

