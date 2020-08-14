$(document).ready(function(){
  // alert();
});


function ChangeSlider(slider_type, classname){
  $("#mens_fashion_image").hide();
  $("#womens_fashion_image").hide();
  $("#baby_kid_fashion_image").hide();
  $("#mobile_image").hide();
  $("#electronic_image").hide();
  $("#office_appliance_image").hide();
  $(".fashion_tab").removeClass('active');
  $("."+classname).addClass('active');
  $("#"+slider_type).show();
}
