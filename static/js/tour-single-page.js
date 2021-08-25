$(document).ready(function () {

    $('body').scrollspy({
        target: '#myScrollspy'
    })
    $('.collapse').collapse()

    $('#myTab a').on('click', function (e) {
        e.preventDefault()
        $(this).tab('show')
    })

    window.onscroll = function () {
        // console.log(window.pageYOffset)
        var element = document.querySelector('.mid-right');
        if (window.pageYOffset <= 3000 && window.pageYOffset >= 530) {

            // console.log(element)
            this.document.querySelector('.route').style.position = 'fixed';
            this.document.querySelector('.route').style.top = '10px';
            this.document.querySelector('.route ul').style.position = '';
            this.document.querySelector('.route ul').style.bottom = '10px';
            element.classList.add("offset-lg-3");
        } else if (window.pageYOffset > 2438) {
            this.document.querySelector('.route').style.position = 'relative';
            this.document.querySelector('.route ul').style.position = 'absolute';
            this.document.querySelector('.route ul').style.bottom = '10px';

        } else {
            this.document.querySelector('.route').style.position = '';
            this.document.querySelector('.route').style.top = '';
            element.classList.remove("offset-lg-3");
        }
    }


    var expend_all = document.querySelector('.expendall');

    expend_all.addEventListener("click", function () {
        if (expend_all.classList.contains('collapseall')) {
            collapseAll();
        } else {
            expandAll();
        }
    });


    var expandAll = () => {
        var collapses = document.querySelectorAll('#accordion .collapse')

        var collapse_heads = document.querySelectorAll('.collapse-head')
        var expend_all_word = document.querySelector('.expend-all')

        var parent = document.querySelector('#headingOne')


        var inhead_plus = document.querySelectorAll('.inhead-plus-img');
        console.log(inhead_plus)
        collapses.forEach((e) => {

            e.classList.add('show');
            expend_all.querySelector('.plus-img').innerHTML = "-";
            expend_all_word.innerHTML = 'Collapse all'
            inhead_plus.innerHTML = '+'


        });

        collapse_heads.forEach((e) => {

            if (e.style.backgroundColor == '#ededed') {
                e.style.backgroundColor = "#2b3945";
            } else {
                e.style.backgroundColor = "#ededed";
            }
        });

        document.querySelector('.expendall').classList.add('collapseall');
        document.querySelector('.expendall').classList.remove('expendall');

    };


    var collapseAll = () => {
        var collapses = document.querySelectorAll('#accordion .collapse')

        var collapse_heads = document.querySelectorAll('.collapse-head')
        var expend_all_word = document.querySelector('.expend-all')
        var parent = document.querySelector('#headingOne')
        var parentChildren = parent.children

        var inhead_plus = document.querySelectorAll('.inhead-plus-img');
        collapses.forEach((e) => {
            e.classList.remove("show");

            this.querySelector('.plus-img').innerHTML = "+";
            expend_all_word.innerHTML = 'Expend all'
            inhead_plus.innerHTML = '-'


        });
        document.querySelector('.collapseall').classList.add('expendall');
        document.querySelector('.collapseall').classList.remove('collapseall');
    };




    // var headerOne = document.querySelectorAll('.collapse-head')
    // headerOne.forEach((e) => {
    //     e.addEventListener("click", function () {

    //         console.log(this);

    //         if (this.closest('.card').querySelector('.collapse').classList.contains('show')) {
    //             console.log('here')
    //             this.style.backgroundColor = "#ededed";



    //         } else {
    //             this.style.backgroundColor = "#2b3945";
    //         }
    //     });
    // })





});