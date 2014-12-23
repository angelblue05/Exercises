var xhr = new XMLHttpRequest();
xhr.open("GET", "http://www.codecademy.com/", false);
// Add your code below!
xhr.send();
console.log(xhr.status);
console.log(xhr.statusText);

// another example

// Add your code below this line!
var xhr = new XMLHttpRequest();
xhr.open("GET", "http://www.codecademy.com/", false);
xhr.send();

// Add your code above this line!

console.log(xhr.status);
console.log(xhr.statusText);
