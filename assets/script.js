
function getColors() {
    r = Math.random() * 256;
    g = Math.random() * 256;
    b = Math.random() * 256;

    let emph = `rgb(${r}, ${g}, ${b})`;
    let darker = `rgb(${r-10}, ${g-10}, ${b-10})`;
    return [emph, darker]
}

let root = document.documentElement;

let change = document.createElement("div");
change.setAttribute("id", "selector");
change.innerText = "Some text";
document.body.appendChild(change);


change.addEventListener("click", (ev) => {
    let colors = getColors();
    root.style.setProperty("--emph", colors[0]);
    root.style.setProperty("--emph-darker", colors[1]);
});



// --emph: #ff5800;
// --emph-rgb: rgb(255, 88, 0);
// --emph-darker: rgb(195, 38, 0);


