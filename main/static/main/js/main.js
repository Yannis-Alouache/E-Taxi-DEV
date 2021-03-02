$( document ).ready(function() {
    const myInput = document.getElementsByClassName("my-input");
    var number = document.getElementById('tel-number');
    let i;
    

    for( i = 0; i < myInput.length; i++ ){
        myInput[i].addEventListener('focus', function(){ 
            var id = this.dataset.id;
            $(".input-icon")[id].classList.add("phone-number-icon-focus");
            console.log("Button n°", id );
         });
    }

     $('.my-input').on("blur", function() {
        $(".input-icon").removeClass("phone-number-icon-focus");
    });

    // Listen for input event on numInput.
    number.onkeydown = function (e) {
        if (!((e.keyCode > 95 && e.keyCode < 106) ||
                (e.keyCode > 47 && e.keyCode < 58) ||
                e.keyCode == 8)) {
            return false;
        }
    }
});




