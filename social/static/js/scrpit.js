document.getElementById('deleteProfileBtn').addEventListener('click', function() {
    document.getElementById('deleteProfilePopup').style.display = 'block';
   });
   
   document.getElementById('cancelDelete').addEventListener('click', function() {
    document.getElementById('deleteProfilePopup').style.display = 'none';
   });
   
   // Optionally, you can also add functionality to close the popup when clicking outside of it
   window.addEventListener('click', function(event) {
    if (event.target == document.getElementById('deleteProfilePopup')) {
       document.getElementById('deleteProfilePopup').style.display = 'none';
    }
   });