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
  let form = event.target.closest("form");
  console.log("Form found:", form);
  console.log("Form action:", form ? form.action : "No action");
  console.log("Form method:", form ? form.method : "No method");
  console.log(
    "message_id value:",
    form
      ? form.querySelector('input[name="message_id"]').value
      : "No message_id"
  );
  if (confirm("Are you sure you want to delete the message?")) {
    console.log("Submittimg form...");
    if (form) {
      form.submit();
      console.log("Ready to submit");
    } else {
      console.log("No form found.");
    }
  } else {
    console.log("Deletion cancelled");
  }
}
