const mobileMenu = document.querySelector(".mobile-menu");
const nav = document.querySelector(".navbar-nav");
const closeBtn = document.querySelector(".close-btn");
const loadMoreBtn = document.getElementById("loadMoreBtn");
const btnArea = document.getElementById("btn-area");
window.addEventListener("resize", function () {
  updateTextContent();
});
mobileMenu.addEventListener("click", listExpended);
function listExpended() {
  nav.classList.add("expanded");
}

closeBtn.addEventListener("click", listClose);
function listClose() {
  nav.classList.remove("expanded");
}

loadMoreBtn.addEventListener("click", loadMoreContent);

let allImageUrls = [];
let allLocationNames = [];
let currentIndex = 13;
function shortCutString(text, num, maxWidth, element) {
  const elementWidth = element.clientWidth;

  if (elementWidth < maxWidth && text.length > num) {
    return text.slice(0, num) + "...";
  } else {
    return text;
  }
}
window.addEventListener("resize", function () {
  applyTextShortening();
});
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
    allImageUrls = data.data.results.map((result) => {
      let filelistString = result.filelist.toLowerCase();
      let urls = filelistString.split(".jpg").map((url) => url.trim() + ".jpg");
      return urls[0];
    });
    allLocationNames = data.data.results.map((result) => {
      return result.stitle;
    });

    let promotionImages = document.querySelectorAll(".promotion img");
    promotionImages.forEach((img, index) => {
      if (allImageUrls[index]) {
        img.src = allImageUrls[index];
      }
    });

    let promotionTitle = document.querySelectorAll(".promotion > div > div");
    promotionTitle.forEach((title, index) => {
      if (allLocationNames[index]) {
        title.textContent = allLocationNames[index];
      }
    });

    let titleDivsImage = document.querySelectorAll(".title1-area > div");
    titleDivsImage.forEach((div, index) => {
      if (allImageUrls[index + promotionImages.length]) {
        div.style.backgroundImage = `url(${
          allImageUrls[index + promotionImages.length]
        })`;
      }
    });

    let titleDivsTitle = document.querySelectorAll(
      ".title1-area > div > span > p "
    );
    titleDivsTitle.forEach((title, index) => {
      if (allLocationNames[index + promotionTitle.length]) {
        const fullText = allLocationNames[index + promotionTitle.length];
        const shortCutText = shortCutString(fullText, 6, 200, title);
        title.textContent = shortCutText;
      }
    });
    console.log(currentIndex);
  });

// function loadMoreContent() {
//   const original = document.querySelector(".whole-main-title1-area");
//   const clone = original.cloneNode(true);
//   btnArea.parentNode.insertBefore(clone, btnArea);

//   const clonedImages = clone.querySelectorAll(".title1-area > div");
//   const clonedTitles = clone.querySelectorAll(
//     ".promotion > div > div, .title1-area > div > span > p"
//   );
//   const allCurrentImages = document.querySelectorAll(".title1-area > div");
//   const allCurrentTitles = document.querySelectorAll(
//     ".whole-main-title1-area .promotion > div > div, .whole-main-title1-area .title1-area > div > span > p"
//   );
//   const newStartIndex =
//     allCurrentImages.length -
//     clone.querySelectorAll(".title1-area > div").length;

//   clonedImages.forEach((div, index) => {
//     const imageIndex = newStartIndex + index;
//     if (imageIndex < allImageUrls.length) {
//       div.style.backgroundImage = `url(${allImageUrls[imageIndex]})`;
//     }
//   });
//   clonedTitles.forEach((title, index) => {
//     const titleIndex = newStartIndex + index;
//     if (titleIndex < allLocationNames.length) {
//       const fullText = allLocationNames[titleIndex];
//       const shortCutText = shortCutString(fullText, 6, 200, title);
//       title.textContent = shortCutText;
//     }
//   });

//   currentIndex += newStartIndex + clonedImages.length + clonedTitles.length;
// }

function loadMoreContent() {
  const btnArea = document.getElementById("btn-area");
  const newMainTitleArea = document.createElement("section");
  const newTitleArea = document.createElement("section");
  newMainTitleArea.className = "whole-main-title1-area";
  newTitleArea.className = "title1-area";

  let endIndex = Math.min(currentIndex + 10, allImageUrls.length);
  let countOfElementsToCreate = endIndex - currentIndex;

  for (let i = 0; i < 10; i++) {
    const actualIndex = currentIndex + i;
    const newDiv = document.createElement("div");
    newDiv.className = `title${i + 1}`;
    if (i < countOfElementsToCreate) {
      newDiv.style.backgroundImage = `url(${allImageUrls[actualIndex]})`;

      const newImg = document.createElement("img");
      newImg.src = "./images/star_icon.svg";
      newImg.alt = "";

      const newSpan = document.createElement("span");
      const newP = document.createElement("p");
      const fullText = allLocationNames[actualIndex];
      const shortCutText = shortCutString(fullText, 6, 200, newP);
      newP.textContent = shortCutText;

      newSpan.appendChild(newP);
      newDiv.appendChild(newImg);
      newDiv.appendChild(newSpan);
    } else {
      newDiv.visibility = "hidden";
      newDiv.style.backgroundImage = "none";
    }

    newTitleArea.appendChild(newDiv);
  }

  newMainTitleArea.appendChild(newTitleArea);
  btnArea.parentNode.insertBefore(newMainTitleArea, btnArea);
  currentIndex = endIndex;
  if (currentIndex >= allImageUrls.length) {
    if (loadMoreBtn) {
      loadMoreBtn.style.display = "none";
    }
  }
}
