from .models import Coffee


def delete_coffee_helper_func(email):
    '''
    A helper function to get delete the coffee object 
    whenever the user-manager obj gets deleted.
    '''
    if Coffee.objects.filter(store_manager_email=email).exists():
        Coffee.objects.filter(store_manager_email=email).delete()
