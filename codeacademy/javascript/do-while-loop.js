var lookLeft = true;

var getToDaChoppa = function(){
  // Write your do/while loop here!
    do {
        console.log("Look to the left, do you see the Choppa?");   
    }
    while (lookLeft)    {
        console.log("I don't see it!");
        console.log("You then realize, the Choppa is to your right!");
        var lookLeft = false;
    };
};

getToDaChoppa();
