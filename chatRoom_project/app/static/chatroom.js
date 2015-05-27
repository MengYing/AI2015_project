function check(event){
	if(event.keyCode == 13){
		words = document.getElementById('input_msg').value;
		send(words);
		document.getElementById('input_msg').value = '';
	}
}

function send(words){
	
	// test version, not connected to db
	direc = getdir();
	container = document.createElement('div');
	container.setAttribute("class", "msg_container");
	container.setAttribute("align", direc);
	span = document.createElement('span');
	span.setAttribute("class", "msg_text");
	span.setAttribute("chat_id", 888);
	span.setAttribute("position", direc);
	span.setAttribute("align", "left");
	span.innerHTML = words;
	
	if(direc == 'left'){
		head = document.createElement('img');
		head.setAttribute("src", "static/sample1.jpg");
		head.setAttribute("class", "head");
		container.appendChild(head);
	}
	
	container.appendChild(span);
	chatarea = document.getElementById('chat_area');
	chatarea.appendChild(container);
	container.scrollIntoView();
}

// test version
i = 0;
function getdir(){
	if(++i%2==1) return 'left';
	return 'right';
}

// light & unlight
function light(div){
	div.style.backgroundColor = '#EBEBFF';
}

function unlight(div){
	div.style.backgroundColor = 'rgba(235, 245, 255, 0.16)';
}
