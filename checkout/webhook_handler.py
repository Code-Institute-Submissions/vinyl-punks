from django.http import HttpResponse


class StripeWH_handler:
    """ Handle webhooks from stripe """

    def __init__(self, request):
        self.request = request


    def handle_event(self, event):
        """ Handle generic webhook """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
