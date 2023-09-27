from RecipesProject.UsersApp.models import UserProfile


def profile_pic(request):
    if request.user.is_authenticated:
        try:
            profile_pics = request.user.userprofile.profile_pic.url
        except UserProfile.DoesNotExist:
            profile_pics = None
    else:
        profile_pics = None

    return {'profile_pics': profile_pics}
