// Get the popup
var popup = document.getElementById('popup');

// get the image
var img = document.getElementById('img');
var popImg = document.getElementById("img1");
var caption = document.getElementById("caption");
img.onclick = function(){
    popup.style.display = "block";
    popImg.src = this.src;
    caption.innerHTML = this.alt;
}

// get the element that closes the popup
var span = document.getElementsByClassName("close")[0];

// to close the pop up
span.onclick = function() { 
    popup.style.display = "none";
}

