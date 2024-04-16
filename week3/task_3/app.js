const mobileMenu = document.querySelector(".mobile-menu");
const nav = document.querySelector(".navbar-nav");
const closeBtn = document.querySelector(".close-btn");

mobileMenu.addEventListener("click", listExpended);
function listExpended() {
  nav.classList.add("expanded");
}

closeBtn.addEventListener("click", listClose);
function listClose() {
  nav.classList.remove("expanded");
}

const url =
  "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1";

fetch(url)
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok!");
    }
    return response.json();
  })
  .then((data) => {
    console.log(data);
  });
