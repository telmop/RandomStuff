function createGrid(side) {
    const container = document.querySelector(".container");
    for (let i = 0; i < side; i++) {
        container.appendChild(createRow(side));
    }
    addSquareEventListeners();
}

function createRow(side) {
    const row = document.createElement("div");
    row.classList.add("row");
    for (let i = 0; i < side; i++) {
        const element = document.createElement("div");
        element.classList.add("square");
        element.classList.add("square-0");
        row.appendChild(element);
    }
    return row;
}

createGrid(16);

const button = document.querySelector(".new-grid-button");
button.addEventListener("click", () => {
    let gridSize = parseInt(prompt("Desired grid size [1-100]:"));
    if (gridSize < 1 || gridSize > 100 || isNaN(gridSize)) {
        console.log("Invalid grid size");
        gridSize = 16;
    }
    // Remove previous grid.
    const container = document.querySelector(".container");
    container.innerHTML = "";

    createGrid(gridSize);
});


function addSquareEventListeners() {
    const squares = document.querySelectorAll(".square");
    squares.forEach((square) => {
        square.addEventListener("click", (e) => {
            // Dumb as hell, but works.
            if (e.target.classList.contains("square-0")) {
                e.target.classList.remove("square-0");
                e.target.classList.add("square-1");
            } else if (e.target.classList.contains("square-1")) {
                e.target.classList.remove("square-1");
                e.target.classList.add("square-2");
            } else if (e.target.classList.contains("square-2")) {
                e.target.classList.remove("square-2");
                e.target.classList.add("square-3");
            } else if (e.target.classList.contains("square-3")) {
                e.target.classList.remove("square-3");
                e.target.classList.add("square-4");
            } else if (e.target.classList.contains("square-4")) {
                e.target.classList.remove("square-4");
                e.target.classList.add("square-5");
            } else if (e.target.classList.contains("square-5")) {
                e.target.classList.remove("square-5");
                e.target.classList.add("square-6");
            } else if (e.target.classList.contains("square-6")) {
                e.target.classList.remove("square-6");
                e.target.classList.add("square-7");
            } else if (e.target.classList.contains("square-7")) {
                e.target.classList.remove("square-7");
                e.target.classList.add("square-8");
            } else if (e.target.classList.contains("square-8")) {
                e.target.classList.remove("square-8");
                e.target.classList.add("square-9");
            } else if (e.target.classList.contains("square-9")) {
                e.target.classList.remove("square-9");
                e.target.classList.add("square-10");
            }
        });
    });
}

