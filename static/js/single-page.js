$(function () {
    $('.gallery').gallery();
});

$(function () {
    $('.calender').pignoseCalender({
        multiple: true,
        select: function (date, obj) {
            obj.calender.parent().next().show().text('You selected ' +
                (date[0] === null ? 'null' : date[0].format('YYYY-MM-DD')) +
                '~' +
                (date[1] === null ? 'null' : date[1].format('YYYY-MM-DD')) +
                '.');
              
                var a = Math.ceil((date[1]._d - date[0]._d)/(60*60*24*1000))
                document.querySelectorAll('.price-count').forEach(function(e){
                    var price =parseInt(e.dataset.price)
                    e.innerText = price * a

                })
                console.log(date[0].format('YYYY-MM-DD'))
                document.querySelectorAll('.reserve-button').forEach(function(e){
                    e.href = e.href +'&first_date='+date[0].format('YYYY-MM-DD')+'&second_date='+date[1].format('YYYY-MM-DD')+'&total_days='+a
                    
                })
        }
       
    });
    
});
