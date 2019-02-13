
    
        function checkForm() {
            var groupRadio = ($('input[type="radio"]').length/5);
            if($("input:checked").length==groupRadio) return true;
                    else{alert("Hai dimenticato qualcosa"); return false;}
         
        }