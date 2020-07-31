$(document).ready(function(){
  GetCategory();
});

$("#category").on("change", function(){
  GetSubCategory();
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
      <option value="">Select Sub Category</option>
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
                <input class="form-check-input" type="radio" name="exampleRadios" id="set_home_image`+i+`" value="option1" checked>
                <label class="form-check-label" for="set_home_image`+i+`">Home image</label>
              </div>
              <br />
              <div class="form-group">
                <input type="number" class="form-control" id="inputEmail4" value="`+sl_no+`" placeholder="Serial no.">
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
