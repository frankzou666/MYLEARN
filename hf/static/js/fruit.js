
// bind event at window.onload
window.onload=function() {


    //change background color
    var fruitTrs = document.getElementsByClassName("fruitTr");
    for (var i = 0; i < fruitTrs.length; i++) {
        // first we udpate the subtotal
        var tds = fruitTrs[i].cells;
        tds[3].innerText=parseInt(tds[1].innerText) * parseInt(tds[2].innerText);
        //bind event to every element
        fruitTrs[i].onmouseover = chnagefruitTrsBGColors;
        fruitTrs[i].onmouseleave = clearfruitTrsBGColors;
    }

    //delete Element
    var delImages = document.getElementsByClassName("delImage");
    for (var i = 0; i < delImages.length; i++) {
        //bind event to every element
        delImages[i].onclick = delElementBydelImage;
    }

     //change mouse cursor and onclick update subtotal price
    var pricePers = document.getElementsByClassName("pricePer");
    for (var i = 0; i < pricePers.length; i++) {
        //bind event to every element
        pricePers[i].onmouseover = changeMouseCursorForpricePer;
        pricePers[i].onclick = updatePricePer;
    }

    // add new addFruitItem
    confirmBtn.onclick = addFruitItem;
    //update totalPrice
    updateTotalPrices();


}


function delElementBydelImage() {
     //delete Event
     if (event && event.srcElement && event.srcElement.tagName=='IMG'){
         var img = event.srcElement;
         var td = img.parentElement;
         var tr = td.parentElement;
         tr.remove();
     }

}

function chnagefruitTrsBGColors() {
     //actually we put on event on TR, but we can only see tr tag

     if (event && event.srcElement && event.srcElement.tagName=='TD'){
         // we can only get tr from gd
         var tr = event.srcElement.parentElement;
         // get all td from tr, and change color to white
         var tds = tr.cells;
         tr.style.backgroundColor="navy";
         for (var i=0;i<tds.length ; i++){
             tds[i].style.color="white";
         }

     }

}

function  clearfruitTrsBGColors(){
    if (event && event.srcElement && event.srcElement.tagName=='TR'){
         // we can only get tr from gd
         var tr = event.srcElement;
         tr.style.backgroundColor="transparent";
         var tds = tr.cells;
         for (var i=0;i<tds.length ; i++){
             tds[i].style.color="black";
         }
     }
}


// change mouse cursor
function changeMouseCursorForpricePer(){
     if (event && event.srcElement && event.srcElement.tagName=='TD'){
         var td=  event.srcElement;
         td.style.cursor="hand";
     }
}

function updatePricePer(){
    if (event && event.srcElement && event.srcElement.tagName=='TD'){
         var td=  event.srcElement;
         //get orgin value,only when we modify value
         if (td.firstChild && td.firstChild.nodeType==3 && td.className=="pricePer"){
             var value = td.innerText;
            //why do you set "size" instead of 'width'?
             td.innerHTML="<input type='text' size='2'>";
             var input = td.firstChild;
             input.value=value;
             // selectd the value when do we get
             input.select();
             //element lost focus,update subtotal
             input.onblur = updatePrice;


         }

     }

}


function updatePrice(){
    if (event && event.srcElement && event.srcElement.tagName=='INPUT'){
        var input = event.srcElement;
        var newValue = input.value;
        var priceTd = input.parentElement;
        // get gr
        var tr = priceTd.parentElement;
        // get tds
        var tds = tr.cells
        priceTd.innerText = newValue;
        //update subtotal value;
        tds[3].innerText=parseInt(tds[1].innerText) * parseInt(tds[2].innerText);

        //update total
        updateTotalPrices();

    }

}


// update total value
function updateTotalPrices(){
    var subTotals = document.getElementsByClassName("subTotal");
    var totalPrices = document.getElementsByClassName("totalPrice");
    var sum = 0;
    for (var i = 0; i < subTotals.length; i++) {
        sum = sum + parseInt(subTotals[i].innerText);
    }
    totalPrices[0].innerText=sum;
}

function addFruitItem(){
    var tableAddFruitItem = event.srcElement.parentElement.parentElement.parentElement;
    var tblFruit =  document.getElementById("tblFruit");
    //get value from input element , you should not use innerText
    var fnameValue = document.getElementById("fname").value;
    var fpricePer = document.getElementById("fpricePer").value;
    var fcount = document.getElementById("fcount").value;

    newRow = tblFruit.insertRow(tblFruit.rows.length-1);
    newRow.align="center";
    newRow.className="fruitTr";
    var cell0 = newRow.insertCell(0);
    var cell1 = newRow.insertCell(1);
    var cell2 = newRow.insertCell(2);
    var cell3 = newRow.insertCell(3);
    var cell4 = newRow.insertCell(4);
    cell1.className="pricePer";
    cell3.className="subTotal";
    cell0.innerText = fnameValue;
    cell1.innerText = fpricePer;
    cell2.innerText = fcount;
    cell3.innerText = parseInt(fpricePer) * parseInt(fcount);
    cell4.innerHTML= tblFruit.rows[1].cells[4].innerHTML;
    cell4.firstChild.onclick = delElementBydelImage
    newRow.onmouseover = chnagefruitTrsBGColors;
    newRow.onmouseleave = clearfruitTrsBGColors;
    newRow.onclick = updatePricePer;
    updateTotalPrices();
    //update total



}