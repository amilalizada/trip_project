
const all_data = {

}
document.querySelector('#search-button-1').addEventListener('click', (e) => {
    e.preventDefault();
    var cityName = document.querySelector('#city-name').value
    var selectedBed = document.getElementById("selected-beds").value;
    var selectedChildCount = document.getElementById("selected-child-count").value;
    var selectedRoomCount = document.getElementById("selected-room-count").value;
    // var hotel_amenities = document.querySelectorAll('.checked-inputs')

    var data = {
        'cityName': cityName,
        'selectedBed': selectedBed,
        'selectedChildCount': selectedChildCount,
        'selectedRoomCount': selectedRoomCount,
    }
    all_data['cityName'] = cityName
    all_data['selectedBed'] = selectedBed
    all_data['selectedChildCount'] = selectedChildCount
    all_data['selectedRoomCount'] = selectedRoomCount
    loadAllData(all_data)
})

document.onclick = function (e) {
    if (e.target.classList.contains('checked-inputs')) {
        
        var hotel_amenities= new Array()
        var room_amenities=new Array()
        document.querySelectorAll('.checked-inputs').forEach(function (e) {
            if (e.classList.contains('hotel-amenity')) {
                if (e.checked == true) {
                    var hotel_amenity = e.closest('.d-flex').querySelector('.choose-types').innerText
                    hotel_amenities.push(hotel_amenity)
                    
                }
            }
            if (e.classList.contains('room-amenity') && e.checked == true) {
                var room_amenity = e.closest('.d-flex').querySelector('.choose-types').innerText
                room_amenities.push(room_amenity)
            }

        })
        all_data['hotel_amenities'] = hotel_amenities
        all_data['room_amenities'] = room_amenities
        loadAllData(all_data)

    }
        

}
document.querySelector('.min-price').addEventListener('input', (e) => {
    var minPrice = document.querySelector('.min-price').value
    all_data['minPrice'] = minPrice
    loadAllData(all_data)
})
document.querySelector('.max-price').addEventListener('input', (e) => {
    var maxPrice = document.querySelector('.max-price').value
    all_data['maxPrice'] = maxPrice
    loadAllData(all_data)
})

function loadAllData(data) {
    console.log(data)
    $.ajax({
        url: 'http://localhost:8000/api/v1.0/hotels/',
        method: "GET",
        data: data,
        success: function (response) {
            console.log(response)
            // var link = document.querySelector('.slugs-anchor').href
            document.querySelector('.removed-data').innerHTML = ''
            console.log(response.page_range)
            for (hotel of response.filtered_hotels) {
                // let div_row = document.createElement('div')
                // div_row.classList.add('row')
                let div_col_12 = document.createElement('div')
                document.querySelector('.removed-data').appendChild(div_col_12)
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
                image_tag.setAttribute('src', hotel.main_image)
                div_image.appendChild(image_tag)


                let center_section = document.createElement('div')
                center_section.classList.add('col-md-6')
                div_second_row.appendChild(center_section)
                let card_body_center = document.createElement('div')
                card_body_center.classList.add('card-body')
                center_section.appendChild(card_body_center)
                let hotel_name = document.createElement('h6')
                hotel_name.innerText=hotel.name
                hotel_name.classList.add('card-title', 'text-primary', 'mb-1', 'card-title-js')
                let hotel_rating_stars = document.createElement('div')
                hotel_rating_stars.classList.add('d-flex', 'align-items-center', 'mb-3')
                for(let i =0;i<parseInt(hotel.rating);i++){
                    hotel_rating_stars.innerHTML +='<span class="fa fa-star checked"> </span>'
                }
                for(let i=0;i<(5-parseInt(hotel.rating));i++){
                    hotel_rating_stars.innerHTML +='<span class="fa fa-star"> </span>'
                }
                let hotel_long_description = document.createElement('p')
                hotel_long_description.innerText=hotel.short_description
                hotel_long_description.classList.add('card-text', 'hotel-long-desc-js')
                let hotel_name_description_parent = document.createElement('p')
                hotel_name_description_parent.classList.add('card-text')
                card_body_center.appendChild(hotel_name)
                card_body_center.appendChild(hotel_rating_stars)
                card_body_center.appendChild(hotel_long_description)
                card_body_center.appendChild(hotel_name_description_parent)
                let hotel_name_description = document.createElement('small')
                hotel_name_description.classList.add('text-muted')
                hotel_name_description.innerText=hotel.name_description
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
                first_childs_second_div.innerText=hotel.rating
                right_section_sub_div_firstChild.appendChild(first_childs_second_div)

                let right_section_sub_div_secondChild = document.createElement('div')
                right_section_sub_div_secondChild.classList.add('d-flex', 'flex-column', 'justify-content-end', 'p-2')
                right_section_sub_div.appendChild(right_section_sub_div_secondChild)
                let price = document.createElement('span')
                price.innerText=`Price for night ${hotel.min_price}$`
                price.classList.add('text-right', 'price-in-js')
                let reserve_button = document.createElement('a')
                reserve_button.href = hotel.my_url
                reserve_button.classList.add('btn', 'btn-danger', 'reserve-button-js')
                reserve_button.setAttribute('type', 'button')
                reserve_button.innerText='Reserve'
                // console.log(link)
                right_section_sub_div_secondChild.appendChild(price)
                right_section_sub_div_secondChild.appendChild(reserve_button)
            }
            document.querySelector('.old-pagi').innerHTML=''
            document.querySelector('.js-pagination').innerHTML=''
            for (var i =1;i<=response.page_range;i++){
                page_numbers=document.createElement('span')
                page_numbers.innerText=i
                page_numbers.href=`?page=${i}`
                document.querySelector('.js-pagination').appendChild(page_numbers)
                page_numbers.classList.add('m-2','pagination-numbers-js')

                page_numbers.addEventListener('click',function(){
                    all_data['page']=this.innerText
                    loadAllData(all_data)
                })
            }
            
        },
        error: function (error) {
            console.log(error)
        }
    })
}