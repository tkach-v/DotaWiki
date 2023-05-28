// clear input
document.querySelector('.form-x').addEventListener('click', evt => {
    document.querySelector(".searchpage-search input").value = "";
    evt.preventDefault();
});

// add margin when not much content
if (window.screen.width >= 768 && document.querySelectorAll(".search-result").length < 3) {
    document.querySelector(".search-results").style.marginBottom = "35vh";
}
