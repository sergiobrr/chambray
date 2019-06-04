$(document).ready(function() {
	$('#sidebarCollapse').on('click',function(){
		$('#main-sidebar').toggleClass('active');
	});

	$('#close-menu').on('click',function(){
		$('#main-sidebar').toggleClass('active');
	});

	var $grid_iso = $('.grid').isotope({
		itemSelector: '.grid-item',
		percentPosition: false,
		masonry: {
			columnWidth: 300,
			fitWidth: true,
			gutter: 10
		}
	});

	// init Masonry
	var $grid = $('.grid').masonry({
		columnWidth: 300,
		itemSelector: '.grid-item',
		percentPosition: false,
		fitWidth: true,
		gutter: 10
	});

	//layout Masonry after each image loads
	$grid.imagesLoaded().progress( function() {
		$grid.masonry('layout');
		$grid.addClass('masonry');
	});

	var toggleClasses = function(element, className) {
		if (element.hasClass(className)) {
			element.removeClass(className);
		} else {
			element.addClass(className);
		}
	}

	var filterIsotope = function(classname) {
		$grid_iso.isotope({filter: classname});
	}

	$('.isofilter').click(function() {
		var classname = $(this).attr('id');
		$('.grid-item').each(function(){
			console.log($(this), !$(this).hasClass('closed'));
			if(!$(this).hasClass('closed')) {
				var id = '#' + $(this).attr('id');
				console.log($(this), id);
				closeItem(id);
			}
		});
		filterIsotope(classname);
		$('.isofilter').removeClass('isoactive')
		$(this).addClass('isoactive');
	});

	var opened = 1;

	$('.grid-item').click(function() {
		var id = '#' + $(this).attr('id');
		animateItem(id);
	});

	var animateItem = function(id) {
		if($(id).hasClass('closed')) {
			openItem(id);	
		} else {
			closeItem(id);
		};
	};

	var openItem = function(id) {
		$(id).css('z-index', 10 + opened);
		opened++;
		$(id).find('img.unanimated-image').addClass('hidden');
		$(id).removeClass('grid-sizer').addClass('grid-item--width2');
		// setTimeout(function(){
		// 	$grid.masonry('layout');
		// }, 200);
		$(id).addClass('levited');
		$(id).find('img.animated-image').removeClass('animated-image')
				.addClass('revealed');
		setTimeout(function(){
			$(id).find('div.summarize-row').removeClass('hidden');
		}, 400);
		$(id).find('div.lrd-item-title').addClass('important');
		$(id).find('ul.links').addClass('links-important');
		$(id).removeClass('closed');
	};

	var closeItem = function(id) {
		console.log('close item', id);
		$(id).find('div.summarize-row').addClass('hidden');
		$(id).find('img.revealed').removeClass('revealed').addClass('animated-image');
		$(id).find('img.unanimated-image').removeClass('hidden');
		$(id).find('div.lrd-item-title').removeClass('important');
		$(id).find('ul.links').removeClass('links-important');
		setTimeout(function(){
			$(id).removeClass('levited');
			$(id).removeClass('grid-item--width2').addClass('grid-sizer');
		}, 200);
		// setTimeout(function(){
		// 	$grid.masonry('layout');
		// }, 300);
		$(id).addClass('closed');
		$(id).css('z-index', '1');
	}

});
