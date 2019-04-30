/*
Stefan Tan
SoftDev2 pd8
K21 -- Onions, Bell Peppers, and Celery, Oh My!
2019-04-29
*/

d3.json("2006_-_2012_School_Demographics_and_Accountability_Snapshot.json").then(function(data) {

    //console.log(data);

    //mean of total enrollment in 2011-2012
    var d0 = data.filter(function(n) {return (n['schoolyear'] == 20112012);});
    var total = d0.reduce(function(a,b) {return a + b['total_enrollment']}, 0);
    var mean = total/d0.length;
    var average = document.getElementById('avg');
    average.innerHTML = mean;
    //console.log(mean);

    //%female of total enrollment in 2011-2012
    var d1 = data.filter(function(n) {return (n['schoolyear'] == 20112012);});
    var tot_fem = d0.reduce(function(a,b) {return a + parseInt(b['female_num'])}, 0);
    var fem = tot_fem/total * 100;
    //console.log(tot_fem);
    //console.log(total);
    //console.log(fem);
    var female = document.getElementById('fem');
    female.innerHTML = fem + "%";

    //number of male enrollment in 2011-2012
    var d2 = data.filter(function(n) {return (n['schoolyear'] == 20112012);});
    var tot_male = d0.reduce(function(a,b) {return a + parseInt(b['male_num'])}, 0);
    var male = document.getElementById('mal');
    male.innerHTML = tot_male;
});
