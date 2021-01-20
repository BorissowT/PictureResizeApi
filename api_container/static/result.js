var url_string = window.location.href;
var url = new URL(url_string);
var id = url.searchParams.get("id");
request_for_the_picture(id);


function request_for_the_picture(id){
      $.ajax({
        type: 'GET',
        url: `/api/${id}`,
        headers: {
          "Content-Type": "application/json"
        },
      }).done(function (data) {
        if (data['status']){
          console.log("in process...")
          setTimeout(function (){
            console.log("sending again");
            request_for_the_picture(id  );
                    },4000);

        }
        else {
          console.log(data['image']);
          var image = new Image();
          image.src = `data:image/png;base64,${data['image']}`;
          document.body.appendChild(image);
          $("#status").remove();
          $(document.body).append(`<div><a download=\"${data["identifier"]}.PNG\" href=\"data:image/png;base64,${data['image']}\">Download</a></div>`);
        }
      });

  }