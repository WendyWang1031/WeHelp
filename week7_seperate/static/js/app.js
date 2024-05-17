document.addEventListener("DOMContentLoaded", function () {
  const loginForm = document.querySelector(".log-in");
  const signupForm = document.querySelector(".input-area");

  signupForm.addEventListener("submit", function (event) {
    checkRegisterUser(event, this);
  });
  loginForm.addEventListener("submit", function (event) {
    checkUserState(event, this);
  });
});

function checkRegisterUser(event, form) {
  event.preventDefault();
  const name = form.querySelector("#name").value;
  const registerUsername = form.querySelector("#register-username").value;
  const registerPassword = form.querySelector("#register-password").value;

  if (name === "" || registerUsername === "" || registerPassword === "") {
    alert("Please enter your name , username and password.");

    return;
  } else {
    signup(form);
    console.log("good job! All field are filled!");
  }
}

function checkUserState(event, form) {
  event.preventDefault();
  const usernameInput = document.querySelector("#username").value;
  const passwordInput = document.querySelector("#password").value;
  if (usernameInput === "" || passwordInput === "") {
    alert("Please enter your username and password.");
    return;
  } else {
    login(form);
    console.log("good job! All field are filled!");
  }
}

function signup(form) {
  const name = form.querySelector("#name").value;
  const registerUsername = form.querySelector("#register-username").value;
  const registerPassword = form.querySelector("#register-password").value;
  const registerHint = document.querySelector(".register-hint");
  fetch("http://127.0.0.1:8000/api/signup", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: name,
      username: registerUsername,
      password: registerPassword,
    }),
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
        console.log("Registration successful");
        registerHint.innerText = "成功註冊會員，請在下方登入會員頁面";
        form.reset();
      } else {
        console.error("Registration failed: " + data.message);
        registerHint.innerText = data.message;
      }
    })

    .catch((error) => {
      console.log(`Error: ${error}`);
      registerHint.innerText = error.message;
    });
}

function login(form) {
  console.log("test whether inside....");
  const usernameInput = form.querySelector("#username").value;
  const passwordInput = form.querySelector("#password").value;
  fetch("http://127.0.0.1:8000/api/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username: usernameInput,
      password: passwordInput,
    }),
  })
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("Network response was not ok.");
      }
    })

    .then((data) => {
      if (data.success) {
        console.log("Login successful");
        console.log(data);
        window.location.href = data.redirect;
      } else {
        console.error("Login failed" + data.message);
      }
    })

    .catch((error) => {
      console.log(`Error: ${error}`);
      console.error("Login failed:" + (error.message || "Unknown error"));
    });
}
