    // document.querySelector('.children-show-extra-items').addEventListener('click', function () {
    //     if (document.querySelector('.icon-down').classList.contains('d-none')) {
    //         document.querySelector('.icon-up').classList.add('d-none')
    //         document.querySelector('.icon-down').classList.remove('d-none')
    //     } else {
    //         document.querySelector('.icon-down').classList.add('d-none')
    //         document.querySelector('.icon-up').classList.remove('d-none')
    //     }



    // })
    // if(document.querySelector('.children-show-extra-items').classList.contains

    $('#datepicker').datepicker({
        uiLibrary: 'bootstrap4'
    });
    $('#datepicker1').datepicker({
        uiLibrary: 'bootstrap4'
    });

    
    $(function () {
        // инициализация datetimepicker7 и datetimepicker8
        $("#datetimepicker7").datetimepicker();
        $("#datetimepicker8").datetimepicker({
            useCurrent: false
        });
        $("#datetimepicker7").on("dp.change", function (e) {
            $('#datetimepicker8').data("DateTimePicker").minDate(e.date);
        });
        $("#datetimepicker8").on("dp.change", function (e) {
            $('#datetimepicker7').data("DateTimePicker").maxDate(e.date);
        });
    });