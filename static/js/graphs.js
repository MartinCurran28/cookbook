queue()
   .defer(d3.json, "/recipes/data")
   .await(makeGraphs);
   
function makeGraphs(error, recipesData){
    var ndx = crossfilter(recipesData);
    
//   recipesData.forEach(function (d){
//       d.calories = parseInt(d.calories);
//   });
   
   show_category_total(ndx);
   show_recipes_total(ndx);
   
   dc.renderAll();
}
   
function show_category_total(ndx){
    
    var category_dim = ndx.dimension(dc.pluck("category_name"));
    var total_category = category_dim.group();
    
    dc.pieChart("#total-categories")
      .height(300)
      .radius(120)
      .transitionDuration(1500)
      .dimension(category_dim)
      .group(total_category);
    
}   

function show_recipes_total(ndx){
    
    var recipes_dim = ndx.dimension(dc.pluck("recipe_name"));
    var total_recipes = recipes_dim.group();
    
    dc.pieChart("#total-recipes")
      .height(300)
      .radius(120)
      .transitionDuration(1500)
      .dimension(recipes_dim)
      .group(total_recipes);
    
}   