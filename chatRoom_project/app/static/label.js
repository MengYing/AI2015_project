//var choice = 'None';
//var label_post = 'None';
var reason = 'None';
var category = ['Meeting', 'Lecture', 'Study', 'Empty'];
var expression = ['開會', '上課', '自習/休閒', '無活動'];
var initial = false;
const GENERAL = '#33FFFF';
const CHOSEN = '#91C7FF';


// get label_post from he left side

document.addEventListener("keyup", keyup, false);
function keyup(event){
	var value = document.getElementById('reason').value;
	if(value == "") value = 'None';
	reason = value;
	//document.getElementById('word1').innerHTML = value;
	//document.getElementById('open').style.display = 'none';
}
/*
function setdefaultvalue(label){
	label_post = label;
	document.getElementById('open').style.display = 'none';
}

function clearchoice(){
	choice = 'None';
	label_post = 'None';
	$('.choice').removeClass('active');
	document.getElementById('open').style.display = 'none';
}

function setupchoice(button){
	choice = button.getAttribute("value");
	label_post = choice;
	if(choice == 'Others')
		document.getElementById('open').style.display = 'block';
	$(button).addClass("active");
}

function light(button){
	if(choice == button.getAttribute("value")){
		clearchoice();
	}else{
		clearchoice();
		setupchoice(button);
	}
}
*/
function refreshchoice(){
	//choice = 'None';
	//label_post = 'None';
	reason = 'None';
	//document.getElementById('next').innerHTML = 'Next';
	//document.getElementById('word1').innerHTML = '';
	document.getElementById('reason').value = "";
	//clearchoice();
}


// main part

var timestamp;

function replace(page){
	document.write(page);
	document.close();
}

function record(){
	//console.log(label_post);
	console.log(reason);
	/*
	if(label_post == 'None'){
		alert('請選擇一個活動類別');
		return;
	}
	*/
	if(reason == 'None' || reason == ""){
		alert('請填寫答案');
		return;
	}
	var timediff = new Date().getTime() - timestamp;
	var pic = document.getElementById('pic');
	$.post("/record/"+pic.getAttribute('value')+"/"+timediff+"/"+reason, function(response){
		//console.log(response);
		//console.log(response.pic);
		if(typeof(response) == 'string') replace(response);
		setpic(response.pic, response.idx, response.ttl, response.ques);
	});
	refreshchoice();
}

function show(s, idx, ttl){
	return '('+idx+'/'+ttl+')  '+s.substring(0,4)+'/'+s.substring(4,6)+'/'+s.substring(6,8)+' '+s.substring(9,11)+':'+s.substring(11,13);
}

function setpic(newpic, newidx, ttlidx, question){
	console.log(question);
	document.getElementById('question').innerHTML = question;
	
	picObj = document.getElementById('pic');
	picObj.setAttribute("value", newpic);
	picObj.src = "http://disa.csie.ntu.edu.tw/~janetyc/data/"+newpic.substring(0,8)+"/image_"+newpic+".jpg";
	document.getElementById('time').innerHTML = show(newpic, newidx, ttlidx);
	timestamp = new Date().getTime();
    document.getElementById("reason").focus();
    if (!initial) {
        initial = true;
        document.getElementById("reason").addEventListener('keypress', function (e) {
            var key = e.which || e.keyCode;
            if (key === 13) { // 13 is enter
            record();
            }
        });
    }
	/*
	picObj.onerror = function(){ 
		$.getJSON('/newpic', function(response){
			setpic(response.pic);
		});
	}
	*/
}


// initiating
/*		
function buildup(){
	upper = document.getElementById('upper');
	choicecontainer = document.createElement("div");
	choicecontainer.setAttribute("class", "btn-group");
	for(i=0; i<category.length; ++i){
		middle = document.createElement("button");
		middle.setAttribute("class", "choice btn btn-lg btn-default");
		middle.setAttribute("value", category[i]);
		middle.setAttribute("onclick", "light(this)");
		middle.innerHTML = expression[i];
		choicecontainer.appendChild(middle);
	}
	upper.appendChild(choicecontainer);
}*/
