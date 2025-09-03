// Loader
window.addEventListener("load", function () {
  setTimeout(function () {
    document.getElementById("loader").style.opacity = "0";
    setTimeout(function () {
      document.getElementById("loader").style.display = "none";
    }, 500);
  }, 1000);
});

// Back to top button
const backToTopButton = document.getElementById("backToTop");

window.addEventListener("scroll", function () {
  if (window.pageYOffset > 300) {
    backToTopButton.classList.add("visible");
  } else {
    backToTopButton.classList.remove("visible");
  }
});

backToTopButton.addEventListener("click", function () {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
});