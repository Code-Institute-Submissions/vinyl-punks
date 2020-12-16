let stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
let clientSecret = $("#id_client_secret").text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
    base: {
        color: '#32325d',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#fa755a',
        iconColor: '#fa755a'
    }
};
let card = elements.create("card", { style: style });

card.mount("#card-field");

card.addEventListener("change", function (e) {
    let errorContainer = $("#card-error");
    if (e.error) {
        let html = `<i class="fas fa-exclamation-circle"></i>
                    <span>${e.error.message}`;
        $(errorContainer).append(html);
    } else {
        errorContainer.text("")
    }
});

var form = document.getElementById("payment-form");
form.addEventListener("submit", function (event) {
    event.preventDefault();
    card.update({ "disabled": true });
    $("#submit-btn").attr("disabled", true)
    $(form).fadeToggle(100);
    $("#loading-overlay").fadeToggle(100);
    payWithCard(stripe, card, clientSecret);
});

var payWithCard = function (stripe, card, clientSecret) {

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card
        }
    }).then(function (result) {
        if (result.error) {
            let errorContainer = $("#card-error");
            let html = `<i class="fas fa-exclamation-circle"></i>
            <span>${result.error.message}`;
            $(errorContainer).append(html);
            $(form).fadeToggle(100);
            $("#loading-overlay").fadeToggle(100);
            card.update({ "disabled": false });
            $("#submit-btn").attr("disabled", false)
        } else {
            form.submit();
        }
    });
};

