const registerSubmitBtn = document.querySelector(".submit-btn");
const signInBtn = document.querySelector(".log-in-btn");

registerSubmitBtn.addEventListener("click", checkRegisterUser);

function checkRegisterUser() {
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
    console.log("good job! You agreed!");
  }
}
