const container = document.querySelector("#container");

const content = document.createElement("div");
content.classList.add("content");
content.textContent = "This is the glorious text-content!";
container.appendChild(content);


const paragraph = document.createElement("p");
paragraph.setAttribute("style", "color: red;");
paragraph.textContent = "Hey I'm red!";
container.appendChild(paragraph);

const h3 = document.createElement("h3");
h3.setAttribute("style", "color: blue;");
h3.textContent = "I'm a blue h3!";
container.appendChild(h3);

const div = document.createElement("div");
const h1 = document.createElement("h1");
h1.textContent = "I'm in a div";
const p = document.createElement("p");
p.textContent = "ME TOO!";
div.appendChild(h1);
div.appendChild(p);
container.appendChild(div);

const btn = document.querySelector("#btn");
btn.addEventListener("click", (e) => {
    console.log(e.target);
    e.target.style.background= "blue";
    alert("Goodbye World");
});

