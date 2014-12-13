var nyc = {
    fullName: "New York City",
    mayor: "Bill de Blasio",
    population: 8000000,
    boroughs: 5
};

// write a for-in loop to print the value of nyc's properties
for (var list in nyc) {
    console.log(nyc[list]);   
}

// another example

var nyc = {
    fullName: "New York City",
    mayor: "Bill de Blasio",
    population: 8000000,
    boroughs: 5
};

for(var items in nyc) {
    console.log(items);   
}

// another example

var languages = {
    english: "Hello!",
    french: "Bonjour!",
    notALanguage: 4,
    spanish: "Hola!"
};

// print hello in the 3 different languages
for (var hello in languages) {
    if (typeof languages[hello] === "string") {
    console.log(languages[hello]); 
    };
};
