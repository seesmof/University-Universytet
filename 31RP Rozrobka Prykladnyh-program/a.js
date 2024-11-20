var search_bar = document.querySelector("#q");
document.addEventListener("keydown", function (event) {
  if (event.ctrlKey && event.key === " ") {
    window.scrollTo(0, 0);
    search_bar.focus();
  }
});
