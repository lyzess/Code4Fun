var cakeprice= new Array();
cakeprice["cake6"]= 20;
cakeprice["cake8"]= 25;
cakeprice["cake10"]= 35;
cakeprice["cake12"]= 75;

function sizecakeprice()
{
    var priceofcake= 0;
    var fromhtml= document.forms["fieldcake"];
    var chosencake= fromhtml.elements["sizeofcake"];
    for(var i=0; i<chosencake.length; i++)
    {
        if (chosencake[i].checked)
        {
            priceofcake= cakeprice[chosencake[i].value];
            break;
        }
    }
    return priceofcake;
}

var fillingprice= new Array();
fillingprice["none"]= 0;
fillingprice["fill1"]= 7;
fillingprice["fill2"]= 5;
fillingprice["fill3"]= 8;
fillingprice["fill4"]= 12;

function fillingcakeprice()
{
    var priceoffilling= 0;
    var fromhtml= document.forms["fieldcake"];
    var chosenfilling= fromhtml.elements["filling"];
    
    priceoffilling= fillingprice[chosenfilling.value];
    return priceoffilling;
}

function candlecakeprice()
{
    var candleprice= 0;
    var fromhtml= document.forms["fieldcake"];
    var chosencandle= fromhtml.elements["candle"];
    if (chosencandle.checked==true)
    {
        candleprice= 5;
    }
    return candleprice;
}

function inscriptioncakeprice()
{
    var inscriptionprice= 0;
    var fromhtml= document.forms["fieldcake"];
    var beingchosen= fromhtml.elements["inscription"];
    if (beingchosen.checked==true)
    {
        inscriptionprice= 20;
    }
    return inscriptionprice;
}

function totalprice()
{
    var total= sizecakeprice() +fillingcakeprice() +candlecakeprice() +inscriptioncakeprice();
    var display= document.getElementById("displaytotalprice");
    display.innerHTML= "Total price for cake: RM "+total;
}

function Submit()
{
    var total= sizecakeprice() +fillingcakeprice() +candlecakeprice() +inscriptioncakeprice();
    alert("Thank you for buying with us! Total price for cake: RM "+total);
}