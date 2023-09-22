$(document).ready(function () {
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function (data) {
      // Mostrar la traducción en el elemento <div id="hello">
      $("#hello").text(data.hello);
    });
  });
