const addItemElement = document.getElementById("add_item")
const ulelemnt = document.querySelector(".my_list")

addItemElement.addEventListener("click", function () {
    const newLi = document.createElement("li")
    newLi.textContent = "Item";
    ulelemnt.appendChild(newLi);
});
