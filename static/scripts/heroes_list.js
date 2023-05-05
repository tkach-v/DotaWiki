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


function getHeroes(complexity, primaryAbility) {

    const url = new URL(window.location.href);
    if (complexity) {
        url.searchParams.set("complexity", complexity);
    }
    if (primaryAbility) {
        url.searchParams.set("primary_ability", primaryAbility);
    }

    fetch(url, {
        headers: {
            "X-Requested-With": "XMLHttpRequest",
        }
    })
        .then(response => response.json())
        .then(data => {
            const heroesList = document.querySelector(".heroes-list");
            heroesList.innerHTML = "<h1 id=\"no-hero-match\">No Heroes match your filter</h1>";

            (data.context).forEach(hero => {
                const heroHTMLElement = `
                <div class="col-6 col-md-3 col-lg-2 p-0 pe-3 pb-3">
                    <a class="d-flex flex-column" href="{% url 'hero:hero_list' %}">
                        <img class="img-fluid" src="/media/${hero.image_url_small}" alt="${hero.name}">
                        <div class="hero-name">${hero.name}</div>
                    </a>
                </div>
                `
                heroesList.innerHTML += heroHTMLElement;
            });
        });
}

// add filter to heroes page
const heroURL = "{% url 'hero:hero_list' %}";

// filter attributes
document.querySelectorAll(".attribute a").forEach(a => {
    a.addEventListener('click', evt => {



        // style clicked
        if (a.classList.contains("clicked")) {
            a.classList.remove('clicked');
            getHeroes(null, null);
        } else {
            getHeroes(null, a.querySelector("p").innerText);
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
            lstComplexity[0].innerHTML = "<img src=\"/static/images/heroes_list/complexity_empty.svg\" alt='comlexity_1'>";
            lstComplexity[1].innerHTML = "<img src=\"/static/images/heroes_list/complexity_empty.svg\" alt='comlexity_2'>";
            lstComplexity[2].innerHTML = "<img src=\"/static/images/heroes_list/complexity_empty.svg\" alt='comlexity_3'>";
            getHeroes(null, null);
        } else {
            if (lstComplexity[i].id === 'complexity_1') {
                lstComplexity[0].classList.add('chosen');
                lstComplexity[1].classList.remove('chosen');
                lstComplexity[2].classList.remove('chosen');
                lstComplexity[0].innerHTML = "<img src=\"/static/images/heroes_list/complexity_full.svg\" alt='comlexity_1'>";
                lstComplexity[1].innerHTML = "<img src=\"/static/images/heroes_list/complexity_empty.svg\" alt='comlexity_2'>";
                lstComplexity[2].innerHTML = "<img src=\"/static/images/heroes_list/complexity_empty.svg\" alt='comlexity_3'>";
                getHeroes(1, null);
            } else if (lstComplexity[i].id === 'complexity_2') {
                lstComplexity[0].classList.remove('chosen');
                lstComplexity[1].classList.add('chosen');
                lstComplexity[2].classList.remove('chosen');
                lstComplexity[0].innerHTML = "<img src=\"/static/images/heroes_list/complexity_full.svg\" alt='comlexity_1'>";
                lstComplexity[1].innerHTML = "<img src=\"/static/images/heroes_list/complexity_full.svg\" alt='comlexity_2'>";
                lstComplexity[2].innerHTML = "<img src=\"/static/images/heroes_list/complexity_empty.svg\" alt='comlexity_3'>";
                getHeroes(2, null);
            } else {
                lstComplexity[0].classList.remove('chosen');
                lstComplexity[1].classList.remove('chosen');
                lstComplexity[2].classList.add('chosen');
                lstComplexity[0].innerHTML = "<img src=\"/static/images/heroes_list/complexity_full.svg\" alt='comlexity_1'>";
                lstComplexity[1].innerHTML = "<img src=\"/static/images/heroes_list/complexity_full.svg\" alt='comlexity_2'>";
                lstComplexity[2].innerHTML = "<img src=\"/static/images/heroes_list/complexity_full.svg\" alt='comlexity_3'>";
                getHeroes(3, null);
            }
        }

        evt.preventDefault();
    });
}



