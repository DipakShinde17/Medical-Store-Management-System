from .models import Settings

def global_settings(request):

    setting = Settings.objects.first()

    return {
        "setting": setting
    }