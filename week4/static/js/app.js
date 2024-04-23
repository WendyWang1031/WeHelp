const submitBtn = document.querySelector(".submit-btn");
const agreeCheckBox = document.getElementById("agree-box");
const calBtn = document.querySelector(".cal-btn");

submitBtn.addEventListener("click", checkUserHitBox);
agreeCheckBox.addEventListener("click", checkUserAgree);
document.addEventListener("DOMContentLoaded", (event) => {
  calBtn.addEventListener("click", checkCalculate);
});

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

function checkCalculate(event) {
  const inputNumber = document.getElementById("number").value;
  let number = parseInt(inputNumber);
  if (number < 0 || isNaN(number)) {
    alert("Please enter a positive number");
    event.preventDefault();
    return;
  }

  window.location.href = `/square/${number}`;
}
