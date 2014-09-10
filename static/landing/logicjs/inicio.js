(function(){
var controller={start : function(_,context,APP){

var $context=$(context);

function sendRegister(){
	$(".form_error").hide();
	$(".form_error_sending").show();
	var _data = APP.Form.getFields($context.find("#register_form"));
	//console.log(_data);
	if(_data && typeof _data.FK_EVENT!="undefined"){
		var offset=$("#register_form").offset();
		APP.Page.block("register_form");
		APP.Page.loading(true, (offset.top+$context.find("#register_form").height()/2), (offset.left+$context.find("#register_form").width()/2)-50);
		$("#send_register").unbind();
		$.easyAjax({
			file:"sendRegister",
			data:_data,
			success:function(payload){
				$(".form_error").hide();
				if(payload=="ERROR_EMAIL")
					$(".form_error_email").show();
				else if(payload=="ERROR_FIELDS")
					$(".form_error_unaviable").show();
				else if(payload=="ERROR_EVENT")
					$(".form_error_event").show();
				else if(payload=="ERROR_SIZE")
					$(".form_error_size").show();
				else if(payload=="ERROR_WHITELIST")
					$(".form_error_email_whitelist").show();
				else if(payload=="OK")
					window.location.href=base_url+"registro_confirmar";
				else
					alert("Se produjo un error inesperado: "+payload);
			},
			error:function(){
				$(".form_error").hide();
				$(".form_error_unaviable").show();
			},
			complete:function(){
				APP.Page.unblock("register_form");
				APP.Page.loading(false);
				$("#send_register").click(function(e){
					sendRegister();
					e.preventDefault();
				});
			}
		});
	}else{
		$(".form_error").hide();
		$(".form_error_fields").show();
	}
}

$(document).ready(function(e){
	$("#send_register").click(function(e){
		sendRegister();
		e.preventDefault();
	});
	
	$("#register_form").submit(function(e){
		sendRegister();
		e.preventDefault();
	});	
});

}};
return controller;
})();