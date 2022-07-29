// Get the modal
// var modal = document.getElementById("myModal");
// var btn = document.getElementById("myBtn");
// var span = document.getElementsByClassName("close")[0];
// btn.onclick = function() {
//   modal.style.display = "block";
  
//   modal.style.transition="all .3s linear"
// }
// // Jab user clicks on <span> (x), close the modal
// span.onclick = function() {
//   modal.style.display = "none";
// }
// // Jab User will click model ke bahar
// window.onclick = function(event) {
//   if (event.target == modal) {
//     modal.style.display = "none";
//   }
// }

// ---------------Model working ends here-------------

var modal = document.getElementById("myModal");
var btn = document.getElementById("myBtn");
var span = document.getElementsByClassName("close")[0];
btn.onmouseover = function() {
  modal.style.display = "block";
  
  modal.style.transition="all .3s linear"
}
// Jab user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}
// Jab User will click model ke bahar
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}