/**
 * home JS - separated because homepages usually use a lot of stuff the rest of the site doesn't need
 */
/* define $ as jQuery just in case */
(function ($) {
	/* slideshow - my custom plugin */
	$.fn.slideshow = function () {
		/* set vars */
		var slideshow = this;
		var slides = slideshow.find('.slide');
		var controls = slideshow.find('.control');
		var active_slides = slideshow.find('.slide.active');
		var active_slide = active_slides.first().length > 0 ? active_slides.first() : slideshow.find('.slide:eq(0)');
		var target_index = active_slide.index();
		var target_el = slideshow.find('.slide:eq(' + target_index + ')');
		var target_control = slideshow.find('.control:eq(' + target_index + ')');
		var slide_speed = 10000;
		var timer;

		/* hide the slides before showing the active slide */
		slideshow.hide();
		$(window).load(function () {
			/* hide all slides, then show the active one */
			slides.removeClass('active').hide();
			target_el.addClass('active').show();

			/* remove active class from all controls and then add it to the target (active) control */
			controls.removeClass('active');
			target_control.addClass('active');

			/* show the slideshow when everything is set */
			slideshow.show();

			/* animate the slideshow every XX seconds */
			var timer = setInterval(show_next_slide, slide_speed);
		});

		/* navigator */
		slideshow.on('click', '.control', function (e) {
			/* reset the timer */
			window.clearInterval(timer);

			/* set the vars */
			var target_index = $(this).index();
			var target_slide = slideshow.find('.slide:eq(' + target_index + ')');

			/* show the targeted slide */
			slides.removeClass('active').hide();
			target_slide.show().addClass('active');

			/* change the control nav to active */
			controls.removeClass('active');
			$(this).addClass('active');
			e.preventDefault();
		});

		/* animate slides */
		function show_next_slide() {
			/* set the vars */
			var slides = slideshow.find('.slide');
			var curr_slide = slideshow.find('.slide.active');
			var curr_index = curr_slide.index();
			var next_index = parseInt(curr_index + 1);
			if (next_index > slides.length - 1) {
				var next_index = 0;
			}
			var target_el = slideshow.find('.slide:eq(' + next_index + ')');
			var target_control = slideshow.find('.control:eq(' + next_index + ')');

			/* show the next slide */
			slides.hide().removeClass('active');
			target_el.show().addClass('active');

			/* change the control nav to active */
			controls.removeClass('active');
			target_control.addClass('active');
		}
	}
})(jQuery);
