$(document).ready(function(){
  $("#search_product_id").on("keyup", function(e){
    let search_value = e.currentTarget.value;
    $(".result_data").html(``);
    if(search_value != ""){
      $(".search_result_div").show();
      $.ajax({
        url: '/site-admin/stock/search-product',
        method: "GET",
        data: {
          "search_keyword": search_value,
          'search_by': "product_id",
        },
        success: function(e){
          e.resp.map((data, key) => {
            // console.log(data);
            Search_result_div(data);
          });
        },
        error: function(e){
          console.log(e);
        }
      });
    }
    else{
      $(".search_result_div").hide();
    }
  });

  $("#search_product_name").on("keyup", function(e){
    let search_value = e.currentTarget.value;
    $(".result_data").html(``);
    if(search_value != ""){
      $(".search_result_div").show();
      $.ajax({
        url: '/site-admin/stock/search-product',
        method: "GET",
        data: {
          "search_keyword": search_value,
          'search_by': "product_name",
        },
        success: function(e){
          e.resp.map((data, key) => {
            // console.log(data);
            Search_result_div(data);
          });
        },
        error: function(e){
          console.log(e);
        }
      });
    }
    else{
      $(".search_result_div").hide();
    }
  });
});

function Search_result_div(data){
  // console.log(data);
  let tertiary_category = "";
  if(data.product_tertiary_category)
    tertiary_category = data.product_tertiary_category;

  var template = `
    <a href="javascript:void(0);" onclick="return ShowProduct('`+data.product_custom_id+`');">
      <div class="col-md-1">
        <img src="/static/site_image/135x180.png" alt="" width='60px' height="80px">
      </div>
      <div class="col-md-3 search_product_details">
        <span>`+data.product_title+`</span>
      </div>
      <div class="col-md-2 search_product_details">
        <span>`+data.product_category+`</span>
      </div>
      <div class="col-md-2 search_product_details">
        <span>`+data.product_sub_category+`</span>
      </div>
      <div class="col-md-2 search_product_details">
        <span>`+tertiary_category+`</span>
      </div>
      <div class="col-md-2 search_product_details">
        <span>`+data.product_seller+`</span>
      </div>
    </a>
  `;

  $(".result_data").append(template);
}

function ShowProduct(product_id){
  $(".search_result_div").hide();
  $(".result_data").html(``);

  // Fetch one product
  $.ajax({
    url: '/site-admin/stock/view-product',
    method: "GET",
    data: {
      "product_id": product_id
    },
    success: function(e){
      // console.log(e);
      e.resp.map((data, key) => {
        PlacedValue(data);
      });
    },
    error: function(e){
      console.log(e);
    }
  });
}

function PlacedValue(data){
  console.log(data);
  $("#product_id").val(data.product_custom_id);
  $("#product_title").val(data.product_title);
  $("#category").val(data.product_category);
  $("#sub_category").val(data.product_sub_category);
  $("#tertiary_category").val(data.product_tertiary_category);
  $("#seller").val(data.product_seller);
  $("#color").val(data.product_color);
  $("#size").val(data.product_size);
  $("#made_in").val(data.product_made_in);
}


$("#stock_submit").on('submit', function(){
  if($("#product_id").val() == ""){
    alert("Product not choose")
    return false;
  }
  if($("#stock_qty").val() == ""){
    alert("Add stock")
    return false;
  }
  if($("#main_price").val() == ""){
    alert("Add main price")
    return false;
  }
  if($("#offer_price").val() == ""){
    alert("Add offer price")
    return false;
  }
  if($("#purchase").val() == ""){
    alert("Add purchase price")
    return false;
  }
  return true;
});
