document.getElementById('search').addEventListener('input', function () {
    
    var searchInput = document.getElementById('search');
    var inputValue = searchInput.value;
    // console.log(inputValue);
    $.ajax({
        url: 'http://localhost:8000/api/v1.0/cities/',
        method: 'GET',
        data: {
            'inputValue': inputValue,
        },
        success: function (response) {
            console.log(response);
            $('.empty').html('')
            let formDiv = $(`<div class="form-div w-100"><div>`);
            $('.empty').append(formDiv)
            if (inputValue) {
                for (let object of response.data_obj) {

                    $('.form-div').append(`<a class="w-100 mt-1 mb-1" href="${object.url}"><img class="ajax-img ml-2" src="${object.main_image}"><span class="ml-3">${object.name}</span></a>`)

                }
            }
        },
        error: function (error_response) {
            console.log(error_response);
        }
    })
});


