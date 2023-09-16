const toggleHeaderElement = document.getElementById('toggle_header');
const headerElement = document.querySelector('header');

toggleHeaderElement.addEventListener('click', function () {
    // Usa classList.toggle() para alternar entre las clases "red" y "green"
    headerElement.classList.toggle('red');
    headerElement.classList.toggle('green');
});
