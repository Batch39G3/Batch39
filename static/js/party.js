let i = 1;
let body = document.getElementsByTagName("body")[0];

for (i; i <= 20; i++) {
    let button = document.createElement("button");
    button.innerHTML = 'Button ' + i;
    body.appendChild(button);
    button.addEventListener("click", function() {
        alert(this.innerHTML);
    });
}