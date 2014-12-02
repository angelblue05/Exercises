/*jshint multistr:true */

var text = "Hey, how are you \
doing? My name is Tamara. I'm sorry \
you haven't head what I said. My name \
is Tamara.";

var myName = "Tamara"
var hits = []

for (var i = 0; i < text.length; i++) {
    if (myName[0] === text[i]) {
        
        var characterSave = "";
        for (var j = i; j < myName.length + i; j++) {
            characterSave = text[j];
            hits.push(characterSave);  
        }
    }
}

if (hits.length === 0) {
    console.log("Your name wasn't found!");   
}
else    {
    console.log(hits);   
}
