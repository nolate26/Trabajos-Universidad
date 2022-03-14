function botonhistograma(){
    var histogramas = document.getElementById("Histogramas");
    var densidad = document.getElementById("Densidad");
    
    if (histogramas.style.display == "none") {
        if (densidad.style.display != "none"){
            densidad.style.display = "none";
        }
        
        histogramas.style.display="";
        ScrollReveal({cleanup: true}).reveal('.contenedor_foto1',{delay: 500});
        
    
    } else if (histogramas.style.display == "") {
        histogramas.style.display = "none";
    }


    
}
//incluir -> ScrollReveal.


function botondensidad(){
    var histogramas = document.getElementById("Histogramas");
    var densidad = document.getElementById("Densidad");

    if (densidad.style.display == "none"){
        if (histogramas.style.display != "none"){
            histogramas.style.display = "none";
        }

        densidad.style.display = "";
        ScrollReveal({cleanup: true}).reveal('.contenedor_foto2',{delay: 500});

    } else if (densidad.style.display == "") {
        densidad.style.display = "none";
    }
}


function escondertodo() {
    var grafWatching = document.getElementById("grafico1_3");
    var grafCompleted = document.getElementById("grafico2_3");
    var grafPlan = document.getElementById("grafico3_3");
    var grafShingeki = document.getElementById("graficoShingeki");
    var grafSteins = document.getElementById("graficoSteins");
    var grafGintama = document.getElementById("graficoGintama");
    var grafFullmetal = document.getElementById("graficoFullmetal");
    var grafHunter = document.getElementById("graficoHunter");
    var grafScore = document.getElementById("grafico1_4");
    var grafWatching2 = document.getElementById("grafico2_4");
    var grafCompleted2 = document.getElementById("grafico3_4");
    var grafPlan2 = document.getElementById("grafico4_4");

    if (grafWatching.style.display != "none"){
        grafWatching.style.display = "none";
    }
    if (grafCompleted.style.display != "none"){
        grafCompleted.style.display = "none";
    }
    if (grafPlan.style.display != "none"){
        grafPlan.style.display = "none";
    }
    if (grafShingeki.style.display != "none"){
        grafShingeki.style.display = "none";
    }
    if (grafSteins.style.display != "none"){
        grafSteins.style.display = "none";
    }
    if (grafGintama.style.display != "none"){
        grafGintama.style.display = "none";
    }
    if (grafFullmetal.style.display != "none"){
        grafFullmetal.style.display = "none";
    }
    if (grafHunter.style.display != "none"){
        grafHunter.style.display = "none";
    }
    if (grafScore.style.display != "none") {
        grafScore.style.display = "none";
    }
    if (grafWatching2.style.display != "none") {
        grafWatching2.style.display = "none";
    }
    if (grafCompleted2.style.display != "none") {
        grafCompleted2.style.display = "none";
    }
    if (grafPlan2.style.display != "none") {
        grafPlan2.style.display = "none";
    }
    //console.log("Se acaba de borrar las imagenes");

}

function lista1(evento) {
    var grafWatching = document.getElementById("grafico1_3");
    var grafCompleted = document.getElementById("grafico2_3");
    var grafPlan = document.getElementById("grafico3_3");
    var grafShingeki = document.getElementById("graficoShingeki");
    var grafSteins = document.getElementById("graficoSteins");
    var grafGintama = document.getElementById("graficoGintama");
    var grafFullmetal = document.getElementById("graficoFullmetal");
    var grafHunter = document.getElementById("graficoHunter");


    switch (evento.value){
        case "":
            escondertodo();
            break;
        
        case "Shingeki":
            escondertodo();
            grafShingeki.style.display = "";
            break;
        
        case "Steins":
            escondertodo();
            grafSteins.style.display = "";
            break;
        
        case "Gintama":
            escondertodo();
            grafGintama.style.display = "";
            break;
        
        case "Fullmetal":
            escondertodo();
            grafFullmetal.style.display = "";
            break;
        
        case "Hunter":
            escondertodo();
            grafHunter.style.display = "";
            break;
        
        case "Watching":
            escondertodo();
            grafWatching.style.display = "";
            break;
        
        case "Completed":
            escondertodo();
            grafCompleted.style.display = "";
            break;
        
        case "Plan to Watch":
            escondertodo();
            grafPlan.style.display = "";
            break;
        
        
    }
}

function lista2(evento) {
    var grafScore = document.getElementById("grafico1_4");
    var grafWatching2 = document.getElementById("grafico2_4");
    var grafCompleted2 = document.getElementById("grafico3_4");
    var grafPlan2 = document.getElementById("grafico4_4");

    switch (evento.value) {
        case "":
            escondertodo();
            break;

        case "Score":
            escondertodo();
            grafScore.style.display = "";
            //console.log("Mostrando " + evento.value);
            break;

        case "Watching":
            escondertodo();
            grafWatching2.style.display = "";
            //console.log("Mostrando " + evento.value);
            break;

        case "Completed":
            escondertodo();
            grafCompleted2.style.display = "";
            //console.log("Mostrando " + evento.value);
            break;

        case "Plan to Watch":
            escondertodo();
            grafPlan2.style.display = "";
            //console.log("Mostrando " + evento.value);
            break;

        
    }


}



var fullmetalmode = false;
function botondark() {
    //Esta función se encarga de activar el modo "Fullmetal Alchemist: Brotherhood"

    var encabezado = document.getElementById("encabezado");
    var botondark = document.getElementById("botondark");


    if (fullmetalmode == false) {
        console.log("Fullmetal Alchemist Mode activado!");

        encabezado.style.backgroundColor = "#ac090993";
        encabezado.style.color = "white";
        encabezado.style.fontFamily = "GravTrac";
        
        botondark.textContent = "Normal Mode";
        
        document.body.style.backgroundImage = "url(./img/fma.jpg)";
        document.body.style.color = "white";

        fullmetalmode = true;
    } else if(fullmetalmode == true){
        console.log("Fullmetal Alchemist Mode desactivado!");

        encabezado.style.backgroundColor = "#17DD9B";
        encabezado.style.color = "black";
        encabezado.style.fontFamily = "Zen Dots";

        document.body.style.backgroundImage = "";
        document.body.style.color = "black";
        
        botondark.textContent = "Fullmetal Alchemist: Brotherhood Mode";

        fullmetalmode = false;
    }



}