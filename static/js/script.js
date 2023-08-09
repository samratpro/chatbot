
function opennav(){
    
    document.getElementById("sidbar-control").style.display = "block";
    document.getElementById("opennav-id").style.display = "none";
    document.getElementById("dashcontent").classList.remove("col-sm-12");
    document.getElementById("dashcontent").classList.add("col-sm-9");
};

function closenav(){
    document.getElementById("opennav-id").style.display = "block";
    document.getElementById("sidbar-control").style.display = "none";
    document.getElementById("dashcontent").classList.remove("col-sm-9");
    document.getElementById("dashcontent").classList.add("col-sm-12");

};