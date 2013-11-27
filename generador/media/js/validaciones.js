function validar() {
            var estaTodoOK = true;

            if (document.getElementById("username_login").value.length<8 || document.getElementById("password_login").value.length<8){
            	estaTodoOK = false;
            }

            if (!estaTodoOK) {
                    alert("la longitud de nombre de usuario y de contraseña debe ser mayor a 8");        
            }
            return estaTodoOK;
        }