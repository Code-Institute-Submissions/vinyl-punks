(function () {
    "use strict";

    setRatings();
    // Update a review with AJAX/POST
    $(".fa-edit").click(function () {
        hideFormAndButtons();
        setSelects();
        let productId = $(this).data("product-id");
        let actionIcons = $(this).closest("div").addClass("d-none");
        let ratingId = $(this).closest("div").siblings(".rating-wrapper").data("rating-id");
        let ratingWrapper = $(this).closest("div").siblings(".rating-wrapper");
        let contentPara = $(this).closest(".review").children(".review-content").addClass("d-none");
        let textArea = $(this).closest(".review").children("textarea").removeClass("d-none");
        let ratingSelect = $(this).closest(".review").children("select").removeClass("d-none");
        let saveButton = $(this).closest(".review").children("button").removeClass("d-none");
        $(".save").click(function () {
            var newText = $(textArea).val();
            var newRating = $(ratingSelect).val();
            newText = $.trim(newText);
            if (newText.length >= 4 && newText != "") {
                let url = "update_review/" + productId + "/" + ratingId + "/";
                let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
                let postData = {
                    "content": newText,
                    "rating": newRating,
                    "csrfmiddlewaretoken": csrfToken,
                };
                $.post(url, postData).done(function (success) {
                    $(ratingWrapper).data("rating", success.updated_rating);
                    $(contentPara).text(newText).removeClass("d-none");
                    $(textArea).addClass("d-none");
                    $(saveButton).addClass("d-none");
                    $(ratingSelect).addClass("d-none");
                    $(actionIcons).removeClass("d-none");
                    resetRatings();
                    setRatings();
                }).fail(function () {
                    location.reload();
                });

            } else {
                alert("Review must contain a minimum of 5 characters.");
            }
        });

    });

    // Prevent multiple reviews to be editable simultanously
    function hideFormAndButtons() {
        $(".rating").addClass("d-none");
        $(".action-icons").removeClass("d-none");
        $(".update-textarea").addClass("d-none");
        $(".review-content").removeClass("d-none");
        $(".save").addClass("d-none").unbind();
    }

    // Reset ratings before setting new rating (in case new rating is higher)
    function resetRatings() {
        let ratingIcons = $(".rating-icon");
        for (let i = 0; i < ratingIcons.length; i++) {
            if (!$(ratingIcons[i]).hasClass("text-secondary")) {
                $(ratingIcons[i]).addClass("text-secondary");
            }
        }
    }

    // Display current ratings
    function setRatings() {
        let ratingWrappers = $(".rating-wrapper");
        for (let i = 0; i < ratingWrappers.length; i++) {
            let ratingNumber = $(ratingWrappers[i]).data("rating");
            let ratingIcons = $(ratingWrappers[i]).children();
            for (let j = 0; j < ratingNumber; j++) {
                $(ratingIcons[j]).removeClass("text-secondary");
            }
        }
    }

    // Pre-select current rating option
    function setSelects() {
        let ratingWrappers = $(".rating-wrapper");
        let ratingSelects = $(".rating");
        for (let i = 0; i < ratingSelects.length; i++) {
            let options = $(ratingSelects[i]).children();
            let ratingNumber = $(ratingWrappers[i]).data("rating");
            for (let j = 0; j < options.length; j++) {
                if ($(options[j]).val() == ratingNumber) {
                    $(options[j]).prop("selected", true);
                }
            }

        }
    }

    // Delete review with AJAX and remove from DOM
    $(".delete-review-btn").click(function () {
        let reviewWrapper = $(this).closest(".modal").prev(".review");
        let reviewId = $(this).data("review-id");
        let url = "/delete_review/" + reviewId + "/";
        $.ajax({
            url: url, success: function (result) {
                $(reviewWrapper).remove();
            }, error: function () {
                location.reload();
            }
        });
    });
})();