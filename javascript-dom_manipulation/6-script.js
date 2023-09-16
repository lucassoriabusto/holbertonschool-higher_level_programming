const characterElement = document.getElementById("character");

// Hacer una solicitud HTTP GET a la URL usando Fetch API
fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .then((response) => response.json())
  .then((data) => {
    // Extraer el nombre del personaje de la respuesta JSON
    const characterName = data.name;
    // Mostrar el nombre en el elemento HTML con id "character"
    characterElement.textContent = characterName;
  });
