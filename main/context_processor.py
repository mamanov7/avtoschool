from main.models import Contact


def get_contact(request):
    context = {
        'contact': Contact.objects.first(),
    }
    return context
