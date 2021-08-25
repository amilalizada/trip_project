$(document).ready(function () {


    var find_restaurant
    var option_checkbox_input = []
    var option_radio_input
    var all_options
    var current_page = 1;
    var restaurant_dropdown_text = document.querySelector('.restaurant-dropdown').innerText;

    document.querySelectorAll('.pages').forEach(function(e){
        e.addEventListener('click',function(){
            current_page = parseInt(e.innerText);
        })
    })
    let before_arrow = document.querySelector('.before-arrow');
    if(before_arrow){
        document.querySelector('.before-arrow').addEventListener('click',function(){
        current_page = current_page - 1;
        console.log(current_page)
    })
    }
    let next_arrow = document.querySelector('.next-arrow');
    if(next_arrow){
        document.querySelector('.next-arrow').addEventListener('click',function(){
        current_page = current_page + 1;
        console.log(current_page)
    })
    }
    

    document.querySelector('.restaurant-find').closest('.col-md-2').addEventListener('click',function(){
        find_restaurant = document.querySelector('.restaurant-filter-input').value
    })

    document.onclick = function (e) {
        if (! e.target.closest('.restaurant-dropdown')){
            document.querySelector('.dropdown-list').classList.remove('d-block')
            document.querySelector('.dropdown-list').classList.add('d-none')
        }

        if (e.target.closest(".all-options") && e.target.closest(".position-relative").querySelector('.all-option-tables').classList.contains('d-block')) {
            let parentElement = e.target.closest(".position-relative")
            parentElement.querySelector('.all-option-tables').classList.remove("d-block");
            parentElement.querySelector('.all-option-tables').classList.add("d-none");
        }

        else if (e.target.closest(".all-options") && e.target.closest(".position-relative").querySelector('.all-option-tables').classList.contains('d-none')) {
            document.querySelectorAll('.all-option-tables').forEach(function (e) {
                e.classList.remove("d-block");
                e.classList.add("d-none");
            })
            let parentElement = e.target.closest(".position-relative")
            parentElement.querySelector('.all-option-tables').classList.remove("d-none");
            parentElement.querySelector('.all-option-tables').classList.add("d-block");
        }

        else if(e.target.classList.contains('custom-checkbox')){
            current_page = 1
            option_checkbox_input = []
            if(e.target.checked==false){
                target_option = e.target.closest('.d-flex').querySelector('.checkbox-option').innerHTML
                document.querySelectorAll('.checkbox-option').forEach(function(filter_option){
                    if(filter_option.innerText == target_option){
                      filter_option.closest('.align-items-center').querySelector('input').checked=false
                    }
                })
            }
            document.querySelectorAll('.custom-checkbox').forEach(function (e) {
                if(e.checked==true){
                    var option = e.closest('.d-flex').querySelector('.checkbox-option').innerHTML
                    option_checkbox_input.push(option)
                    document.querySelectorAll('.checkbox-option').forEach(function(filter_option){
                        if(filter_option.innerText == option){
                          filter_option.closest('.align-items-center').querySelector('input').checked=true
                        }
                    })
                    
                }
               
            })
        }

        else if (e.target.classList.contains('regular-radio')){
                current_page = 1
                target_option = e.target.closest('.d-flex').querySelector('.radio-option').innerHTML
                document.querySelectorAll('.radio-option').forEach(function(filter_option){
                    if(filter_option.innerText != target_option){
                        filter_option.closest('.align-items-center').querySelector('input').checked=false;
                    }
                    else{
                        filter_option.closest('.align-items-center').querySelector('input').checked=true;
                    }
                })
                option_radio_input = target_option
                console.log(option_radio_input)
        }

        else if (!e.target.closest(".all-option-tables")) {
            document.querySelectorAll('.all-option-tables').forEach(function (e) {
                e.classList.remove("d-block");
                e.classList.add("d-none");
            })
        }
        all_options ={
            'option_checkbox_input' : option_checkbox_input,
            'option_radio_input' : option_radio_input,
            'find_restaurant' : find_restaurant,
            'restaurant_dropdown_text' : restaurant_dropdown_text,
        }
        option(all_options)
    }

    function option(all_options){
     $.ajax({
                    url : 'http://localhost:8000/api/v1.0/restaurants/',
                    method : "GET",
                    data : all_options,
                    success: function(response) {
                        console.log(response)
                        let number_restaurant_in_page = 1;
                        let count_all_restaurants = response.restaurants.length;
                        if(response.restaurants.length==0){
                            current_page=0;
                        }

                        $('.restaurants-cards').empty();
                        if(response.restaurants.length <= 1){
                            document.querySelector('.count-restaurants').innerText = `${response.restaurants.length} Restaurant`;
                        }
                        else{

                            document.querySelector('.count-restaurants').innerText = `${response.restaurants.length} Restaurants`;
                        }
                        for(let restaurant of response.restaurants){
                            restaurants(restaurant)
                        
                    }
                    
                    let header_pagination = document.querySelector('.block-27')
                    header_pagination.innerHTML = ''
                    document.querySelector('.restaurants-list').appendChild(header_pagination);
                    let ul_pagination = document.createElement('ul');
                    ul_pagination.classList.add('d-flex','list-pagination')
                    header_pagination.appendChild(ul_pagination);
                    let page_number =Math.ceil(response.restaurants.length/1);
 
                    currentPage(current_page)


                    function restaurants(response){
                        if(response){
                        let restaurant_card = document.createElement('div')
                            document.querySelector('.restaurants-cards').appendChild(restaurant_card)
                            restaurant_card.classList.add('mt-3','card','restaurant-card','mb-3')
                            restaurant_card.style.maxWidth='100%'
                            let no_gutters = document.createElement('div')
                            no_gutters.classList.add('d-flex','no-gutters')
                            restaurant_card.appendChild(no_gutters)
                            let image_link = document.createElement('a')
                            image_link.setAttribute('href',response.url)
                            no_gutters.appendChild(image_link)
                            let restaurant_image = document.createElement('img')
                            restaurant_image.classList.add('card-img','restaurant-card-img')
                            restaurant_image.setAttribute('src', response.image)
                            image_link.appendChild(restaurant_image)
                            let div_body_card = document.createElement('div')
                            no_gutters.appendChild(div_body_card)
                            let card_body = document.createElement('div')
                            card_body.classList.add('card-body','ml-1','body-card')
                            div_body_card.appendChild(card_body)
                            let restaurant_name = document.createElement('a')
                            restaurant_name.setAttribute('href',response.url)
                            restaurant_name.classList.add('card-title','m-0','restaurant-name')
                            restaurant_name.innerText = response.name
                            card_body.appendChild(restaurant_name)
                            let for_rating = document.createElement('div')
                            card_body.appendChild(for_rating)
                            let div_star = document.createElement('div')
                            for_rating.appendChild(div_star)
                            
                            for(let i =0;i<parseInt(response.overall_rating);i++){
                                div_star.innerHTML +='<span class="fa fa-star checked"> </span>'
                            }
                            for(let i=0;i<(5-parseInt(response.overall_rating));i++){
                                div_star.innerHTML  +='<span class="fa fa-star"> </span>'
                            }

                            let restaurant_city_name = document.createElement('small')
                            restaurant_city_name.classList.add('restaurant-city-name')
                            restaurant_city_name.innerText = response.city.name
                            card_body.appendChild(restaurant_city_name)
                            let work_time = document.createElement('p')
                            work_time.style.fontSize = '14px'
                            work_time.style.fontWeight = '400'

                            let restaurant_open_time_part_first = parseInt(response.open_time[0] + response.open_time[1])
                            if(restaurant_open_time_part_first>12){
                                restaurant_open_time_part_first = restaurant_open_time_part_first -12 ;
                            }
                            if(restaurant_open_time_part_first<10){
                                restaurant_open_time_part_first = '0' + restaurant_open_time_part_first ;
                            }
                            let restaurant_close_time_part_first = parseInt(response.close_time[0] + response.close_time[1])
                            if(restaurant_close_time_part_first >12){
                                restaurant_close_time_part_first  = restaurant_close_time_part_first - 12 ;
                            }
                            if(restaurant_close_time_part_first<10){
                                restaurant_close_time_part_first = '0' + restaurant_close_time_part_first ;
                            }
                            let restaurant_open_time_part_second='';
                            let restaurant_close_time_part_second='';
                            for(i=2;i<5;i++){
                                restaurant_open_time_part_second += response.open_time[i] ;
                                restaurant_close_time_part_second += response.close_time[i] ;
                            }
                            let restaurant_open_time = restaurant_open_time_part_first + restaurant_open_time_part_second ;
                            let restaurant_close_time = restaurant_close_time_part_first + restaurant_close_time_part_second ;
                            work_time.innerHTML = (`<span style="font-weight: 700;">Opening times:</span> ${restaurant_open_time} a.m. - ${restaurant_close_time} p.m.`)
                            card_body.appendChild(work_time)

                            let restaurant_delivery = document.createElement('div')
                            restaurant_delivery.classList.add('restaurant-delivery')
                            restaurant_delivery.innerText = `Takeout`
                            card_body.appendChild(restaurant_delivery)
                            let restaurant_telephone = document.createElement('div')
                            restaurant_telephone.classList.add('restaurant-telephone')
                            card_body.appendChild(restaurant_telephone)
                            let tel_svg = document.createElement('img')
                            tel_svg.setAttribute('src','/static/images/tel.svg')
                            restaurant_telephone.appendChild(tel_svg)
                            let restaurant_phone_number = document.createElement('span')
                            restaurant_phone_number.innerText = response.phone_number
                            restaurant_telephone.appendChild(restaurant_phone_number)
                    }
                }
                    
                    
                    

                    function currentPage(current_page){
                        ul_pagination.innerHTML = ''
                        
                        if(current_page > 1){
                            ul_pagination.innerHTML += ('<li><span class="before-arrow" href="">&lt;</span></li>')
                        }
                        for(i=1;i<=page_number;i++){
                            ul_pagination.innerHTML += `<li><span style="color:#077fff" class="pages" data-page="${i}" href="">${i}</span></li>`
                        }
                        if(current_page != page_number){
                            ul_pagination.innerHTML += ('<li><span class="next-arrow" href="">&gt;</span></li>')
                        }
                        document.querySelector('.list-pagination').querySelectorAll('.pages').forEach(function(page){
                            if(current_page == parseInt(page.getAttribute('data-page'))){
                                page.classList.add('active-page');
                            }
                        })
                        $('.restaurants-cards').empty();
                        for(i=current_page-1*number_restaurant_in_page;i<current_page*number_restaurant_in_page;i++){
                            restaurants(response.restaurants[i])
                        }
                    }


                    let before_arrow = document.querySelector('.before-arrow');
                    if(before_arrow){
                        before_arrow.addEventListener('click',function(){
                        current_page = current_page - 1;
                        currentPage(current_page)
                    })
                    }
                    
                    let next_arrow = document.querySelector('.next-arrow');
                    if(next_arrow){
                        next_arrow.addEventListener('click',function(){
                        current_page = current_page + 1;
                        currentPage(current_page)
                    })
                    }
                    

                    document.querySelectorAll('.pages').forEach(function(page){
                        page.addEventListener('click',function(){
                        current_page = parseInt(page.getAttribute('data-page'));
                        currentPage(current_page)
                        
                    })
                })
                    
                    


                        
                    },
                    error: function (error) {
                        console.log(error)
                    }
                })
            }

    document.querySelector('.restaurant-dropdown').addEventListener('click',function(){
        if (document.querySelector('.dropdown-list').classList.contains('d-none')){
            document.querySelector('.dropdown-list').classList.remove('d-none')
        document.querySelector('.dropdown-list').classList.add('d-block')
        }
        else {
            document.querySelector('.dropdown-list').classList.remove('d-block')
            document.querySelector('.dropdown-list').classList.add('d-none')
        }
    })

    document.querySelectorAll('.type-list').forEach(function(element){
        element.addEventListener('click',function(){
            let list_option = element.innerText
            document.querySelector('.restaurant-dropdown-featured').innerText=list_option
            restaurant_dropdown_text = list_option
            option(all_options)
        })
    })


})



