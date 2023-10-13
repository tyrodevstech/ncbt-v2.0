def get_profile_image(request):
    student = ''
    if hasattr(request.user, 'studentregistrationuni' ):
        student = 'uni'
    elif hasattr(request.user, 'studentregistrationcollage'):
        student = 'clg'

    context = {
        'student': student
    }

    return context