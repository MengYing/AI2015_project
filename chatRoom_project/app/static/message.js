var msg_controller = new function(){
	var thisObj = this;
	//TODO: bind click event
	return thisObj = {
		init : function(){
			$(".msg").each(function(){
				$(this).bind("click",function(){
					showBar($(this));
				});
			});
		},
		addMessage : function(converse_id,str,direction,point){
			var color = getColor(point);
			var output = getMessageDiv(str,color,direction,converse_id);
			$('#chat_area').append(output);
			$('.msg[chat_id="' + converse_id + '"]').bind("click",function(){
				showBar($(this));
			});
		},
		updateMsgColor : function(converse_id,point){
			var color = getColor(point);
			var div = $(".msg[chat_id='" + converse_id + "']");
			$(div).css("color",color)
		},
		modifyMsgColor : function(){
			//user modify the color => post to server
			$.post();
		}
	};

	function print(str){
		console.log(str);
	}
	function getColor(point){
		return "red"
	}
	//handle the block:msg
	function getMessageDiv(str,color,direction,converse_id){
		var div = '<div></div>';
		var style = {"height":"auto", "background-color":"green", "color":"red"};
		var attr = {"chat_id":converse_id, "position":direction};
		div = $(div).addClass("msg").attr(attr).css(style);
		return setMessageContent(div,str);
	}
	//handle elements in block:msg
	function setMessageContent(div,str){
		var span = '<span>' + str + '</span>';
		span = $(span).addClass("msg_content");
		var block = panelUserSetPoint();
		return $(div).append(span).append(block);
	}
	function showBar(obj){
		$(obj).children(".msg_color_set").show();
		$(obj).unbind("click");
		$(obj).bind("click",function(){
			hideBar($(obj));
		});
	}
	function hideBar(obj){
		$(obj).children(".msg_color_set").hide();
		$(obj).unbind("click");
		$(obj).bind("click",function(){
			showBar($(obj));
		});
	}
	function panelUserSetPoint(){
		var block = '<div></div>';
		block = $(block).addClass("msg_color_set").css("display","none").append("lalala");
		return block
	}
};