const navLinksBlock = document.querySelector(".nav-links-block-open");

function showNavLinks(){
    if(navLinksBlock.style.display == "block"){
        navLinksBlock.style.display = "none";
    }
    else{
        navLinksBlock.style.display = "block";
    }
}