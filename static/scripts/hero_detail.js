// expand ability when clicked and close others
let items = document.querySelectorAll(".ability-item");

items.forEach(item => {
    item.addEventListener('click', evt => {
        if (item.style.transform !== "scale(1.15)") {
            item.style.zIndex = '10';
            item.style.transform = "scale(1.15)";
            if (item.classList.contains("talents")) {
                item.querySelector("svg path").style.fill = "#FED14C";
            }
        } else {
            item.style.transform = "scale(1)";
            item.style.zIndex = "1";
            if (item.classList.contains("talents")) {
                item.querySelector("svg path").style.fill = "#FFFFFF";
            }
        }

        // unscale other items
        items.forEach(otherItem => {
            if (otherItem !== item) {
                otherItem.style.transform = "scale(1)";
                otherItem.style.zIndex = "1";

                if (otherItem.classList.contains("talents")) {
                    otherItem.querySelector("svg path").style.fill = "#FFFFFF";
                }
            }
        });

        // close other collapsed
        document.querySelectorAll(".hero-info .show").forEach(i => {
            i.classList.remove("show");
        });
        document.querySelector("#collapseTalentTree").classList.remove("show");

        evt.preventDefault();
    });
});
