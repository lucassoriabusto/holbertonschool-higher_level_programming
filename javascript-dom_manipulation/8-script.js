document.addEventListener("DOMContentLoaded", function () {
    const helloElement = document.getElementById("hello");
  
    fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
      .then((response) => response.json())
      .then((data) => {
        // Obtiene la traducción de "hello" desde la respuesta JSON
        const translation = data.hello;
  
        // Muestra la traducción en el elemento HTML con id "hello"
        helloElement.textContent = translation;
      });
    });
