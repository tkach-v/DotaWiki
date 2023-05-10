// Filter basic items or neutral-items
document.querySelector(".basic-items").addEventListener('click', evt => {
    document.querySelector('.filter-items-basic').style.display = 'flex';
    document.querySelector('.filter-items-neutral').style.display = 'none';
    document.querySelector('.basic-items').classList.add("clicked");
    document.querySelector('.neutral-items').classList.remove("clicked");
    document.querySelector('.filter-items-basic a').click();


    console.log("FUCK ME")
    evt.preventDefault();
});

document.querySelector(".neutral-items").addEventListener('click', evt => {
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

        evt.preventDefault();
    });
});
