const messageSubmitBtn = document.querySelector(".submit-message-btn");
const deleteMeassgeBtn = document.querySelector(".delete-message-btn");
const btnContainer = document.querySelector(".for-center");

messageSubmitBtn.addEventListener("click", checkMessage);

if (btnContainer) {
  btnContainer.addEventListener("click", function (event) {
    if (event.target.classList.contains("delete-message-btn")) {
      checkDeleteMessage(event);
    }
  });
}

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

function checkDeleteMessage(event) {
  event.preventDefault();
  if (confirm("Are you sure you want to delete the message?") == true) {
    console.log("Yes,delete");
  } else {
    console.log("Nooooo!");
  }
}
