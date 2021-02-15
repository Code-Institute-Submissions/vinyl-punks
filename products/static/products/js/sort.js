(function () {
    "use strict";
    $('.sort-by').click(function () {
        let sortMethod = $(this);
        let currentUrl = new URL(window.location);

        selectedVal = $(sortMethod).attr("data-value");
        let sort = selectedVal.split("-")[0];
        let direction = selectedVal.split("-")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    })
})();