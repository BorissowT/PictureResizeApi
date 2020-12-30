const reader = new FileReader();

$("#submit").on("click",()=>{
  const file = document.getElementById('pictureInput').files[0];

  //file's loaded
  reader.addEventListener("load", function () {
    var result = reader.result.split(",");
    var width = $('#width').val()
    var height = $("#height").val()
    send_ajax_with_image(result[1], width, height);
  }, false);

  function send_ajax_with_image(image, width, height){
    
    var json = `{"image":"${image}", "width":"${width}", "height":"${height}"}`;
    $.ajax({
      type:'POST',
      url: '/api/',
      headers: {
                    "Content-Type": "application/json"
                },
      data: json
    }).done(function(data, textStatus, request) {
      console.log(request.getResponseHeader('id'))
    }).fail(function(e) {
      console.log(e);
    });
  }
  //load file to reader
  reader.readAsDataURL(file);

});