document.addEventListener("DOMContentLoaded", function () {
    const reservationButton = document.getElementById("show-reservations");
    
    reservationButton.addEventListener("click", function () {
      const checkboxes = document.querySelectorAll(".table-box-button");
      
      checkboxes.forEach(function (checkbox) {
        checkbox.checked = true;
      });
    });
  });
  