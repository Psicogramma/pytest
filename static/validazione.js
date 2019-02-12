function checkForm(){
    var nameBox;
    for (i = 1; i <= 16; i++) {
        var  nameBox ="d"+i;
        var x = document.getElementsByName(nameBox);
	      if(!x[0].checked && !x[1].checked && !x[2].checked && !x[3].checked && !x[4].checked) {
            alert("Hai dimenticato di rispondere a qualche domanda");
            return false;
        }
    }
    return true;
}