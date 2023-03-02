
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BooksSerializer

from .models import Books


# Create your views here.

@api_view(['GET'])
def apiOverwiev(request):
    api_urls = {
        'List': '/book-list/',
        'Detail View': '/book-detail/<str:pk>/',
        'Create': '/book-create/',
        'Update': '/book-update/<str:pk>/',
        'Delete': '/book-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['POST'])
def bookCreate(request):
    serializer = BooksSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def bookList(request):
    tasks = Books.objects.all().order_by('-id')
    serializer = BooksSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def bookDetail(request, pk):
    tasks = Books.objects.get(id=pk)
    serializer = BooksSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['PATCH', 'PUT'])
def bookUpdate(request, pk):
    task = Books.objects.get(id=pk)
    serializer = BooksSerializer(instance=task, data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def bookDelete(request, pk):
    task = Books.objects.get(id=pk)
    task.delete()

    return Response('Item udalen')

# Create your views here.
