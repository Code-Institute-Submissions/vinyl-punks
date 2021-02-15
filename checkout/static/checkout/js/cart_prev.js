(function () {
    "use strict";

    /* Hide delete icons in cart preview */
    let cartDeleteIcons = $(".delete-icon");
    for (let i = 0; i < cartDeleteIcons.length; i++) {
        $(cartDeleteIcons[i]).addClass("d-none");
    }
})();