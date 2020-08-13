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
})
