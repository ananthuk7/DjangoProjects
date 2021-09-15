from django.shortcuts import redirect


def user_authentication(func):
    def wrapper(request, id=None, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('signin')
        else:
            return func(request, id, *args, **kwargs)
    return wrapper
