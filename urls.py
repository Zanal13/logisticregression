from django.http import JsonResponse
from django.shortcuts import render

class APIException(Exception):
    def __init__(self, status_code, error_code=None, message=None):
        self.status_code = status_code
        self.error_code = error_code
        self.message = message
        super().__init__(self)

def handle_api_error(exception):
    if exception.status_code == 400:
        error_description = generate_error_description_400(exception)
    elif exception.status_code == 500:
        error_description = generate_error_description_500(exception)
    else:
        error_description = 'Unhandled error'

    return error_description

def generate_error_description_400(exception):
    if exception.error_code == 'SOME_ERROR':
        return 'Error description for SOME_ERROR'
    elif exception.error_code == 'ANOTHER_ERROR':
        return 'Error description for ANOTHER_ERROR'
    else:
        return 'Generic error description for 400 errors'

def generate_error_description_500(exception):
    return 'Generic error description for 500 errors'

def get_user(request, user_id):
    try:
        # Get user data based on user_id
        if user_id == 1:
            user_data = {'name': 'John Doe', 'email': 'johndoe@example.com'}
            return JsonResponse(user_data)
        else:
            raise APIException(400, error_code='USER_NOT_FOUND')
    except APIException as e:
        error_description = handle_api_error(e)
        print(str(e))  # Print the error to console
        return render(request, 'error.html', {'error': str(e), 'error_description': error_description})
    except Exception as e:
        print(str(e))  # Print the error to console
        return JsonResponse({'error': str(e)}, status=500)

def update_user(request, user_id):
    try:
        # Update user data based on user_id
        if user_id == 1:
            # Perform update operation
            return JsonResponse({'message': 'User updated successfully'})
        else:
            raise APIException(400, error_code='USER_NOT_FOUND')
    except APIException as e:
        error_description = handle_api_error(e)
        print(str(e))  # Print the error to console
        return render(request, 'error.html', {'error': str(e), 'error_description': error_description})
    except Exception as e:
        print(str(e))  # Print the error to console
        return JsonResponse({'error': str(e)}, status=500)
