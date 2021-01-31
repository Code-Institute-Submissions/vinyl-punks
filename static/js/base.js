(function () {
    "use strict";

    /* Enable messages (toasts) */
    $('.toast').toast('show');
    setTimeout(function () {
        $(".toast").toast("dispose");
    }, 8000);

    /* Toggle cart-preview */
    $("#dropdown-cart").click(function () {
        displayCart();
    });

    function displayCart() {
        $("#cart-preview").fadeToggle(200);
    }

    /* Remove item form cart-preview */
    $(".delete-icon").click(function () {
        let item_id = $(this).data('product');
        let productRow = $(this).closest(".row");
        $.ajax({
            url: "delete_from_cart/" + item_id + "/?ajax=true", success: function () {
                $(productRow).remove();
                getContexts();
            }
        });
    });

    /* Get contexts from server */
    function getContexts() {
        $.ajax({
            url: "cart_contents/?ajax=true", success: function (result) {
                let total = parseFloat(result.total);
                let delivery = parseFloat(result.delivery);
                let grandTotal = parseFloat(result.grand_total);
                total = total.toFixed(2);
                delivery = delivery.toFixed(2);
                grandTotal = grandTotal.toFixed(2);
                $(".preview-total").text("$" + total);
                $(".preview-delivery").text("$" + delivery);
                $(".preview-grand-total").text("$" + grandTotal);
                $(".cart-item-counter").text(result.product_count);
                if (result.product_count == "0") {
                    $(".cart-item-counter").addClass("d-none");
                    $(".cart-header").text("Your cart is empty");
                    $(".checkout-btn").addClass("disabled");
                    $(".update-cart-btn").addClass("d-none");
                }
            }
        });
    }
})();
