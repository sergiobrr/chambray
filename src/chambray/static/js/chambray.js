$(document).ready(function(){
	$('#sidebarCollapse').on('click',function(){
		$('#main-sidebar').toggleClass('active');
		$('.owl-carousel').toggleClass('ristretto');
		$('.home-slide-container').toggleClass('ristretto');
		console.log('ATTIVATO....');
		//$('#sidebarCollapse').toggleClass('lrd-hidden');
	});

	$('#closer-btn').on('click',function(){
		console.log('e che cazzo...');
		$('#sidebarCollapse').toggleClass('lrd-hidden');
		//$('#main-sidebar').toggleClass('active');
	});
});