const reader = new FileReader();

$("#submit").on("click",()=>{
  const file = document.getElementById('pictureInput').files[0];
  
  //file's loaded
  reader.addEventListener("load", function () {
    console.log(reader.result);
  }, false);

  //load file to reader
  reader.readAsDataURL(file);

});