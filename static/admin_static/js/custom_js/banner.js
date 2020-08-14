$(document).ready(function(){
  // alert();
});

$("#men_banner_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("men_banner_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#men_upload_preview").html(prepare_div);
});

$("#women_banner_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("women_banner_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#women_upload_preview").html(prepare_div);
});

/*  BAby & Kids  */

$("#baby_kid_banner_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("baby_kid_banner_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#baby_kid_upload_preview").html(prepare_div);
});

/*  Mobile  */

$("#mobile_banner_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("mobile_banner_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#mobile_upload_preview").html(prepare_div);
});

/*  Electronics  */

$("#electronics_banner_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("electronics_banner_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#electronics_upload_preview").html(prepare_div);
});

/*  Office Appliance  */

$("#office_appliance_banner_img").on('change', function(){
  var prepare_div = ``;
  let count = document.getElementById("office_appliance_banner_img").files.length;
  prepare_div+=`<div class="form-group col-md-12">Image preview</div>`;
  for(i=0; i<count; i++){
    prepare_div+=`
      <div class="form-group col-md-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" style="height: 110px;" src="`+URL.createObjectURL(event.target.files[i])+`" alt="Card image cap">
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="form-group">
                  <input type="link" name="banner_link" class="form-control" id="banner_link" placeholder="Link">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    `
  }
  $("#office_appliance_upload_preview").html(prepare_div);
});
