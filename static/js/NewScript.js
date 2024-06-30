const chatInput = document.getElementById("input-msg");
const sendChatbtn = document.querySelector(".chat-input span");
const chatbox = document.getElementById("msg-chat");
const mode = document.getElementById("btnchange");
const checkBox = document.querySelector("input[type=checkbox]");

let userMessage;
//


function onch(){
  if (checkBox.checked == true){
      document.body.style.backgroundImage = "url('static/images/backgrounddark.jpg')";
      document.getElementById("user").style.color = "#fff";
      document.getElementsByClassName("chatbot")[0].style.backgroundColor = "#000";
      document.getElementsByClassName("chat-input")[0].style.backgroundColor = "#000";
      document.getElementById("input-msg").style.backgroundColor="#000"
      document.getElementById("input-msg").style.color="#fff"
  } else {
      document.body.style.backgroundImage = "url('static/images/backgroundlight.jpg')";
      document.getElementById("user").style.color = "#000";
      document.getElementsByClassName("chatbot")[0].style.backgroundColor = "#fff";
      document.getElementsByClassName("chat-input")[0].style.backgroundColor = "#fff";
      document.getElementById("input-msg").style.backgroundColor="#fff"
      document.getElementById("input-msg").style.color="#000"
  }
  console.log("btn clk"); 
}
checkBox.addEventListener('click',onch())

//add login and register page prompt user to login if not exist register save their details
const createChatLi = (message, className) =>{





    const chatLi = document.createElement("li");
    chatLi.classList.add("chat",className);
    let chatContent = className ==="outgoing" ? `<p>${message}</p>`: `<span class="material-symbols-outlined">smart_toy</span><p>${message}</p>`;
    chatLi.innerHTML = chatContent;
    return chatLi;
} 



const handleChat = ()=>{
    userMessage= chatInput.value;
    console.log(userMessage)
    if(!userMessage) return;
    var dataD=" "
    chatbox.appendChild(createChatLi(userMessage,"outgoing"))
    fetch('', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({
          'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
          'message': userMessage
        })
      })
        .then(response => response.json())
        .then( data => {
          const res = data.response;
          console.log("Tag : ",res[1]);
          
          console.log("full msg :",res);
          console.log("msg : ",res[0]);
          chatbox.appendChild(createChatLi(res[0],"incoming"))

          if(res[1]){
           // console.log("schoolar detected");
          }
          setTimeout(()=>{
            
            if(res[1]=="login"){
              console.log("redirecting to login");
              window.location.replace("http://127.0.0.1:8000/login");
            }else if(res[1]=="register"){
              console.log("redirecting to register");
              window.location.replace("http://127.0.0.1:8000/register");
            }else if(res[1]=="holiday"){
                chatbox.appendChild(createChatLi(data.holidays,"incoming"))
                //console.log(data.holidays[i][0] ,data.holidays[i][1]);
            }else if(res[1]=="resultall"){
                chatbox.appendChild(createChatLi(data.result,"incoming"))
            }else if(res[1]=="resultme"){
                chatbox.appendChild(createChatLi(data.result,""))
            }else if(res[1]=="complaint"){
              chatInput.value="subject : complaint\nMessage :"
            }else if(res[1]=="schoolarshipadd"){
                chatbox.appendChild(createChatLi("Choose schoolarship from above","incoming"))
                chatbox.appendChild(createChatLi("I will fill rest of your details","incoming"))
                chatInput.value="schoolarship name : "
            }else if(res[1]=="resetpass"){
              
            }else if(res[1]=="getpass"){
              chatInput.value="password : "
            }else if(res[1]=="suggestion"){
              chatInput.value="Suggestion : "
            }else if(res[1]=="issue"){
              chatInput.value="Issue : "
            }else if(res[9]=="fascility"){ 

              for(var b = 1;b<res.length-1;b++){            

                chatbox.appendChild(createChatLi(res[b],"incoming"));
        
                console.log(res[b]);                
              }
           
            }else if(res[1]=="imagegallery"){ 
                      
              window.location.replace("http://127.0.0.1:8000/gallery")
           
            }else if(res[1]=="chmode"){ 
              console.log(document.getElementsByClassName("chatbot")[0].style.backgroundColor);
                if(document.getElementsByClassName("chatbot")[0].style.backgroundColor=="rgb(255, 255, 255)"){
                  document.body.style.backgroundImage = "url('static/images/backgrounddark.jpg')";
                  document.getElementById("user").style.color = "#fff";
                  document.getElementsByClassName("chatbot")[0].style.backgroundColor = "#000";
                  document.getElementsByClassName("chat-input")[0].style.backgroundColor = "#000";
                  document.getElementById("input-msg").style.backgroundColor="#000"
                  document.getElementById("input-msg").style.color="#fff"
                
                }else{
                  document.body.style.backgroundImage = "url('static/images/backgroundlight.jpg')";
                  document.getElementById("user").style.color = "#000";
                  document.getElementsByClassName("chatbot")[0].style.backgroundColor = "#fff";
                  document.getElementsByClassName("chat-input")[0].style.backgroundColor = "#fff";
                  document.getElementById("input-msg").style.backgroundColor="#fff"
                  document.getElementById("input-msg").style.color="#000"
                }
                  
                
                
              
                  
                
            }else if(res[1]=="lightmode"){ 
              if(document.getElementsByClassName("chatbot")[0].style.backgroundColor!="rgb(255, 255, 255)"){
                document.body.style.backgroundImage = "url('static/images/backgroundlight.jpg')";
                document.getElementById("user").style.color = "#000";
                document.getElementsByClassName("chatbot")[0].style.backgroundColor = "#fff";
                document.getElementsByClassName("chat-input")[0].style.backgroundColor = "#fff";
                document.getElementById("input-msg").style.backgroundColor="#fff"
                document.getElementById("input-msg").style.color="#000"
                
              }else{
                chatbox.appendChild(createChatLi("Already on light mode","incoming"));

              }
              
            }else if(res[1]=="darkmode"){ 
              if(document.getElementsByClassName("chatbot")[0].style.backgroundColor=="rgb(255, 255, 255)"){
                document.body.style.backgroundImage = "url('static/images/backgrounddark.jpg')";
                document.getElementById("user").style.color = "#fff";
                document.getElementsByClassName("chatbot")[0].style.backgroundColor = "#000";
                document.getElementsByClassName("chat-input")[0].style.backgroundColor = "#000";
                document.getElementById("input-msg").style.backgroundColor="#000"
                document.getElementById("input-msg").style.color="#fff"
              }else{
                
                chatbox.appendChild(createChatLi("Already on dark mode","incoming"));
              }
            }else if(res[1]=="feedback"){
              chatInput.value="Feedback : "
              console.log("setting text");
            }
            
          },1000)
          

          
        });
    
    
    //message to be generate
    
    
    chatInput.value="";
    

}

sendChatbtn.addEventListener("click",handleChat)


window.addEventListener('load', function() {
    console.log("Window loading");
    this.setTimeout(()=>{
      chatbox.appendChild(createChatLi("Hii there 👋","incoming"))
      this.setTimeout(()=>{
        chatbox.appendChild(createChatLi("How can I help you today?","incoming"))
      },1000);
    },500)
   
})
