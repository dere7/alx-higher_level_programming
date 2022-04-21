$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (json) {
  $('div#character').text(json.name);
});
