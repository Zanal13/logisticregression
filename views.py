import time
class SessionUpdateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'last_update_time' not in request.session:
            request.session['last_update_time'] = time.time()
        elif time.time() - request.session['last_update_time'] > 10:
            request.session['last_update_time'] = time.time()
            # update session value here

        response = self.get_response(request)
        return response
