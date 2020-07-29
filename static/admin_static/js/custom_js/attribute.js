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
