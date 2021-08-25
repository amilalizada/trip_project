$('body').on('click', '.arrow-collapse', function(e) {
    var $this = $(this);
    if ( $this.closest('li').find('.collapse').hasClass('show') ) {
      $this.removeClass('active');
    } else {
      $this.addClass('active');
    }
    e.preventDefault();  
    
  });
$(window).resize(function () {
    var $this = $(this),
        w = $this.width();

    if (w > 768) {
        if ($('body').hasClass('offcanvas-menu')) {
            $('body').removeClass('offcanvas-menu');
        }
    }
})

$('body').on('click', '.js-menu-toggle', function (e) {
    var $this = $(this);
    e.preventDefault();

    if ($('body').hasClass('offcanvas-menu')) {
        $('body').removeClass('offcanvas-menu');
        $this.removeClass('active');
    } else {
        $('body').addClass('offcanvas-menu');
        $this.addClass('active');
    }
})

// click outisde offcanvas
$(document).mouseup(function (e) {
    var container = $(".site-mobile-menu");
    if (!container.is(e.target) && container.has(e.target).length === 0) {
        if ($('body').hasClass('offcanvas-menu')) {
            $('body').removeClass('offcanvas-menu');
        }
    }
});
