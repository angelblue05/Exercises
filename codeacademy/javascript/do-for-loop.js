// Write your code below!

var loopWhile = true;
var loopDo = true;

do  {
    console.log("We're looping!");   
} while (loopDo = false);

for (var i = 1; i < 3; i++) {
    console.log("We're looping " + i + "x faster!");   
}

while (loopWhile) {
    console.log("Feeling dizzy, stopping looping");
    var loopWhile = false;
}
