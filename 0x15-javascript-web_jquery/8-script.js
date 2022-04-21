$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (json) {
  for (const film of json.results) {
    $('ul#list_movies').append('<li>' + film.title + '</li>');
  }
});
