$(document).ready(function () {

    $('.all-photos').click(function(){
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
            document.querySelector('.table-place-open-time').classList.remove("d-block"); 
            document.querySelector('.table-place-open-time').classList.add("d-none"); 
        }
        else if (e.target.closest('.jquery-effect')) 
        {
            if(document.querySelector('.table-place-open-time').classList.contains('d-none'))
            {
                document.querySelector('.table-place-open-time').classList.remove("d-none"); 
                document.querySelector('.table-place-open-time').classList.add("d-block"); 
            }
            else{
                document.querySelector('.table-place-open-time').classList.remove("d-block"); 
                document.querySelector('.table-place-open-time').classList.add("d-none"); 
            }
            
        }
        else if (!e.target.closest('.table-place-open-time')) 
        {
            document.querySelector('.table-place-open-time').classList.remove("d-block"); 
            document.querySelector('.table-place-open-time').classList.add("d-none"); 
        }

    }

