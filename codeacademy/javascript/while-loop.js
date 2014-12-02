var understand = true;

while(understand === true){
	console.log("I'm learning while loops!");
	understand = false;
}

// another challenge

//Remember to set your condition outside the loop!
var three = true
var msg = "I'm looping!"

var loop = function(){
	while(three){
	    for (var i = 1; i < 4; i++) {
		console.log(msg);
	    };
	    three = false;
	};
};

loop();

// another challenge

var loopOnce = true;

var soloLoop = function(){
  while (loopOnce) {
        console.log("Looped once!");
        loopOnce = false;
  }
  
};

soloLoop();
