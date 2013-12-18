function validar_register(){
    var menor = true;
    var mayor = true;
    var email = document.getElementById('email');
    var va_email = revisarEmail(email);

    var username = document.getElementById('username');
    var va_username = true;
    va_username = val_espacios(username);
    if(document.getElementById('username').value.length<8 || document.getElementById('passwordone').value.length<8 || document.getElementById('passwordtwo').value.length<8 ){
            menor = false;
            alert("la longitud de nombre de usuario y de contraseña debe ser mayor a 8");
    }
    if(document.getElementById('username').value.length>30 || 
        document.getElementById('passwordone').value.length>30 || 
        document.getElementById('passwordtwo').value.length>30 ){
            mayor = false;
            alert("la longitud de nombre de usuario y de contraseña debe ser menor de 30");
    }
    return ((menor && mayor) && (va_email && va_username));
}

function validar_modificacion(){
    var menor = true;
    var mayor = true;
    var email = document.getElementById('email');
    var va_email = revisarEmail(email);
    
    if(document.getElementById('passwordone').value.length<8 || 
        document.getElementById('passwordtwo').value.length<8 ){
            menor = false;
            alert("la longitud de nombre de usuario y de contraseña debe ser mayor a 8");
    }
    if(document.getElementById('passwordone').value.length>30 || 
        document.getElementById('passwordtwo').value.length>30 ){
            mayor = false;
            alert("la longitud de nombre de usuario y de contraseña debe ser menor de 30");
    }
    return (menor && mayor && va_email);
}

function validar_password(){
    var isok = true;
    if(document.getElementById('passwordone').value != document.getElementById('passwordtwo').value){
        isok = false;
        alert("LAS CONTRASEÑAS NO SON IGUALES"); 
    }
    return  isok;
}

function revisarEmail(elemento) {
    var isCorrecto = true;
    if (elemento.value!="") {
        var dato = elemento.value;
        var expresion = /^([a-zA-Z0-9_\.-])+@(([a-zA-Z])+)\.([a-zA-Z]{2,3})(\.([a-zA-Z]{2,3}))?$/;
        if (!expresion.test(dato)) {
            alert('email incorrecto');
            isCorrecto = false;
        } 
    }
    else{
        alert("Debe asignar un email al usuario");
        isCorrecto = false;
    }
    return isCorrecto;
}

function val_espacios(Obj)
{
    var texto = Obj.value;
    var texto_limpio = texto.replace(/^\s+|\s+$/g,"");
    if (texto_limpio==""){
        Obj.focus(); 
        alert("Debe asignar un username");       
        return false;
    }
    return true;
}

function val_new_user () {    
    var vr = validar_register();
    var vp = true;
    if (vr) {
        vp = validar_password();
    }

    return (vp && vr);   
}

function val_edit_user () {    
    var vr = validar_modificacion();
    var vp = true;
    if (vr) {
        vp = validar_password();
    }

    return (vp && vr);   
}

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


function validar_edit() {
    var estaTodoOK = true;

    if (document.getElementById("id_new_password1").value.length<8 || document.getElementById("id_new_password2").value.length<8){
        estaTodoOK = false;
        alert("la longitud debe ser mayor a 8 en ambos campos");
    }

    if (document.getElementById("id_new_password1").value.length>30 || document.getElementById("id_new_password2").value.length>30){
        estaTodoOK = false;
        alert("la longitud debe ser menor de 30 en ambos campos");
    }
    return estaTodoOK;
}

//<a href="{% url 'logout_view' %}" class="link">Salir</a>