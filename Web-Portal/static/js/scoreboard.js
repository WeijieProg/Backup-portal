
var tabs = document.querySelectorAll(".scoreboard_tabs ul li");
var maze_1 = document.querySelector(".maze_1");
var maze_2 = document.querySelector(".maze_2");
var maze_3 = document.querySelector(".maze_3");
var items = document.querySelectorAll(".scoreboard_item");

tabs.forEach(function(tab){
	tab.addEventListener("click", function(){
		var current_tab = tab.getAttribute("data-li");

		tabs.forEach(function(tab){
			tab.classList.remove("active");
		})

		tab.classList.add("active");

		items.forEach(function(item){
			item.style.display = "none";
		})

		if(current_tab == "maze_1"){
			maze_1.style.display = "block";
		}
		else if(current_tab == "maze_2"){
			maze_2.style.display = "block";
		}
		else{
			maze_3.style.display = "block";
		}

	})
})