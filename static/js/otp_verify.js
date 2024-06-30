const btn = document.getElementById("btn");
const otp_input = document.getElementById("otp")
const handleChat = ()=>{
    const otp = otp_input.value;
    fetch('', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({
          'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
          'otp':otp
        })
      })
        .then(response => response.json())
        .then( data => {
          const res = data.response;
          console.log("server : ",res[0]);
          if(res[0]=="true"){
            window.location.replace("http://127.0.0.1:8000/create")
          }else{
            window.location.replace("http://127.0.0.1:8000/otpverify")
          }
         
})
}

btn.addEventListener("click",handleChat);

