var user = prompt("What choice do you make? Chocolate, ice cream or fruits").toUpperCase();

switch (user)   {
    case 'CHOCOLATE':
        console.log("This is the best choice. Chocolate is awesome!");
        var darkChocolate = prompt("Do you like dark chocolate?").toUpperCase();
        var milkChocolate = prompt("Do you like milk chocolate?").toUpperCase();
        if (darkChocolate === "YES" && milkChocolate === "YES") {
            console.log("You are a true chocolate fan!");   
        } else  {
            console.log("You're still playing on team chocolate!")    
        }
    break;
    case 'ICE CREAM':
        console.log("Depends on the flavor. Careful not to get a brain freeze.");
    break;
    case 'FRUITS':
        console.log("This is the heathiest choice. You're a health nut!");
        var withSugar = prompt("Do you like your fruits with sugar?").toUpperCase();
        var withNothing = prompt("Do you eat fruits, straight from the tree?").toUpperCase();
        if (withSugar === "YES" || withNothing === "NO")   {
            console.log("You are still eating fruits, you health nut!");   
        } else  {
            console.log("You are doing very good, eating fruits");
        }
    break;
    default:
        console.log("Fool, didn't you see the three choices?");
}
