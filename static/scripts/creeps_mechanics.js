let acc = document.querySelectorAll(".table-title");

for (let i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("table-title-active");
        let panel = this.nextElementSibling;
        console.log(panel)
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}