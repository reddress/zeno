from .models import AccountType

def accountTypes(request):
    if request.user:
        return {'userAccountTypes': AccountType.objects.filter(owner=request.user)}
    return {'userAccountTypes': []}
