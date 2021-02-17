from django.http import JsonResponse
from rest_framework.decorators import api_view
import rest_framework.renderers

from todo_app.models import Tutorial






@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def tutorial_detail(request, pk):
    # find tutorial by pk (id)
    try:
        tutorial = Tutorial.objects.get(pk=pk)
    except Tutorial.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # GET / PUT / DELETE tutorial


