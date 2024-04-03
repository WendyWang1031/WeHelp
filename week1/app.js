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
