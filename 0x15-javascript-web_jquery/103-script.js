function hello () {
  $.getJSON(
    'https://fourtonfish.com/hellosalut/',
    { lang: $('input#language_code').val() },
    function (json) {
      $('div#hello').text(json.hello);
    }
  );
}

$(function () {
  $('input#btn_translate').bind('click', hello);
  $('input#language_code').bind('keydown', function (event) {
    if (event.which === 13) {
      hello();
    }
  });
});
