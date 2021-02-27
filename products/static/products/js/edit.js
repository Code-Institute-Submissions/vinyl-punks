(function () {
    "use strict";
    
    $(function () {
        $('[data-toggle="tooltip"]').tooltip();
    });

    setInputName();

    // Add another input
    let input = `
                <div class="m-2 input-wrapper">
                <p class="mb-2">Title</p>
                <input type="text" class="track-input" aria-label="track title" required>
                <i class="fas fa-times fa-lg text-danger remove-input"></i>
                </div>
                `;
    $("#add-input").click(function () {
        $(".track-inputs").append(input);
        setInputName();
        eventListenerRemoveInput();
    });

    // Add eventlistener for added input
    function eventListenerRemoveInput() {
        $(".remove-input").click(function () {
            $(this).closest(".input-wrapper").remove();
            setInputName();
        });
    }

    // Set individual name of input based on number of inputs
    function setInputName() {
        let inputs = $(".track-input");
        for (let i = 0; i < inputs.length; i++) {
            $(inputs[i]).attr("name", "track" + (i + 1));
        }
    }
})();