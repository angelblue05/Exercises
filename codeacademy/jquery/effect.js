$(document).ready(function() {
    $('div').click(function() {
        $(this).effect('explode');    
    }); 
});

// another example

$(document).ready(function() {
    $('div').click(function() {
        $(this).effect('bounce', {times:3}, 500);    
    }); 
});
