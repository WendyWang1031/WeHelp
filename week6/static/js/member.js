const messageSubmitBtn = document.querySelector(".submit-message-btn");

messageSubmitBtn.addEventListener("click", checkMessage);

function checkMessage(event) {
  const messageInput = document.querySelector("#message_content").value;
  if (messageInput === "") {
    alert("Please enter your message content.");
    event.preventDefault();
    return;
  } else {
    console.log("good job! Message field are filled!");
  }
}
