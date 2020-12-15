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
let card = elements.create("card", {style: style});

card.mount("#card-field");

card.addEventListener("change", function(e) { 
    let errorContainer = $("#card-error");
    if (e.error) {
        let html = `<i class="fas fa-exclamation-circle"></i>
                    <span>${e.error.message}`;
        $(errorContainer).append(html)
    } else {
        errorContainer.text("")
    }
});