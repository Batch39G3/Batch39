window.onload = function () {};
var btn = document.querySelector("#btn");
btn.onclick = function () {
  var div = document.createElement("div");
  div.innerHTML = generateit();
  document.getElementById("box").appendChild(div);
};

function generateit() {
  return "<input type='text' class='txt' placeholder='Enter party name' required>&nbsp<input type='text' class ='txt1' placeholder = 'Enter region' required>&nbsp<input type='text' class='txt2' placeholder='Enter name' required>&nbsp<button id ='btn' onclick='removeit(this);'>Remove</button>";
}

function removeit(btn) {
  document.getElementById("box").removeChild(btn.parentNode);
}

values = [];
values1 = [];
values2 = [];
function data1() {
  var x = document.querySelectorAll(".txt");
  for (var i = 0; i < x.length; i++) {
    values[i] = x[i].value;
  }
}

function data2() {
  var y = document.querySelectorAll(".txt1");
  for (var j = 0; j < y.length; j++) {
    values1[j] = y[j].value;
  }
}

function data3() {
  var z = document.querySelectorAll(".txt2");
  for (var k = 0; k < z.length; k++) {
    values2[k] = z[k].value;
  }
}

function check() {

    console.log('This is the function being called');
    var val1 = values.toString();
    var val2 = values1.toString();
    var val3 = values2.toString();
    var jsonData = JSON.stringify({"value1": val1, "value2": val2, "value3": val3});
    // console.log('{{url_for('admin')}}');
    // var jsonData = "{value1:" +  val1 + ", value2:" + val2 + ", value3:" + val3 + "}";
    $.ajax({
      type: 'POST',
    //   url: "{{ url_for("admin")}}",
    //   url: "http://localhost:8081/",
      url: "/admin",
      data: jsonData,
    //   data: jsonData,
      dataType: "text",
    //   contentType : "application/json",
    });
}