const messageSubmitBtn = document.querySelector(".submit-message-btn");
const deleteMeassgeBtn = document.querySelector(".delete-message-btn");
const btnContainer = document.querySelector(".for-center");
const searchMemberBtn = document.querySelector(".search-btn");

messageSubmitBtn.addEventListener("click", checkMessage);
searchMemberBtn.addEventListener("click", checkMember);

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

function checkMember(event) {
  event.preventDefault();
  const username = document.getElementById("search_username").value;
  fetch(`http://127.0.0.1:8000/api/member?username=${username}`)
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("Network response was not ok.");
      }
    })
    .then((data) => {
      if (data && data.data) {
        console.log(data);
        document.getElementById(
          "search-result"
        ).innerText = `${data.data.name}(${data.data.username})`;
      } else {
        document.getElementById("search-result").innerText = "無此會員";
      }
    })
    .catch((error) => {
      console.log(`Error: ${error}`);
    });
}

document.addEventListener("DOMContentLoaded", function () {
  const userInfoElement = document.getElementById("user-info");
  const userID = userInfoElement.dataset.userId;
  console.log("User ID from dataset:", userID);

  const updateButton = document.querySelector(".update-name-btn");
  if (updateButton) {
    updateButton.addEventListener("click", function (event) {
      event.preventDefault();
      const newName = document.getElementById("change_name").value;
      updateAllUsernames(newName, userID);
      updateName(newName, userID);
    });
  }
});

function updateAllUsernames(newName, userID) {
  const usernameDisplays = document.querySelectorAll(".username-display");
  if (userID) {
    const userIDStr = userID.toString();
    usernameDisplays.forEach(function (display) {
      if (display.dataset.userId === userIDStr) {
        display.textContent = newName;
      }
    });
  } else {
    console.error("No user ID provided or user ID is undefined.");
  }
}

function updateName(newName, userID) {
  console.log("User ID from dataset:", userID);
  fetch(`http://127.0.0.1:8000/api/member`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name: newName }),
  })
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("Network response was not ok.");
      }
    })
    .then((data) => {
      if (data.ok) {
        console.log(data);
        document.querySelector(
          ".title"
        ).innerText = `嗨！${newName}，歡迎登入系統`;
        document.getElementById("update-result").innerText = "更新成功";
      } else {
        document.getElementById("update-result").innerText = "更新失敗";
      }
    })
    .catch((error) => {
      console.log(`Error: ${error}`);
      document.getElementById("update-result").innerText = "更新失敗";
    });
}
