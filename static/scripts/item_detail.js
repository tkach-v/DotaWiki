// do connections in recipe
function draw() {
    const horizontalWidth = otherImages[0].offsetWidth * (otherImages.length - 1);

    document.querySelector('.connection').style.width = horizontalWidth + 'px';
}

const otherImages = document.querySelectorAll('.other-item-image');

if (otherImages.length === 0) {
    document.querySelector('.connection').style.display = 'none';
} else if (otherImages.length === 1) {
    document.querySelector('.connect-horizontal').style.borderBottom = '0';
    document.querySelector('.connect-main').style.height = '24px';
    document.querySelector('.connect-others').style.display = 'none';
} else if (otherImages.length === 2) {
    draw();
} else if (otherImages.length === 3) {
    draw();
    document.querySelector(".connect-others").innerHTML = "<div class='col-6 p-0'></div><div class='col-6 p-0'></div>";
    document.querySelector(".connect-others .col-6").style.borderRight = "3px solid #FFFFFF";
} else if (otherImages.length === 4) {
    draw();
    document.querySelector(".connect-others").innerHTML = "<div class='col-4 p-0'></div><div class='col-4 p-0'></div><div class='col-4 p-0'></div>";
    let cols = document.querySelectorAll(".connect-others .col-4");
    cols[0].style.borderRight = "3px solid #FFFFFF";
    cols[1].style.borderRight = "3px solid #FFFFFF";
} else if (otherImages.length === 5) {
    draw();
    document.querySelector(".connect-others").innerHTML = "<div class='col-3 p-0'></div><div class='col-3 p-0'></div><div class='col-3 p-0'></div><div class='col-3 p-0'></div>";
    let cols = document.querySelectorAll(".connect-others .col-3");
    cols[0].style.borderRight = "3px solid #FFFFFF";
    cols[1].style.borderRight = "3px solid #FFFFFF";
    cols[2].style.borderRight = "3px solid #FFFFFF";
} else {
    draw()
}

// fix infobox when scrolled (not for phones)


const abilities = document.querySelectorAll('.item-ability');
if (window.screen.width >= 768 && abilities.length) {
(".item-infobox").offsetHeight;
    let elem = document.querySelector(".item-infobox");
    let elemWidth = elem.offsetWidth;
    let elemHeight = elem.offsetHeight;

    const minScroll = document.querySelector(".col-md-5").offsetTop;
    const maxScroll = document.querySelector(".item-abilities").offsetHeight + minScroll - 51 - 21 - elemHeight;


    elem.style.width = elemWidth + "px";
    // elem.style.height = elemHeight + "px";

    console.log(minScroll);
    console.log(maxScroll);


    (function () {
        window.onscroll = () => {
            console.log(window.scrollY)
            if (window.scrollY > (minScroll - 51)) {
                elem.classList.add('item-infobox-fixed');

                if (window.scrollY <= maxScroll) {
                    elem.style.top = window.scrollY - minScroll + 51 + "px"
                } else {
                    // elem.classList.remove('item-infobox-fixed');
                    elem.style.top = maxScroll - minScroll + 51 + "px"
                    // elem.style.top = null;
                }

            } else {
                elem.classList.remove('item-infobox-fixed');
                elem.style.top = "0";
            }
        };
    }());
}
