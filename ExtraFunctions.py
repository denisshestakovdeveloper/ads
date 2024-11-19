from .models import *
def get_main_user(request):
    sys_user = request.user
    main_user = User.objects.filter(sys_user = sys_user.id).first()
    return main_user