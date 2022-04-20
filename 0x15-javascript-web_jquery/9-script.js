$(function () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=f'
    $.get(url, function (data, textStatus) {
        if (textStatus === 'success') {
            $('#hello').text(data.hello);
        }
    });
});