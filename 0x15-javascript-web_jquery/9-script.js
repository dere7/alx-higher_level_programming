$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (json) {
  $('div#hello').text(json.hello);
});
