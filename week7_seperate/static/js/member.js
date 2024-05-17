const messageSubmitBtn = document.querySelector(".submit-message-btn");
const deleteMeassgeBtn = document.querySelector(".delete-message-btn");
const btnContainer = document.querySelector(".for-center");
const searchMemberBtn = document.querySelector(".search-btn");
const searchResult = document.getElementById("search-result");
const welcomeTitle = document.querySelector(".title");
const welcomeMessage = document.getElementById("welcome-message");
const updateNameResult = document.getElementById("update-result");
const messageContainer = document.querySelector(".for-center");
const messageElement = document.createElement("section");
const formElement = document.createElement("form");

messageSubmitBtn.addEventListener("click", checkMessage);
searchMemberBtn.addEventListener("click", checkMember);

document.addEventListener("DOMContentLoaded", getUserInfo);
document.addEventListener("DOMContentLoaded", showMessage);

if (btnContainer) {
  btnContainer.addEventListener("click", function (event) {
    if (event.target.classList.contains("delete-message-btn")) {
      checkDeleteMessage(event);
    }
  });
}

function getUserInfo() {
  fetch(`http://127.0.0.1:8000/api/user`)
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("Network response was not ok.");
      }
    })
    .then((data) => {
      welcomeMessage.textContent = `Hi！${data.user_name}，歡迎登入系統`;
    })
    .catch((error) => {
      console.log("Failed to fetch user:", error);
      console.log(`Error: ${error}`);
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
    insertMessage();
  }
}

function showMessage() {
  fetch(`http://127.0.0.1:8000/api/member`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        return response.json().then((data) => {
          throw new Error(data.message || "Unknown Error");
        });
      }
    })
    .then((data) => {
      if (data.success) {
        console.log(data);
        messageContainer.innerHTML = "";
        data.message.forEach((message) => {
          let messageElement = document.createElement("div");
          messageElement.className = "show-message-area";
          let messageContent = document.createElement("div");
          messageContent.className = "show-message-content";
          let messageForm = document.createElement("form");
          messageForm.className = "leave-message";
          messageForm.innerHTML = `
          
            <span class="username-display" data-user-id="${message.message_id}">
            ${message.name}
            </span>：${message.content}
            <input type="hidden" name="message_id" value="${message.message_id}">
            <button type="submit" class="delete-message-btn">X</button>
            
          `;

          messageElement.appendChild(messageForm);
          messageContainer.appendChild(messageElement);
        });
      } else {
        messageContainer.innerText = "無留言顯示";
      }
    })
    .catch((error) => {
      console.log(`Error: ${error}`);
    });
}

function insertMessage() {
  fetch(`http://127.0.0.1:8000/api/message`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message_content: messageContent }),
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
        messageContainer.innerHTML = "";
        data.forEach((message) => {
          messageElement.className = "show-message-area";
          message.innerHTML = `
          <div class = "show-message-content">
            <span class="username-display" data-user-id="${message.message_id}">
            ${message.name}
            </span>：${message.content}
            </div>
          `;
          if (message.message_id === YOUR_USER_ID_VARIABLE) {
            formElement.setAttribute("method", "POST");
            formElement.innerHTML = `
            <input type="hidden" name="message_id" value="${message.message_id}">
            <button type="submit" class="delete-message-btn">X</button>
            `;
            messageElement.appendChild(formElement);
          }
          messageContainer.appendChild(messageElement);
        });
      }
    })
    .catch((error) => {
      console.log(`Error: ${error}`);
    });
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
  fetch(`http://127.0.0.1:8000/api/member_username?username=${username}`)
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        return response.json().then((data) => {
          throw new Error(data.message || "Unknown Error");
        });
      }
    })
    .then((data) => {
      if (data && data.data) {
        console.log(data);
        console.log("Member founded");
        searchResult.innerText = `${data.data.name}(${data.data.username})`;
      } else {
        searchResult.innerText = "無此會員";
      }
    })
    .catch((error) => {
      console.log(`Error: ${error}`);
      searchResult.innerText = error.message;
    });
}

document.addEventListener("DOMContentLoaded", function () {
  const userInfoElement = document.getElementById("user-info");
  const userID = userInfoElement.dataset.userId;
  const updateButton = document.querySelector(".update-name-btn");
  console.log("User ID from dataset:", userID);

  if (updateButton) {
    updateButton.addEventListener("click", function (event) {
      event.preventDefault();
      const newName = document.getElementById("change_name").value;
      if (newName) {
        updateAllUsernames(newName, userID);
        updateName(newName, userID);
      } else {
        alert("Please enter a valid name.");
        updateNameResult.innerText = "請輸入可使用的名字";
      }
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
        return response.json().then((data) => {
          throw new Error(data.message || "Unknown Error");
        });
      }
    })
    .then((data) => {
      if (data.success) {
        console.log(data);
        welcomeTitle.innerText = `嗨！${newName}，歡迎登入系統`;
        updateNameResult.innerText = "更新成功";
      } else {
        updateNameResult.innerText = "更新失敗";
      }
    })
    .catch((error) => {
      console.log(`Error: ${error}`);
      updateNameResult.innerText = error.message;
    });
}
