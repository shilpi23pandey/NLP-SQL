//alert("Working");
$(document).ready(function() {
            //option A
        $("#queryForm").submit(function(e){
		e.preventDefault(e);
		$( "#queryResult" ).empty();
		var form = $('#queryForm');
		var formData = form.serialize();
		$.ajax({
		type:"POST",
		data:formData,
    		url : "submitQuery",
	        success: function(result) {
				console.log(result);
				$(result).appendTo('#queryResult');
	        	}
	        });
            });
    $('#closeTerminal').click(function(){
    	$('#terminalDiv').removeClass('animated bounceInLeft');
    	$('#terminalDiv').addClass('animated bounceOutLeft');
    	$('#terminalDiv').animateCss('bounceOutLeft');
    } );
    
    $('#powerOff').click(function(){
    	$('#terminalDiv').removeClass('animated bounceInLeft');
    	$('#terminalDiv').addClass('animated bounceOutLeft');
    	$('#terminalDiv').animateCss('bounceOutLeft');
    } );
    $('#minimizeTerminal').click(function(){
    	$('#terminalDiv').removeClass('animated bounceInLeft');
    	$('#terminalDiv').addClass('animated bounceOutLeft');
    	$('#terminalDiv').animateCss('bounceOutLeft');
    } );
    $('#showTerminal').click(function(){
		$( "#Database" ).hide();
    	$('#terminalDiv').removeClass('animated bounceOutLeft');
    	$('#terminalDiv').addClass('animated bounceInLeft');
    	$('#terminalDiv').animateCss('bouncInLeft');
    } );

    $('#Database').hide(); 
    $('#openDatabase').click(function(){
    	$('#Database').show();
		$( "#showStudentDetails" ).empty();
		$( "#showDepartmentDetails" ).empty();		
    	$.ajax({
			type:"POST",
			data:{},
    		url : "showStudentDetails",
	        success: function(result) {
				console.log(result);
				$(result).appendTo('#showStudentDetails');
	        }	
	    });
	    $.ajax({
			type:"POST",
			data:{},
    		url : "showDepartmentDetails",
	        success: function(result) {
				console.log(result);
				$(result).appendTo('#showDepartmentDetails');
	        }	
	     });
    });

    
});
