$(document).ready(function(){
  // alert();
});


function ChangeSlider(slider_type, classname){
  $("#mens_fashion_image").hide();
  $("#womens_fashion_image").hide();
  $(".fashion_tab").removeClass('active');
  $("."+classname).addClass('active');
  $("#"+slider_type).show();
}
