from django.shortcuts import render


# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


def guidebook(request):
    return render(request, 'guidebook.html')

def grandopening(request):
    return render(request, 'launching.html')

def grandclosing(request):
    return render(request, 'closing.html')


def bad_request_view(request, exception):
    context = {
        'title': '400 | Bad Request',
        'message': 'There was a problem with your request.'
    }
    return render(request, 'error.html', status=400, context=context)


def permission_denied_view(request, exception):
    context = {
        'title': '403 | Forbidden',
        'message': 'You don\'t have access to view this page.'
    }
    return render(request, 'error.html', status=403, context=context)


def page_not_found_view(request, exception):
    context = {
        'title': '404 | Page not Found',
        'message': 'Seems like this page does not exist.'
    }
    return render(request, 'error.html', status=404, context=context)


def server_error_view(request):
    context = {
        'title': 'Oh noes!',
        'message': 'Something went wrong. We apologize for the inconvenience.'
    }
    return render(request, 'error.html', status=500, context=context)