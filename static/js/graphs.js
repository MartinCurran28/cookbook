queue()
   .defer(d3.json, "/recipes/data")
   .await(makeGraphs);
   
function makeGraphs(error, recipesData){
    var ndx = crossfilter(recipesData);
    
    recipesData.forEach(function (d){
        d.calories = parseInt(d.calories);
    });