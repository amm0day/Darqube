from django.http import JsonResponse, HttpResponseBadRequest
from user_management.models import UserModel
from django.views.decorators.csrf import csrf_exempt
from bson import ObjectId


def get_user(request, u_id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = UserModel.get_by_objectId(u_id)
    except UserModel.DoesNotExist:
        return HttpResponseBadRequest()

    return JsonResponse(user.to_dict())

@csrf_exempt
def create_user(request):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        first_name, last_name, email = request.POST["first_name"], request.POST["last_name"], request.POST["email"]
    except KeyError as err:
        return HttpResponseBadRequest(f"Field {err} is not defined")

    new_user = UserModel.objects.create(first_name=first_name, last_name=last_name, email=email)

    return JsonResponse({"user_id": str(new_user.pk)})
