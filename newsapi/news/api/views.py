from rest_framework            import status
from rest_framework.decorators import api_view
from rest_framework.response   import Response

from news.api.models           import Article
from news.api.serializers      import AticleSerializer

@api_view(["GET"])
def article_list_create_api_view(request):
    if request.mathod == "GET":
        articles = Article.objects.filter(active=True)
        serializer = serializer(articles)
        return Response(serializer.data)