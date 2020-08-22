$(document).ready(function(){
  $.ajax({
    url: "http://127.0.0.1:8000/site-admin/attribute/get-cateory",
    method: "GET",
    dataType: "JSON",

    success: function(r){
      let html_content = `
        <option value="">Select Category</option>
      `;

      // let da = r.map((data, key)=> {
      //   console.log(data);
      // });
      // console.log(r.data);
      r.data.map((category, key) => {
          html_content+= `<option value="`+category[0]+`">`+category[1]+`</option>`
          // console.log(category, key)
      })
      $("#id_category_list").html(html_content);
      // console.log(html_content);
    },
    error: function(r){
      console.log(r);
    }
  });


  $.ajax({
    url: "http://127.0.0.1:8000/site-admin/attribute/get-sub-cateory",
    method: "GET",
    dataType: "JSON",

    success: function(r){
      let html_content = `
        <option value="">Select Sub Category</option>
      `;
      // console.log(r.data);
      r.data.map((category, key) => {
          html_content+= `<option value="`+category[0]+`">`+category[1]+`</option>`
          // console.log(category, key)
      })
      $("#id_sub_category_list").html(html_content);
      // console.log(html_content);
    },
    error: function(r){
      console.log(r);
    }
  });
});

function delete_attributes(attribute_type, attribute_name, id){
  let message = 'Confirm delete '+ attribute_type +': '+ attribute_name;
  let conf = confirm(message);
  if(conf){
    var token = $("input[name=csrfmiddlewaretoken]").val();
    console.log(attribute_type, id);

    $.ajax({
      url: "http://127.0.0.1:8000/site-admin/attribute/delete-attributes/",
      method: "POST",
      dataType: "JSON",
      data: {
        'attribute_type': attribute_type,
        'attribute_id': id,
        'csrfmiddlewaretoken': token
      },
      success: function(r){
        console.log(r);
        if(r.response == "success"){
          return true;
        }
      },
      error: function(r){
        console.log(r);
      }
    });
    // return true;
  }
  else{
      return false;
  }
}


function show_image_modal(category_type, category_id){
  // console.log(category_type, category_id);
  $(".model_form_content").hide();
  $('#exampleModalCenter').modal('show');
  $("#exampleModalLongTitle").text(category_type);

  $.ajax({
    url: "/site-admin/attribute/get-subcategory-details",
    method: "GET",
    data: {
      "sub_category_id": category_id
    },
    success: function(e){
      // console.log(e);
      $(".model_form_content").show();
      $(".modal_loader").hide();
      $(".category_name").val(e.sub_category_name);
    },
    error: function(e){
      console.log(e);
    }
  });
}

$("#customFileLang").on("change", function(){
  let image = `<img class="card-img-top" src="`+URL.createObjectURL(event.target.files[0])+`" alt="Card image cap" style="width: 150px; height: 250px;">`;
  $(".preview_img").html(image);
  /*var file = this.files;
  console.log(file);*/
});

$("#attribute_image").on('submit', function(e){
  /*e.preventDefault();
  $form = $(this)
  var formData = new FormData(this);
  console.log(formData);*/
  var file = document.getElementById('customFileLang').files[0];
  console.log(file);
  $.ajax({
    url: "/site-admin/attribute/subcategory-image/",
    method: "POST",
    data:{
      "image": file
    },
    success: function(e){
      console.log(e);
    },
    error: function(e){
      console.log(e);
    }
  });
  return false;
});
