$(document).ready(function() {
    var $paragraph = $("<p>Text after number one</p>");
    $('#one').after($paragraph);
    $('#two').after($paragraph);
});
