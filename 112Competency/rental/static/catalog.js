var movies =[];

function getCatalog(){
    $.ajax({
        url: 'http://127.0.0.1:8000/api/movies',
        type: "GET",
        success: function(response){
            console.log("response from server", response);

            movies = response.objects;
            for(var i=0; i<movies.length; i++){
                var movie = movies[i];
                displayMovie(movie, i);
            }
        },
        error: function(errorDetails){
            console.log("Error", errorDetails);
        }
    });
}

function displayMovie(movie, movie_count){
    //get container
    var container = $("#container");
    var first = "";
    if (movie_count == 0) first = "active";
    //create html sintax
    var sintax = 
    `
    <div class="carousel-item ${first}">
        <img src="http://via.placeholder.com/640x360" class="d-block w-100">
        <div class="carousel-caption d-none d-md-block">
            <h5>${movie.title}</h5>
            <h5>${movie.release_year}</h5>
            <p>${movie.star}</p>
            <p>${movie.director}</p>
        </div>
    </div>
    `;

    console.log(sintax);

    var Indicator = `<li data-target="#carouselExampleCaptions" data-slide-to="${movie_count}" class="${first}"></li>`



    //add sintax 
    container.append(sintax);
    $(".carousel-inidcators").append(Indicator);
}


function init(){
    console.log("Catalog JS is loaded");

    getCatalog();
}


window.onload = init;