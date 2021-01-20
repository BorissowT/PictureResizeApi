const reader = new FileReader();

$("#submit").on("click",()=>{
  const file = document.getElementById('pictureInput').files[0];
  if(!file){
    alert("choose a picture");
    location.reload();
  }
  //file's loaded
  reader.addEventListener("load", function () {
    var result = reader.result.split(",");
    var width = $('#width').val();
    var height = $("#height").val();

    if (Number.isInteger(parseInt(width)) && Number.isInteger(parseInt(height))
        && width > 1
        && height > 1
        && width < 2000
        && height < 2000
    ) {
      send_ajax_with_image(result[1], width, height);
    }
    else{
      alert("width and height has to be more than 1px and less than 2000px");
      location.reload();
    }
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
      console.log("Operation's id is:", request.getResponseHeader('identifier'));
      alert(`Operation's id is: ${request.getResponseHeader('identifier')}`);
      window.location.href = `result?id=${request.getResponseHeader('identifier')}`;
    }).fail(function(e) {
      console.log(e);
    });
  }
  //load file to reader
  reader.readAsDataURL(file);

});