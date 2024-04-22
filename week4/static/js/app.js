const submitBtn = document.querySelector(".submit-btn");
const agreeCheckBox = document.getElementById("agree-box");

submitBtn.addEventListener("click", checkUserHitBox);
agreeCheckBox.addEventListener("click", checkUserAgree);

function checkUserAgree() {
  if (agreeCheckBox.checked) {
    console.log("agree!");
  } else {
    console.log("no ~ not checked");
  }
}

function checkUserHitBox() {
  if (!agreeCheckBox.checked) {
    alert("Please check the checkbox first");
    event.preventDefault();
    return;
  } else {
    console.log("good job! You agreed!");
  }
}
