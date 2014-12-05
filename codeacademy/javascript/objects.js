var friends = {
bill: {
    firstName: 'Bill',
    lastName: 'Buffalo',
    number: "(433) 555-5555",
    address: ['One Microsoft Way', 'Redmond', 'WA', '98052']
    },
steve: {
    firstName: 'Steve',
    lastName: 'Smith',
    number: "(406) 555-5555",
    address: ['Two Google circle', 'San Francisco', 'FL', '96056']
    },
};

var list = function () {
    for  (var name in friends) {
            console.log(name);
    }
};

var search = function (name) {
    for (var lookUp in friends) {
        if(friends[lookUp].firstName === name) {
            console.log(friends[lookUp]);
            return friends[lookUp];
        }
    }
};

search("Bill");


// help us make snoopy using literal notation
// Remember snoopy is a "beagle" and is 10 years old.
var snoopy = {
    species: "beagle",
    age: 10
};

// help make buddy using constructor notation
// buddy is a "golden retriever" and is 5 years old
var buddy = new Object();
buddy.species = "golden retriever";
buddy.age = 5;
