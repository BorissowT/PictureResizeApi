const reader = new FileReader();

$("#submit").on("click",()=>{
  const file = document.getElementById('pictureInput').files[0];

  //file's loaded
  reader.addEventListener("load", function () {
    var result = reader.result.split(",");
    send_ajax_with_image(result[1]);
  }, false);

  function send_ajax_with_image(image){
    
    var json = `{"image":"${image}"}`;
    $.ajax({
      type:'POST',
      url: '/api/',
      headers: {
                    "Content-Type": "application/json"
                },
      data: json
    }).done(function() {
      console.log("done")
    }).fail(function(e) {
      console.log(e);
    });
  }
  //load file to reader
  reader.readAsDataURL(file);

});