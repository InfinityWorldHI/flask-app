$(document).ready(function(){
	const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
	const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

	$(document).on('click', '#edit_user', function(){
		var el = this;
	    var user_index = $(this).data('id');
		
		$.ajax({
			url: `/users/${user_index}`,
			type: 'GET',
			success: function(response){
				$('#user_up_form').html(response);
				$('#userEditModal').modal('show');
			},
			error: function(error){
				console.log(error);
			}
		});
	});

});