(function () {
    "use strict";

    // Disable cart preview when viewing the cart
    $("#dropdown-cart").prop("disabled", true);

    $(function () {
        $('[data-toggle="tooltip"]').tooltip();
    });

    /* Get initial quantities of each product */
    var inputs = $(".quantity-input");
    var prevValues = [];
    /* Get current values */
    for (let i = 0; i < inputs.length; i++) {
        prevValues.push(inputs[i].value);
    }

    /* Check for change in quantity */
    setInterval(function () {
        for (let i = 0; i < inputs.length; i++) {
            let currentValue = inputs[i].value;
            if (prevValues[i] != currentValue) {
                prevValues[i] = currentValue;
                currentValue = parseInt(currentValue);
                let form = $(inputs[i]).parent();
                if (inputs[i].checkValidity() && Number.isInteger(currentValue)) {
                    form.submit();
                }
                else {
                    $(inputs[i]).next().text("Enter quantity between 0 and 10");
                }
            }
        }
    }, 500);
})();