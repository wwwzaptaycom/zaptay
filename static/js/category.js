function ProductFetch(tertiary_category_id, tertiary_category_name){
  console.log(tertiary_category_id, tertiary_category_name);
  $.ajax({
    url: "/category/get-product/",
    method: "GET",
    data:{
      "tertiary_id": tertiary_category_id,
      "tertiary_name": tertiary_category_name
    },
    success: function(e){
      // console.log(e);
      ViewHtml(e.resp);
    },
    error: function(e){
      console.log(e);
    }
  });
}


function ViewHtml(product_details){
  var template = ``;
  product_details.map((data, slno) => {
    console.log(data);
    template += `
      <div class="product_lists">
        <a href="/product/`+data.id+`">
          <div class="product_image">
            <img src="/media/`+data.image_path+`" alt="`+data.image_title+`">
          </div>
          <div class="product_details">
            <div>`+data.name+`</div>
            <div class="price">
              <span class="sale_price"><i class="fa fa-inr" aria-hidden="true"></i> `+data.product_offer_price+`</span>
              <span class="original"><i class="fa fa-inr" aria-hidden="true"></i> `+data.product_main_price+`</span>
            </div>
            <div class="offer">
              <span class="percent">`+data.product_price_off_percent+`% off</span>
              <span class="save">Save `+data.product_price_save+`</span>
            </div>
            <div class="cart_wishlist">
              <button type="button" name="button"><i class="fa fa-heart-o" aria-hidden="true"></i></button>
              <button type="button" name="button"><i class="fa fa-shopping-cart" aria-hidden="true"></i></button>
            </div>
          </div>
        </a>
      </div>
    `
  });
  $(".products").html(template);
}
