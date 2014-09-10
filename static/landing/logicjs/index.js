(function(){
var APP=function(){
	var self=this;
	
	/* ************************ */
	/* 			  Form			*/
	/* ************************ */
	self.Form=function(){
		/* ************************ */
		/* 		 Private - Form		*/
		/* ************************ */
		var Form=this;

		var _getNode=function(nodeThing){
			var $node=null;
			if(typeof nodeThing!=="undefined"){
				if(typeof nodeThing==="string") //ID
					$node=$("#"+nodeThing);
				else
					if(nodeThing.length===undefined) //html node
						$node=$(nodeThing);
					else //html or jQuery nodes
						$node=$(nodeThing[0]);
			}
			return $node;
		};
		
		/* ************************ */
		/* 		 PUBLIC - Form		*/
		/* ************************ */
		Form.isEmail=function(email){   
			return email.match(/^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,3})$/);
		};
		
		Form.isEmpty=function(variable){
			return (typeof variable==="undefined" || variable===null || variable.length==0 || variable.value==="" || variable=="" || variable.match(/^\s+$/));
		};
		
		Form.haveWhitespaces=function(variable) {   
		    var espacio=[" ","\n","\t","\r"];
		    if(!Form.isEmpty(variable))
				for(var i=0; i<variable.length; i++)
					if(espacio.indexOf( variable.substring(i,i+1) ) != -1)
						return true;
		    return false;
		};
		Form.bindError=function(node){
			var $inputNode=_getNode(node);
			if($inputNode[0].type!=="submit"){
				if($inputNode[0].nodeName=="OPTION")
					$inputNode=$inputNode.parent();
				$inputNode.addClass("input_error");
				if($inputNode[0].type==="checkbox" || $inputNode[0].type==="radio" || $inputNode[0].type==="select-one" || $inputNode[0].type==="select-multiple")
					$inputNode.bind("change.inputError",function(){
						$inputNode.removeClass("input_error");
						$inputNode.unbind("change.inputError");
					});
				else if($inputNode[0].type!=="submit")
					$inputNode.bind("keyup.inputError",function(){
						$inputNode.removeClass("input_error");
						$inputNode.unbind("keyup.inputError");
					});
			}
		};
		Form.unbindError=function(node){
			var $inputNode=_getNode(node);
			if($inputNode[0].type!=="submit"){
				if($inputNode[0].nodeName=="OPTION")
					$inputNode=$inputNode.parent();
				$inputNode.removeClass("input_error");
				if($inputNode[0].type==="checkbox" || $inputNode[0].type==="radio" || $inputNode[0].type==="select-one" || $inputNode[0].type==="select-multiple")
					$inputNode.unbind("change.inputError");
				else if($inputNode[0].type!=="submit")
					$inputNode.unbind("keyup.inputError");
			}
		};
		//Dump all values into array, form can be an ID, html or jQuery node
		Form.getFields=function(form, validate){
			var $form=self.Page.getNode(form);
			if(validate===undefined) validate=true;
			if($form){
				var values={},
					valid=true;
				$form.find(":input").each(function(index,el){
					//console.log(this.id);
					//console.log(this.value);
					if(this.type==="radio"){
						if(this.checked)
							if($form.find("input[name="+this.name+"]").length>0)
								values[this.name]=$(this).val();
							else
								values[this.id]=$(this).val();
					}else if(this.type==="checkbox"){
						values[this.id]=this.checked;
					}else{
						if(this.type==="email" && $(this).val()!="" && !Form.isEmail(this.value) && this.required===false){
							valid=false;
							if(validate)
								Form.bindError(this);
						}else
							values[this.id]=$(this).val();
					}
						
					
					if(this.required!==false)
						if((this.type==="radio" || this.type==="checkbox") && !this.checked){
							if(validate)
								Form.bindError(this);
							valid=false;
						}else{
							if(Form.isEmpty(this.value) || (this.type==="email" && !Form.isEmail(this.value)) ){
								valid=false;
								if(validate)
									Form.bindError(this);
							}else
								if(validate)
									Form.unbindError(this);
						}
				});
				if(validate)
					return valid?values:null;
				else
					return values;
			}else
				return null;
		};
		
		/* ************************ */
		/* 	  CONSTRUCTOR - Form	*/
		/* ************************ */
		(function(){})();
	};
	
	/* ************************ */
	/* 		  Controller		*/
	/* ************************ */
	self.Controller=function(){
		/* ************************ */
		/* 	 PRIVATE - Controller	*/
		/* ************************ */
		var Controller=this,
			_stack={
				after	: [],
				before	: []
			},
			_namespace={},
			_cachedScripts=[],
			_cache={
				script	: [],
				context	: document
			};
		
		/* ************************ */
		/* 	 PUBLIC - Controller	*/
		/* ************************ */
		//Store Window context
		Controller.setContext=function(context){
			_cache.context=context;
		};
		Controller.getContext=function(){
			return _cache.context;
		};
		//Store JS code after load
		Controller.after=function(callback){
			_stack.after.push(callback);
		};
		//Store JS code before load
		Controller.before=function(callback){
			_stack.before.push(callback);
		};
		//Excecute all stored JS code when loaded
		Controller.ready=function(){
			for(var i=0;i<_stack.before.length;i++)
				if(typeof _stack.before[i]==="function")
					_stack.before[i](_namespace, _cache.context, self);
			for(var i=0;i<_stack.after.length;i++)
				if(typeof _stack.after[i]==="function")
					_stack.after[i](_namespace, _cache.context, self);
			_stack.before=[];
			_stack.after=[];
		};
		//Load JS controller script
		Controller.load=function(page,context){
			page=page||actual_loc;
			var found=false;
			for(var i=0;i<_cache.script.length;i++){
				if(page==_cache.script[i].page)
					found=i;
			}
			if(found!==false){
				Controller.before(_cache.script[found].fn.start);
				Controller.ready();
			}else{
				$.cachedScript=function(url,options){
					options = $.extend(options||{},{
				    	dataType: "script",
				    	cache: false,
				    	url: url
				  	});
					return jQuery.ajax(options);
				};
                                console.log(page);
                                console.log(base_url);
				$.cachedScript(base_url+'logicjs/'+page+'.js').done(function(payload){
					payload=eval(payload);
					_cache.script.push({
						page : page,
						fn	 : payload
					});
					if(typeof payload.start==="function"){
						Controller.before(payload.start);
						Controller.ready();
					}
				});
			}
		};
		
		/* ************************ */
		/* CONSTRUCTOR - Controller */
		/* ************************ */
		(function(){})();
	};
	
	/* ************************ */
	/* 		   History  		*/
	/* ************************ */
	self.History=function(){
		/* ************************ */
		/* 	   PRIVATE - History	*/
		/* ************************ */
		var History=this;
		
		/* ************************ */
		/* 	   PUBLIC - History  	*/
		/* ************************ */
		
		
		/* ************************ */
		/*   CONSTRUCTOR - History  */
		/* ************************ */
		(function(){})();
	};
	
	/* ************************ */
	/* 		  	 Page  			*/
	/* ************************ */
	self.Page=function(){
		/* ************************ */
		/* 	  	 PRIVATE - Page		*/
		/* ************************ */
		var Page=this,
			_$img=null;
		
		/* ************************ */
		/* 	  	 PUBLIC - Page 		*/
		/* ************************ */
		//Show loading animation
		Page.loading=function(state,top,left){
			if(state===true && !_$img){
				_$img=$("<img src='"+base_url+"img/loading_big.gif' />").css({
					position:"absolute",
					zIndex:999,
					left:left||0,
					top:top||0
				});
				var context=self.Controller.getContext();
				if(context.top!=window){
					if($(context).find("body").length>0)
						$(context).find("body").append(_$img);
					else
						context.append(_$img);
				}else
					$("body").append(_$img);
			}else if(_$img){
				_$img.remove();
				_$img=null;
			}
		};
		//Block section
		Page.block=function(node){
			Page.getNode(node).css("opacity","0.4").css("pointer-events","none");
		};
		//Unblock section
		Page.unblock=function(node){
			//console.log(node);
			//console.log(Page.getNode(node));
			Page.getNode(node).css("opacity","1").css("pointer-events","all");
		};
		//Get jQuery node
		Page.getNode=function(nodeThing){
			var $node=null,
				$context=$(self.Controller.getContext());
			if(typeof nodeThing!=="undefined"){
				if(typeof nodeThing==="string") //ID
					$node=$context.find("#"+nodeThing);
				else
					if(nodeThing.length===undefined) //html node
						$node=$context.find(nodeThing);
					else if(typeof nodeThing.get!=="function") //html or jQuery nodes
						$node=$context.find(nodeThing);
					else
						$node=$context.find(nodeThing.get(0));
			}
			if(typeof $node[0]==="undefined"){
				var $node=null,
					$context=$(document);
				if(typeof nodeThing!=="undefined"){
					if(typeof nodeThing==="string") //ID
						$node=$context.find("#"+nodeThing);
					else
						if(nodeThing.length===undefined) //html node
							$node=$context.find(nodeThing);
						else if(typeof nodeThing.get!=="function") //html or jQuery nodes
							$node=$context.find(nodeThing);
						else
							$node=$context.find(nodeThing.get(0));
				}
			}
			return $node;
		};
		/* ************************ */
		/*   	CONSTRUCTOR - Page	*/
		/* ************************ */
		(function(){})();
	};
	
	/* ************************ */
	/* 	Bind index.html events	*/
	/* ************************ */
	var _bind=function(){
		$(document).ready(function(){
			var frameWidthOffset=function(){
				return $(window).width() < 400 ? 250 : $(window).width() < 699 ? 110 : -50;
			};
			$(".iframe_info").colorbox({
				iframe : true,
				width : 552 - frameWidthOffset(),
				height : "500px"
			});
			$(".iframe_baja").colorbox({
				iframe : true,
				width : 552 - frameWidthOffset(),
				height : "340px"
			});
			$(".iframe_aviso").colorbox({
				iframe : true,
				width : 552 - frameWidthOffset(),
				height : "337px"
			});
			$(".iframe_cha").colorbox({
				iframe : true,
				width : 550 - frameWidthOffset(),
				height : "550px"
			});
			
			//----------------------PLACEHOLDERS----------------------
			if (!Modernizr.input.placeholder) {
				$("input").each(function(){
			      if($(this).val()=="" && $(this).attr("placeholder")!=""){
			        $(this).val($(this).attr("placeholder"));
			        $(this).focus(function(){
			          if($(this).val()==$(this).attr("placeholder")) $(this).val("");
			        });
			        $(this).blur(function(){
			          if($(this).val()=="") $(this).val($(this).attr("placeholder"));
			        });
			      }
			    });
				$("textarea").each(function(){
			      if($(this).val()=="" && $(this).attr("placeholder")!=""){
			        $(this).val($(this).attr("placeholder"));
			        $(this).focus(function(){
			          if($(this).val()==$(this).attr("placeholder")) $(this).val("");
			        });
			        $(this).blur(function(){
			          if($(this).val()=="") $(this).val($(this).attr("placeholder"));
			        });
			      }
			    });
			}
		});
	};
	
	/* ************************ */
	/* 	  PUBLIC - Start APP	*/
	/* ************************ */
	self.start=function(settings, onCmsStart){
		self.context=document;
		//Window vars
		window.base_url=settings.base_url;
		window.ria_url=settings.ria_url;
		window.contenido=settings.contenido;
		window.actual_loc=settings.actual_loc;
		//Bind index.html events
		_bind();
		//APP callback
		onCmsStart();
		//Init App Controller
		self.Controller=new self.Controller();
		self.Controller.load(settings.page||actual_loc);
		//Init History Controller
		self.History=new self.History();
		//Init Page Controller
		self.Page=new self.Page();
		//Init Form Controller
		self.Form=new self.Form();
		//Destroy start
		self.start=function(page,context){
			if(typeof context==='object')
				self.Controller.setContext(context);
			self.Controller.load(page);
		};
	};
	
};

if(typeof window.APP==="undefined")
	window.APP=new APP();
	
})();