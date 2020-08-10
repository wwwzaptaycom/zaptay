$(document).ready(function(){
  get_category()
  // get_seller()
});

$("#category").on("change", function(e){
  GetSearch_product();
  get_sub_category();
});

$("#sub_category").on('change', function(){
  GetSearch_product();
  get_tertiary_category();
});

$("#ter_category").on("change", function(){
  GetSearch_product();
});

$("#search_product_number").on("keyup", function(e){
  let search_value = e.currentTarget.value;
  $.ajax({
    url: "http://127.0.0.1:8000/site-admin/product/search-product-id/",
    method: "GET",
    dataType: "JSON",
    data:{
      search_key: search_value
    },
    success: function(resp){
      console.log(resp);
      var table_content = '';
      if(resp.resp.length != 0){
        resp.resp.map((data, key) => {
          // console.log(data);
          table_content+= `
            <tr>
              <th scope="row">${key+1}</th>
                <td>${data.create_date}</td>
                <td style="font-size: 14px; font-weight: 700;">${data.prod_custom_id}</td>
                <td>${data.prod_title}</td>
                <td>${data.prod_category}</td>
                <td>--</td>
                <td>
                  <a href="/site-admin/product/${data.prod_custom_id}" class="btn btn-info btn-sm">
                  <i class="fas fa-eye"></i>
                  View
                  </a>
                  <a href="javascript:void(0);" class="btn btn-warning btn-sm">
                  <i class="fas fa-edit"></i>
                  Edit
                  </a>
              </td>
            </tr>`;
        });
        $("#table_content").html(table_content);
      }
      else{
        table_content+= `
          <tr>
            <td colspan="7" style="text-align: center;">No product found</td>
          </tr>`;
        $("#table_content").html(table_content);
      }
    },
    error: function(resp){
      console.log(resp);
    }
  });
});

function get_category(){
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

function get_sub_category(){
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
      if(r.response != "Failed"){
        r.data.map((category, key) => {
          html_content+= `<option value="`+category[0]+`">`+category[1]+`</option>`
        })
        $("#sub_category").html(html_content);
      }
      else{
        $("#sub_category").html(`<option value="">Select Category First</option>`);
        $("#ter_category").html(`<option value="">Select Sub Category First</option>`);
      }
    },
    error: function(r){
      console.log(r);
      }
  });
}

function get_tertiary_category(){
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
      if(r.response != "Failed"){
        r.data.map((category, key) => {
          html_content+= `<option value="`+category[0]+`">`+category[1]+`</option>`
        })
        $("#ter_category").html(html_content);
      }
      else{
        $("#ter_category").html(`<option value="">Select Sub Category First</option>`);
      }
    },
    error: function(r){
      console.log(r);
      }
  });
}

$("#clear_filter").on('click', function(){
  document.location.reload();
});

function GetSearch_product(){
  let get_category_id = get_sub_category_id = get_tertiary_id = '';

  get_category_id = $("#category").val();
  get_sub_category_id = $("#sub_category").val();
  get_tertiary_id = $("#ter_category").val();

  var table_content = '';

  $.ajax({
    url: "http://127.0.0.1:8000/site-admin/product/search-product",
    method: "GET",
    dataType: "JSON",
    data:{
      category_id: get_category_id,
      sub_category_id: get_sub_category_id,
      tertiary_category_id: get_tertiary_id,
    },
    success: function(resp){
      console.log(resp);
      if(resp.resp.length != 0){
        resp.resp.map((data, key) => {
          // console.log(data);
          table_content+= `
            <tr>
              <th scope="row">${key+1}</th>
                <td>${data.create_date}</td>
                <td style="font-size: 14px; font-weight: 700;">${data.prod_custom_id}</td>
                <td>${data.prod_title}</td>
                <td>${data.prod_category}</td>
                <td>--</td>
                <td>
                  <a href="/site-admin/product/${data.prod_custom_id}" class="btn btn-info btn-sm">
                  <i class="fas fa-eye"></i>
                  View
                  </a>
                  <a href="javascript:void(0);" class="btn btn-warning btn-sm">
                  <i class="fas fa-edit"></i>
                  Edit
                  </a>
              </td>
            </tr>`;
        });
        $("#table_content").html(table_content);
      }
      else{
        table_content+= `
          <tr>
            <td colspan="7" style="text-align: center;">No product found</td>
          </tr>`;
        $("#table_content").html(table_content);
      }
    },
    error: function(resp){
      console.log(resp);
    }
  })

  $("#table_content").html(table_content);
}
