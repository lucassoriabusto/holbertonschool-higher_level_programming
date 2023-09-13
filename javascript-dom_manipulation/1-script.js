const redheaderElement = document.getElementById('red_header');

redheaderElement.addEventListener('click', function () {
    const headerElement = document.querySelector('header');
    headerElement.style.color = '#FF0000';
});