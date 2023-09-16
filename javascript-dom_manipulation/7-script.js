const listMoviesElement = document.getElementById("list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then((response) => response.json())
  .then((data) => {
    // Obtiene la lista de películas desde la respuesta JSON
    const movies = data.results;

    // Itera a través de cada película y crea un elemento de lista para cada título
    movies.forEach((movie) => {
      const movieTitle = movie.title;
      const listItem = document.createElement("li");
      listItem.textContent = movieTitle;

      // Agrega el elemento de lista a la lista de películas
      listMoviesElement.appendChild(listItem);
    });
  });
