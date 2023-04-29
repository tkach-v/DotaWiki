// search styling
document.querySelectorAll(".search input").forEach(i => {
    i.addEventListener('keyup', evt => {
        if (i.value !== "") {
            i.parentElement.querySelector("a i").style.display = 'block';
        } else {
            i.parentElement.querySelector("a i").style.display = 'none';
        }


        evt.preventDefault();
    });
});

document.querySelectorAll(".search a").forEach(x => {
    x.addEventListener('click', evt => {
        x.parentElement.parentElement.querySelector("input").value = '';
        x.querySelector("i").style.display = 'none';
        evt.preventDefault();
    });
});


const header = document.querySelector('nav');
// colorize navbar and add x when it is expanded
let nav_expanded = false;
const toggler = document.querySelector(".navbar-toggler");

toggler.addEventListener('click', evt => {
    if (nav_expanded) {
        toggler.innerHTML = "<i class=\"fa-solid fa-bars fa-xl\"></i>";
        if (window.scrollY < 40 && document.querySelector("title").text === "DotaWiki") {
            setTimeout(() => {
                header.classList.remove('header-dark')
            }, 250);
        }
        document.querySelector('body').style.overflow = 'visible';
        nav_expanded = false;
    } else {
        toggler.innerHTML = "<i class=\"fa-solid fa-x fa-lg\"></i>";
        header.classList.add('header-dark');
        document.querySelector('body').style.overflow = 'hidden';
        nav_expanded = true;
    }
    document.querySelector("body").style.pointerEvents = "none";

    setTimeout(() => {
        document.querySelector("body").style.pointerEvents = "auto";
    }, 350);
    evt.preventDefault();
});

// close navbar when clicked outside of it
document.onclick = evt => {
    if (document.getElementById("navbarSupportedContent").classList.contains("show") && (!evt.target.closest("nav"))) {
        document.querySelector(".navbar-toggler").click();
    }
};

// configure up-button to scroll up when it clicked
document.querySelector(".up-button").addEventListener("click", evt => {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

    evt.preventDefault();
});

// show up button when user scroll more than 50px and colorize navbar (on main page) and always colorize it when not
(function () {
    window.onscroll = () => {
        if (window.scrollY > 50) {
            document.querySelector(".up-button").style.display = "block";
            header.classList.add('header-dark');
        } else {
            document.querySelector(".up-button").style.display = "none";

            if (document.querySelector("title").text === "DotaWiki") {
                header.classList.remove('header-dark');
            }
        }
    };
    if (document.querySelector("title").text !== "DotaWiki") {
        header.classList.add('header-dark');
    }
}());
