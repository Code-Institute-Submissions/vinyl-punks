from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle webhooks from stripe """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle generic webhook """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle successful payment intent webhook """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """ Handle generic webhook """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
