var myNodelist = document.getElementsByTagName("LI");
var i;

var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
}
function newElement() {
  var li = document.createElement("li");
  var t=document.createElement("input")
  t.type='checkbox';
  t.setAttribute('id','checking');

  li.appendChild(t);
  var inputValue = document.getElementById("myInput").value;
  var tlab = document.createElement("label");
  tlab.innerHTML=inputValue;
  li.appendChild(tlab);
  if (inputValue === '') {
    alert("You must write or copy-past sth");
  } else {
    document.getElementById("myUL").appendChild(li);
  }
  document.getElementById("myInput").value = "";
  var span = document.createElement("SPAN");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}

function Delete()
    {
        var close = document.getElementsByClassName("close");
        var i;
        for (i = 0; i < close.length; i++)
        {
            close[i].parentElement.style.display = "none";
        }
    }