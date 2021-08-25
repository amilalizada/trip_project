 
var total_days = document.querySelector('.total-price').dataset.sum
var price_night = document.querySelector('.price-for-night').innerText

var total = parseInt(total_days) * parseInt(price_night)
document.querySelector('.total-price').innerText = total
if (total_days==''){
    document.querySelector('.total-price').innerText = price_night
}
var first_date = document.querySelector('.first-date').innerText
if (first_date==''){
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();
    today = yyyy + ' ' + mm + ' ' + dd;
    console.log(today)
    document.querySelector('.first-date').innerText = today
}
var second_date = document.querySelector('.second-date').innerText
if (second_date==''){
    var today = new Date();
    var dd = String(today.getDate()+1).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();
    today = yyyy + ' ' + mm + ' ' + dd;
    console.log(today)
    document.querySelector('.second-date').innerText = today
}