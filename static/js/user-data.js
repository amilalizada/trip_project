const send_data = {

}
document.querySelector('.profile').addEventListener('click', (e) => {
    var user_id = document.querySelector('.profile').dataset.user
    console.log(user_id)
    send_data['reservation-user-id']=''
    send_data['hotel-user-id']=''
    send_data['userId'] = user_id
    getAllData(send_data)
})
document.querySelector('.reservations').addEventListener('click', (e) => {
    var reservation_user_id = document.querySelector('.reservations').dataset.reservation
    console.log(reservation_user_id)
    send_data['userId']=''
    send_data['hotel-user-id']=''
    send_data['reservation-user-id'] = reservation_user_id

    getAllData(send_data)
})
document.querySelector('.hotels').addEventListener('click', (e) => {
    var hotel_user_id = document.querySelector('.hotels').dataset.hotel
    send_data['userId']=''
    send_data['reservation-user-id']=''
    send_data['hotel-user-id'] = hotel_user_id
    getAllData(send_data)
})






function getAllData(data) {
    console.log(data)
    $.ajax({
        url: 'http://localhost:8000/api/v1.0/hotels/user-profile/',
        method: "GET",
        data: data,
        success: function (response) {
            console.log(response)
            if (response.user){
                document.querySelector('.main-div-2').innerHTML = ''
                let h1_title = document.createElement('h1')
                h1_title.innerHTML='My Profile'
                document.querySelector('.main-div-2').appendChild(h1_title)
                let parentDiv = document.createElement('div')
                document.querySelector('.main-div-2').appendChild(parentDiv)
                parentDiv.innerHTML=`<div class="card mb-3" style="max-width: 540px;">
                <div class="row no-gutters">
                <div class="col-md-4">
                    <img src="${response.user.image}" class="card-img" alt="...">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                    <h5 class="card-title">${response.user.name} ${response.user.surname}</h5>
                    <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                    <p class="card-text"><small class="text-muted">${response.user.email}</small></p>
                    </div>
                </div>
                </div>
            </div>`}
            if (response.reservations){
                document.querySelector('.main-div-2').innerHTML = ''
                let h1_title = document.createElement('h1')
                h1_title.innerHTML='My Reservations'
                document.querySelector('.main-div-2').appendChild(h1_title)
                let reservationDiv = document.createElement('div')
                reservationDiv.classList.add('row')
                for (reservation of response.reservations){
                    // document.querySelector('.main-div-2').classList.add('d-flex')
                    document.querySelector('.main-div-2').appendChild(reservationDiv)
                    let child_res_div = document.createElement('div')
                    reservationDiv.appendChild(child_res_div)
                    child_res_div.classList.add('col-4')
                    child_res_div.innerHTML = `<div class="card m-3" style="width: 18rem;">
                    <img src="${reservation.hotel.main_image}" style="width:286px; height:200px; class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">${reservation.hotel.name}</h5>
                      <p class="card-text">Reservation day count : ${reservation.day_count} days</p>
                      <p class="card-text">Reservation  price : ${reservation.price}</p>
                      
                    </div>
                  </div>`
                }
            }
            if (response.hotels){
                document.querySelector('.main-div-2').innerHTML = ''
                let h1_title = document.createElement('h1')
                h1_title.innerHTML='My Hotels'
                document.querySelector('.main-div-2').appendChild(h1_title)
                for (hotel of response.hotels){
                let div_col_12 = document.createElement('div')
                
                document.querySelector('.main-div-2').appendChild(div_col_12)
                div_col_12.classList.add('col-12')
                // div_row.appendChild(div_col_12)
                let div_card = document.createElement('div')
                div_card.classList.add('card', 'mb-3', 'p-3', 'card-js')
                div_col_12.appendChild(div_card)
                let div_second_row = document.createElement('div')
                div_second_row.classList.add('row', 'no-gutters')
                div_card.appendChild(div_second_row)
                let div_image = document.createElement('div')
                div_image.classList.add('col-md-3')
                div_second_row.appendChild(div_image)
                let image_tag = document.createElement('img')
                image_tag.classList.add('content-image', 'card-img')
                image_tag.setAttribute('src', hotel.hotel.main_image)
                div_image.appendChild(image_tag)


                let center_section = document.createElement('div')
                center_section.classList.add('col-md-6')
                div_second_row.appendChild(center_section)
                let card_body_center = document.createElement('div')
                card_body_center.classList.add('card-body')
                center_section.appendChild(card_body_center)
                let hotel_name = document.createElement('h6')
                hotel_name.innerText=hotel.hotel.name
                hotel_name.classList.add('card-title', 'text-primary', 'mb-1', 'card-title-js')
                let hotel_rating_stars = document.createElement('div')
                hotel_rating_stars.classList.add('d-flex', 'align-items-center', 'mb-3')
                for(let i =0;i<parseInt(hotel.hotel.rating);i++){
                    hotel_rating_stars.innerHTML +='<span class="fa fa-star checked"> </span>'
                }
                for(let i=0;i<(5-parseInt(hotel.hotel.rating));i++){
                    hotel_rating_stars.innerHTML +='<span class="fa fa-star"> </span>'
                }
                let hotel_long_description = document.createElement('p')
                hotel_long_description.innerText=hotel.hotel.short_description
                hotel_long_description.classList.add('card-text', 'hotel-long-desc-js')
                let hotel_name_description_parent = document.createElement('p')
                hotel_name_description_parent.classList.add('card-text')
                card_body_center.appendChild(hotel_name)
                card_body_center.appendChild(hotel_rating_stars)
                card_body_center.appendChild(hotel_long_description)
                card_body_center.appendChild(hotel_name_description_parent)
                let hotel_name_description = document.createElement('small')
                hotel_name_description.classList.add('text-muted')
                hotel_name_description.innerText=hotel.hotel.name_description
                hotel_name_description_parent.appendChild(hotel_name_description)


                let right_section = document.createElement('div')
                right_section.classList.add('col-md-3')
                div_second_row.appendChild(right_section)
                let right_section_sub_div = document.createElement('div')
                right_section_sub_div.classList.add('d-flex', 'flex-column', 'justify-content-between', 'h-100')
                right_section.appendChild(right_section_sub_div)
                let right_section_sub_div_firstChild = document.createElement('div')
                right_section_sub_div_firstChild.classList.add('d-flex', 'align-items-center', 'justify-content-end', 'p-2')
                right_section_sub_div.appendChild(right_section_sub_div_firstChild)
                let first_childs_first_div = document.createElement('div')
                first_childs_first_div.classList.add('d-flex', 'flex-column', 'mr-2', 'first-child-js')
                right_section_sub_div_firstChild.appendChild(first_childs_first_div)
                let review_description = document.createElement('h6')
                let review_count = document.createElement('small')
                review_count.innerText='75 Reviews'
                review_description.innerText='Very good'
                first_childs_first_div.appendChild(review_description)
                first_childs_first_div.appendChild(review_count)
                let first_childs_second_div = document.createElement('div')
                first_childs_second_div.classList.add('rating-count')
                first_childs_second_div.innerText=hotel.hotel.rating
                right_section_sub_div_firstChild.appendChild(first_childs_second_div)

                let right_section_sub_div_secondChild = document.createElement('div')
                right_section_sub_div_secondChild.classList.add('d-flex', 'flex-column', 'justify-content-end', 'p-2')
                right_section_sub_div.appendChild(right_section_sub_div_secondChild)
                let price = document.createElement('span')
                price.innerText=`Price for night ${hotel.hotel.min_price}$`
                price.classList.add('text-right', 'price-in-js')
                let reserve_button = document.createElement('a')
                reserve_button.href = hotel.my_url
                reserve_button.classList.add('btn', 'btn-danger', 'reserve-button-js')
                reserve_button.setAttribute('type', 'button')
                reserve_button.innerText='Reserve'
                // console.log(link)
                right_section_sub_div_secondChild.appendChild(price)
                right_section_sub_div_secondChild.appendChild(reserve_button)

                let div_x_button = document.createElement('div')
                div_image.appendChild(div_x_button)
                let span_forget_button = document.createElement('span')
                div_x_button.appendChild(span_forget_button)
                div_x_button.classList.add('forget-button-div','forget-button-div-js')
                div_x_button.setAttribute('hotel_id',hotel.hotel.id)
                span_forget_button.classList.add('forget-button')
                span_forget_button.innerHTML='x'
                document.querySelectorAll('.forget-button-div').forEach(function(e){
                    e.addEventListener('click', function() {
                        let hotels_id= this.getAttribute('hotel_id')
                        console.log(hotels_id)
                        delete_article(hotels_id)
                    })
                }) 

                
                }
            }
            },
        error: function (error) {
            console.log(error)
        }
        })
}

function delete_article(hotel_id) {
    $.ajax({
        url: "{% url 'hotels_app:delete_hotel' 12345 %}".replace('12345', hotel_id),
        method: 'GET',
        success: function (data) {
            location.reload();

        }
    })

}
