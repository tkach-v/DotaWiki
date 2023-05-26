// Async function for getting items from db
function getItems(typeGlobal, typeSpecific) {
    const url = new URL(window.location.href);

    url.searchParams.set("type-global", typeGlobal);
    url.searchParams.set("type-specific", typeSpecific);


    fetch(url, {
        headers: {
            "X-Requested-With": "XMLHttpRequest",
        }
    })
        .then(response => response.json())
        .then(data => {
            const itemsList = document.querySelector(".items-list > .row");
            itemsList.innerHTML  = "";

            (data.context).forEach(item => {
                console.log(item.id)

                const itemHTMLElement = `
                <div class="col-6 col-md-3 col-xl-2 m-0 p-0 pe-3 pb-3">
                    <div class="item py-3 px-auto">
                        <a href="${item.slug}">
                            <div class="row m-0">
                                <div class="col-6 d-flex justify-content-end">
                                    <img class="img-fluid" src="/media/${item.image_url}" alt="Item image">
                                </div>
                                ${item.cost ? `
                                    <div class="col-6 d-flex align-items-center justify-content-start">
                                        <span class="price pe-2">${item.cost}</span>
                                        <img src="/static/images/items_list/coin.png" alt="Coin">
                                    </div>
                                ` : `
                                    <div class="col-6 d-flex align-items-center justify-content-start">
                                        <span class="price pe-2">${item.specific_name}</span>
                                    </div>
                                `}
                            </div>
                            <div class="item-name pt-3 px-2">
                                <span>${item.name}</span>
                            </div>
                        </a>
                    </div>
                </div>        
                `
                itemsList.innerHTML += itemHTMLElement;
            });
        });
}

let chosenTypeGlobal = 'Basics';
let chosenTypeSpecific = 'All';


// Filter basic items or neutral-items
document.querySelector(".basic-items").addEventListener('click', evt => {
    chosenTypeGlobal = 'Basics';
    document.querySelector('.filter-items-basic').style.display = 'flex';
    document.querySelector('.filter-items-neutral').style.display = 'none';
    document.querySelector('.basic-items').classList.add("clicked");
    document.querySelector('.neutral-items').classList.remove("clicked");
    document.querySelector('.filter-items-basic a').click();
    evt.preventDefault();
});

document.querySelector(".neutral-items").addEventListener('click', evt => {
    chosenTypeGlobal = 'Neutral';
    document.querySelector('.filter-items-basic').style.display = 'none';
    document.querySelector('.filter-items-neutral').style.display = 'flex';
    document.querySelector('.neutral-items').classList.add("clicked");
    document.querySelector('.basic-items').classList.remove("clicked");
    document.querySelector('.filter-items-neutral a').click();
    evt.preventDefault();
});


// filter additional items
additionalFilterItems = document.querySelectorAll('.addition-filter .col-6 a')

additionalFilterItems.forEach(i => {
    i.addEventListener('click', evt => {
        i.classList.add('clicked');

        additionalFilterItems.forEach(otherItem => {
            if (otherItem !== i) {
                otherItem.classList.remove('clicked')
            }
        });

        chosenTypeSpecific = i.textContent.trim();
        getItems(chosenTypeGlobal, chosenTypeSpecific);
        evt.preventDefault();
    });
});
