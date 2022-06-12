window.onload = function(){}
var btn = document.querySelector("#btn");
btn.onclick = function(){
    var div= document.createElement("div");
    div.innerHTML = generateit();
    document.getElementById("box").appendChild(div);
}

function generateit()
{
    return "<input type='text' class='txt' placeholder='Enter party name' required>&nbsp<input type='text' class ='txt1' placeholder = 'Enter region' required>&nbsp<input type='text' class='txt2' placeholder='Enter name' required>&nbsp<button id ='btn' onclick='removeit(this);'>Remove</button>";
}

function removeit(btn)
{
    document.getElementById("box").removeChild(btn.parentNode);
}

values =[]
values1 =[]
values2 =[]
function data1(){
    var x = document.querySelectorAll(".txt")
    for(var i=0;i<x.length;i++)
    { 
        values[i] = x[i].value;
    }
  
}

function data2(){
    var y = document.querySelectorAll(".txt1")
    for(var j=0;j<y.length;j++)
    { 
        values1[j] = y[j].value;
    }
  
}

function data3(){
    var z= document.querySelectorAll(".txt2")
    for(var k=0;k<z.length;k++)
    { 
        values2[k] = z[k].value;
    }  
document.write(values);
document.write(values1);
document.write(values2);
}



