from functools import wraps
from rest_framework.exceptions import PermissionDenied


def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(view_instance, request, *args, **kwargs):
            # Check if the user has the required role
            if not request.user.is_authenticated or request.user.role != role:
                raise PermissionDenied("You do not have permission to perform this action.")
            return func(view_instance, request, *args, **kwargs)

        return wrapper

    return decorator
