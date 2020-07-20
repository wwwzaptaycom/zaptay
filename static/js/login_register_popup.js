$(document).ready(function(){
  $(".login").on('click', function(){
    $(".my_login_modal_div").css("display", "flex");
  });

  $(".login_close").on("click", function(){
    $(".my_login_modal_div").css("display", "none");
  });

  $(".register").on("click", function(){
    $(".my_reg_modal_div").css("display", "flex");
  });

  $(".reg_close").on("click", function(){
    $(".my_reg_modal_div").css("display", "none");
  });
});
