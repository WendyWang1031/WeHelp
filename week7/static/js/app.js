const registerSubmitBtn = document.querySelector(".submit-btn");
const logInBtn = document.querySelector(".log-in-btn");

registerSubmitBtn.addEventListener("click", checkRegisterUser);
logInBtn.addEventListener("click", checkUserState);

function checkRegisterUser(event) {
  const register_nameInput = document.querySelector("#name").value;
  const register_usernameInput =
    document.querySelector("#register-username").value;
  const register_passwordInput =
    document.querySelector("#register-password").value;
  if (
    register_nameInput === "" ||
    register_usernameInput === "" ||
    register_passwordInput === ""
  ) {
    alert("Please enter your name , username and password.");
    event.preventDefault();
    return;
  } else {
    console.log("good job! All field are filled!");
  }
}

function checkUserState(event) {
  const usernameInput = document.querySelector("#username").value;
  const passwordInput = document.querySelector("#password").value;
  if (usernameInput === "" || passwordInput === "") {
    alert("Please enter your username and password.");
    event.preventDefault();
    return;
  } else {
    console.log("good job! All field are filled!");
  }
}
