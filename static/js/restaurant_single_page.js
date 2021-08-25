$(document).ready(function () {

    // $("#review-submit").submit(function(e) {
    //     e.preventDefault();
    // });

    $('.all-photos').click(function(){
        console.log('2')
        document.querySelector('.all-photos-page').classList.remove('d-none');
        document.querySelector('.all-photos-page').classList.add('d-block');
        document.querySelector('body').style.overflow='hidden'
      });
    $('.close-all-photos').click(function(){
        document.querySelector('.all-photos-page').classList.remove('d-block');
        document.querySelector('.all-photos-page').classList.add('d-none');
        document.querySelector('body').style.overflowY='scroll'
      });

    
    })

document.onclick = function (e){
        if (e.target.closest('.position-exit-cursor'))
        {
            document.querySelector('.table-restaurant-open-time').classList.remove("d-block"); 
            document.querySelector('.table-restaurant-open-time').classList.add("d-none"); 
        }
        else if (e.target.closest('.jquery-effect')) 
        {
            if(document.querySelector('.table-restaurant-open-time').classList.contains('d-none'))
            {
                document.querySelector('.table-restaurant-open-time').classList.remove("d-none"); 
                document.querySelector('.table-restaurant-open-time').classList.add("d-block"); 
            }
            else{
                document.querySelector('.table-restaurant-open-time').classList.remove("d-block"); 
                document.querySelector('.table-restaurant-open-time').classList.add("d-none"); 
            }
            
        }
        else if (!e.target.closest('.table-restaurant-open-time')) 
        {
            document.querySelector('.table-restaurant-open-time').classList.remove("d-block"); 
            document.querySelector('.table-restaurant-open-time').classList.add("d-none"); 
        }

    }

    document.querySelectorAll('.food-rating').forEach(function(element){
        element.addEventListener('click',function(){
            let food_rating = element.getAttribute('value')
            let food_rating_form = document.querySelector('.food-rating-form')
            food_rating_form.setAttribute('value',food_rating)
        })
    })

    document.querySelectorAll('.service-rating').forEach(function(element){
        element.addEventListener('click',function(){
            let service_rating = element.getAttribute('value')
            let service_rating_form = document.querySelector('.service-rating-form')
            service_rating_form.setAttribute('value',service_rating)
        })
    })

    document.querySelectorAll('.value-rating').forEach(function(element){
        element.addEventListener('click',function(){
            let value_rating = element.getAttribute('value')
            let value_rating_form = document.querySelector('.value-rating-form')
            value_rating_form.setAttribute('value',value_rating)
        })
    })

    document.querySelectorAll('.atmosphere-rating').forEach(function(element){
        element.addEventListener('click',function(){
            let atmosphere_rating = element.getAttribute('value')
            let atmosphere_rating_form = document.querySelector('.atmosphere-rating-form')
            atmosphere_rating_form.setAttribute('value',atmosphere_rating)
        })
    })

    document.querySelector('.heart-img').addEventListener('click',function(){
        console.log('aa')
        let element = document.querySelector('.heart-img')
        console.log(element)
        element.style.backgroundImage="url('/static/images/red-heart.svg')";
    })

    document.querySelectorAll('.save-restaurant-icon').forEach(function(e){
        e.addEventListener('click',function(){
            let element = e.querySelector('.same-location-save-restaurant')
            element.style.backgroundImage="url('/static/images/red-heart.svg')"
        })
        
    })





