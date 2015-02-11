$(document).ready(function(){
   var id = $("#id_product_category").val();
   $("#id_product_category").load("/catalog/ajax/all_categories/?id=" + id);
});