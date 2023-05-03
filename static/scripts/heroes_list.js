// search for heroes
document.querySelector(".search-heroes input").addEventListener('keyup', evt => {
    const userText = evt.target.value.toLowerCase();
    let countMatch = 0;

    if (userText !== '') {
        document.querySelectorAll(".heroes-list > .col-lg-2").forEach(i => {
            if (i.querySelector(".hero-name").innerHTML.toLowerCase().indexOf(userText) > -1) {
                i.style.display = "";
                countMatch += 1;
            } else {
                i.style.display = "none";
            }
            if (countMatch < 10) {
                document.querySelector(".heroes-list").style.marginBottom = "40vh";
            }
        });
        if (countMatch === 0) {
            document.querySelector("#no-hero-match").style.opacity = "1";
        } else {
            document.querySelector("#no-hero-match").style.opacity = "0";
        }
    } else {
        document.querySelectorAll(".heroes-list > *").forEach(i => {
            i.style.display = "";
        });
    }

    evt.preventDefault();
});

document.querySelector(".search-heroes a").addEventListener('click', evt => {
    document.querySelectorAll(".heroes-list > *").forEach(i => {
        i.style.display = "";
    });
    document.querySelector("#no-hero-match").style.opacity = "0";
    evt.preventDefault();
});

// filter attributes
document.querySelectorAll(".attribute a").forEach(a => {
    a.addEventListener('click', evt => {
        // style clicked
        if (a.classList.contains("clicked")) {
            a.classList.remove('clicked');
        } else {
            a.classList.add('clicked');

            // delete styles for others
            document.querySelectorAll(".attribute a").forEach(otherLink => {
                if (otherLink !== a) {
                    otherLink.classList.remove('clicked');
                }
            });
        }
        evt.preventDefault();
    });
});


// filter complexity
lstComplexity = document.querySelectorAll(".complexity a");
for (let i = 0; i < lstComplexity.length; i++) {
    lstComplexity[i].addEventListener('click', evt => {
        if (lstComplexity[i].classList.contains('chosen')) {
            lstComplexity[i].classList.remove('chosen');
            lstComplexity[0].innerHTML = "<img src=\"/static/images/heroes_list/complexity_empty.svg\">";
            lstComplexity[1].innerHTML = "<img src=\"/static/images/heroes_list/complexity_empty.svg\">";
            lstComplexity[2].innerHTML = "<img src=\"/static/images/heroes_list/complexity_empty.svg\">";
        } else {
            if (lstComplexity[i].id === 'complexity_1') {
                lstComplexity[0].classList.add('chosen');
                lstComplexity[1].classList.remove('chosen');
                lstComplexity[2].classList.remove('chosen');
                lstComplexity[0].innerHTML = "<img src=\"/static/images/heroes_list/complexity_full.svg\">";
                lstComplexity[1].innerHTML = "<img src=\"/static/images/heroes_list/complexity_empty.svg\">";
                lstComplexity[2].innerHTML = "<img src=\"/static/images/heroes_list/complexity_empty.svg\">";
            } else if (lstComplexity[i].id === 'complexity_2') {
                lstComplexity[0].classList.remove('chosen');
                lstComplexity[1].classList.add('chosen');
                lstComplexity[2].classList.remove('chosen');
                lstComplexity[0].innerHTML = "<img src=\"/static/images/heroes_list/complexity_full.svg\">";
                lstComplexity[1].innerHTML = "<img src=\"/static/images/heroes_list/complexity_full.svg\">";
                lstComplexity[2].innerHTML = "<img src=\"/static/images/heroes_list/complexity_empty.svg\">";
            } else {
                lstComplexity[0].classList.remove('chosen');
                lstComplexity[1].classList.remove('chosen');
                lstComplexity[2].classList.add('chosen');
                lstComplexity[0].innerHTML = "<img src=\"/static/images/heroes_list/complexity_full.svg\">";
                lstComplexity[1].innerHTML = "<img src=\"/static/images/heroes_list/complexity_full.svg\">";
                lstComplexity[2].innerHTML = "<img src=\"/static/images/heroes_list/complexity_full.svg\">";
            }
        }

        evt.preventDefault();
    });
}



