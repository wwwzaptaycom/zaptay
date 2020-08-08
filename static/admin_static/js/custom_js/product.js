$(document).ready(function(){
  GetCategory();
  Color();
  Size();
  MadeIn();
  Seller();
});

$("#category").on("change", function(){
  GetSubCategory();
  GetCategoryTable();
});
$("#sub_category").on("change", function(){
  TertiaryCategory();
})

function GetCategory(){
  $.ajax({
    url: "http://127.0.0.1:8000/site-admin/attribute/get-cateory",
    method: "GET",
    dataType: "JSON",

    success: function(r){
      let html_content = `
        <option value="">Select Category</option>
      `;
      r.data.map((category, key) => {
          html_content+= `<option value="`+category[0]+`">`+category[1]+`</option>`
      })
      $("#category").html(html_content);
    },
    error: function(r){
      console.log(r);
    }
  });
}

function GetSubCategory(){
  $.ajax({
    url: "http://127.0.0.1:8000/site-admin/attribute/get-sorted-sub-category",
    method: "GET",
    dataType: "JSON",
    data:{
      category_id: $("#category").val()
    },
    success: function(r){
      let html_content = `
      <option value="">Select Sub Category</option>
      `;
      r.data.map((category, key) => {
        html_content+= `<option value="`+category[0]+`">`+category[1]+`</option>`
      })
      $("#sub_category").html(html_content);
    },
    error: function(r){
      console.log(r);
      }
  });
}

function TertiaryCategory(){
  $.ajax({
    url: "http://127.0.0.1:8000/site-admin/attribute/get-sorted-terti-category",
    method: "GET",
    dataType: "JSON",
    data:{
      sub_category_id: $("#sub_category").val()
    },
    success: function(r){
      let html_content = `
      <option value="">Select Tertiary Category</option>
      `;
      r.data.map((category, key) => {
        html_content+= `<option value="`+category[0]+`">`+category[1]+`</option>`
      })
      $("#ter_category").html(html_content);
    },
    error: function(r){
      console.log(r);
      }
  });
}

function Color(){
  $.ajax({
    url: "http://127.0.0.1:8000/site-admin/attribute/get-all-color",
    method: "GET",
    dataType: "JSON",
    success: function(r){
      let html_content = `
      <option value="">Select Color</option>
      `;
      r.data.map((category, key) => {
        html_content+= `<option value="`+category[0]+`">`+category[1]+`</option>`
      })
      $("#color").html(html_content);
    },
    error: function(r){
      console.log(r);
      }
  });
}

function Size(){
  $.ajax({
    url: "http://127.0.0.1:8000/site-admin/attribute/get-all-size",
    method: "GET",
    dataType: "JSON",
    success: function(r){
      let html_content = `
      <option value="">Select Size</option>
      `;
      r.data.map((category, key) => {
        html_content+= `<option value="`+category[0]+`">`+category[1]+`</option>`
      })
      $("#size").html(html_content);
    },
    error: function(r){
      console.log(r);
      }
  });
}

function MadeIn(){
  $.ajax({
    url: "http://127.0.0.1:8000/site-admin/attribute/get-all-made-in",
    method: "GET",
    dataType: "JSON",
    success: function(r){
      let html_content = `
      <option value="">Select Made By</option>
      `;
      r.data.map((category, key) => {
        html_content+= `<option value="`+category[0]+`">`+category[1]+`</option>`
      })
      $("#made_in").html(html_content);
    },
    error: function(r){
      console.log(r);
      }
  });
}

function Seller(){
  $.ajax({
    url: "http://127.0.0.1:8000/site-admin/seller/get-all-seller/",
    method: "GET",
    dataType: "JSON",
    success: function(r){
      let html_content = '';
      console.log(r);
      r.data.map((category, key) => {
        html_content+= `<option value="`+category['seller_id']+`">`+category['seller_name']+`</option>`
      })
      $("#seller").append(html_content);
    },
    error: function(r){
      console.log(r);
      }
  });
}

// Pincode add for delivary charges
/*$("#pincode_add").on("click", function(){
  let template = `
  <div class="form-group col-md-3">
    <div class="card">
      <div class="card-header">
        <div class="form-group">
          <input type="number" class="form-control" name="pincode[]" id="chaeges" placeholder="Enter The Pincode">
        </div>
      </div>
      <div class="card-body">
        <div class="form-group">
          <label for="chaeges">Charge rate</label>
          <input type="number" class="form-control" name="pincode_charge[]" id="chaeges" placeholder="Enter the charge" value="0">
        </div>
      </div>
    </div>
  </div>
  `;
  $("#add_more_pin_codes_div").append(template);
});*/

/* ******************************************************* Image preview ******************************************************* */

$("#product_img").on('change', function(){
  let div_prepare = '';
  let count = document.getElementById("product_img").files.length;
  let sl_no = 0;
  for(i=0; i<count; i++){
    sl_no = i+1;
    // console.log(event.target.files[i])
    // console.log(URL.createObjectURL(event.target.files[i]));
    // $("#show").append("<img src='"+URL.createObjectURL(event.target.files[i])+"'><br>")
    div_prepare+=`
      <div class="form-group col-md-2">
        <div class="card" style="width: 10rem;">
          <img class="card-img-top" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap" style="width: 100%; height: 180px;">
          <div class="card-body">
            <div class="card-text">
              <div class="form-check">
                <input class="form-check-input" type="radio" name="product_home_image" id="set_home_image`+i+`" value="option1" checked>
                <label class="form-check-label" for="set_home_image`+i+`">Home image</label>
              </div>
              <br />
              <div class="form-group">
                <input type="number" class="form-control" name="product_sl_image[]" id="inputEmail4" value="`+sl_no+`" placeholder="Serial no.">
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
  }
  $("#show_upload_image").html(div_prepare);
});

/* ******************************************************* /Image preview ******************************************************* */


/* ****************************************************** Product List ********************************************************** */
$("#clear_filter").on('click', function(){
  document.location.reload();
});

function GetCategoryTable(){
  var table_content = `
    <tr>
      <th scope="row">1</th>
        <td>Category sort</td>
        <td>Otto</td>
        <td>250</td>
        <td>25</td>
        <td>--</td>
        <td>
          <a href="javascript:void(0);" class="btn btn-info btn-sm">
          <i class="fas fa-eye"></i>
          View
          </a>
          <a href="javascript:void(0);" class="btn btn-warning btn-sm">
          <i class="fas fa-edit"></i>
          Edit
          </a>
      </td>
    </tr>
  `;
  $("#table_content").html(table_content);
}
/* ****************************************************** /Product List ********************************************************** */
