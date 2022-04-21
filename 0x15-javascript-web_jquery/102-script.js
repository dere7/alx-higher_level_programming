$(function () {
  $('input#btn_translate').bind('click', function () {
    $.getJSON(
      'https://fourtonfish.com/hellosalut/',
      { lang: $('input#language_code').val() },
      function (json) {
        $('div#hello').text(json.hello);
      }
    );
  });
});
