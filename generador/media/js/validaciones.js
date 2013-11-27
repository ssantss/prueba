function validar() {
            var minOcho = true;
            var maxTreinta = true;

            if (document.getElementById("username_login").value.length<8 || document.getElementById("password_login").value.length<8){
            	minOcho = false;
            }

            if (document.getElementById("username_login").value.length>30 || document.getElementById("password_login").value.length>30){
            	maxTreinta = false;
            }

            if (!minOcho) {
                    alert("la longitud de nombre de usuario y de contraseña debe ser mayor a 8");        
            }

            if (!maxTreinta) {
                    alert("la longitud de nombre de usuario y de contraseña debe ser menor de 30");        
            }

            return minOcho;
        }

function option_selected(sel) {
        var option = sel.options[sel.selectedIndex].value;
        alert("You selected: " + option);
        $('#content_to_pop').load("{% url 'users_view' option %}");
}