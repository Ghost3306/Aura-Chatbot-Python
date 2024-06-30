const loginbtn = document.getElementById("submitbtn");
const username = document.getElementById("user")
const passw = document.getElementById("pass")

var user = username.value;
var pass = passw.value;
console.log(user,pass);
fetch('', {
  method: 'POST',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  body: new URLSearchParams({
    'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
    'usern': user,'passn':pass
  })
  })
    .then(response => response.json())
    .then( data => {
      
      console.log(data.message);
        
        

        
      });
  


