$(function () {
    $('$#btn_translate').on("click keypress", function () {
        code = $('#language_code').val();
        const url = 'https://fourtonfish.com/hellosalut/?lang=' + code;
        $.get(url, function (data, textStatus) {
            if (textStatus === 'success') {
                $('#hello').text(data.hello);
            }
        });
    });
});