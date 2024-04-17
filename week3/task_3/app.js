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

function ShortCutString(str, num) {
  if (str.length > num) {
    return str.slice(0, num) + "...";
  } else {
    return str;
  }
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
    let firstImageUrls = data.data.results.map((result) => {
      let filelistString = result.filelist.toLowerCase();
      let urls = filelistString.split(".jpg").map((url) => url.trim() + ".jpg");
      return urls[0];
    });
    let locationNames = data.data.results.map((result) => {
      return result.stitle;
    });

    let promotionImages = document.querySelectorAll(".promotion img");
    promotionImages.forEach((img, index) => {
      if (firstImageUrls[index]) {
        img.src = firstImageUrls[index];
      }
    });

    let promotionTitle = document.querySelectorAll(".promotion > div > div");
    promotionTitle.forEach((title, index) => {
      if (locationNames[index]) {
        title.textContent = ShortCutString(locationNames[index], 7);
      }
    });

    let titleDivsImage = document.querySelectorAll(".title1-area > div");
    titleDivsImage.forEach((div, index) => {
      if (firstImageUrls[index + promotionImages.length]) {
        div.style.backgroundImage = `url(${
          firstImageUrls[index + promotionImages.length]
        })`;
      }
    });

    let titleDivsTitle = document.querySelectorAll(
      ".title1-area > div > span > p "
    );
    titleDivsTitle.forEach((title, index) => {
      if (locationNames[index + promotionTitle.length]) {
        title.textContent = ShortCutString(
          locationNames[index + promotionTitle.length],
          7
        );
      }
    });
  });
