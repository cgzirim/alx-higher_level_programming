$(function () {
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json'
    $.get(url, function (data, textStatus) {
        if (textStatus === 'success') {
            let movies = data.results;
            for (let i in movies) {
                $('#list_movies').append('<li>' + movies[i].title + '</li>')
            }
        }
    });
});