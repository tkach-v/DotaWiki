// do slider for full screen images and do adaptive for it
const sliderLinks = document.querySelectorAll(".slide .poster__link");
let currentSlide = "creeps";

if (window.innerWidth < 950) {
    document.querySelector(".section").style.height = document.querySelector(`#${currentSlide}`).offsetHeight + "px";
}

sliderLinks.forEach(a => {
    a.addEventListener('click', evt => {
        if (a.textContent.toLowerCase() === "creeps") {
            document.querySelector(`#${currentSlide}`).classList.remove("active");
            document.querySelector("#creeps").classList.add("active");
            currentSlide = "creeps";
        } else if (a.textContent.toLowerCase() === "items") {
            document.querySelector(`#${currentSlide}`).classList.remove("active");
            document.querySelector("#items").classList.add("active");
            currentSlide = "items";
        } else if (a.textContent.toLowerCase() === "heroes") {
            document.querySelector(`#${currentSlide}`).classList.remove("active");
            document.querySelector("#heroes").classList.add("active");
            currentSlide = "heroes";
        } else {
            document.querySelector(`#${currentSlide}`).classList.remove("active");
            document.querySelector("#mechanics").classList.add("active");
            currentSlide = "mechanics";
        }

        if (window.innerWidth < 950) {
            document.querySelector(".section").style.height = document.querySelector(`#${currentSlide}`).offsetHeight + "px";
        }

        evt.preventDefault()
    });
});
