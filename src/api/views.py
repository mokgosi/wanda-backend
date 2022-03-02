from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, serializers, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (APIView, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.settings import import_from_string

from .models import Wander
from .models import Testimonial
from .models import Page

from .serializers import TestimonialSerializer
from .serializers import WanderSerializer
from .serializers import UserSerializer
from .serializers import PageSerializer


class TestimonialViewSet(viewsets.ModelViewSet):

    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)


class WanderViewSet(viewsets.ModelViewSet):

    queryset = Wander.objects.all()
    serializer_class = WanderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)


class PageViewSet(viewsets.ModelViewSet):

    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    





'''
class TestimonialViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, 
                         mixins.CreateModelMixin, mixins.RetrieveModelMixin, 
                         mixins.UpdateModelMixin, mixins.DestroyModelMixin):


    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

'''
'''
class TestimonialViewSet(viewsets.ViewSet):

    def list(self, request):
        testimonials = Testimonial.objects.all()
        serializer = TestimonialSerializer(testimonials, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TestimonialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Testimonial.objects.all()
        testimonial = get_object_or_404(queryset, pk=pk)
        serializer = TestimonialSerializer(testimonial)
        return Response(serializer.data)

    def update(self, request, pk=None):
        testmonial = Testimonial.objects.get(pk=pk)
        serializer = TestimonialSerializer(testmonial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        testimonial = Testimonial.objects.get(pk=pk)
        testimonial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''


'''
class TestimonialList(generics.GenericAPIView, mixins.ListModelMixin, 
                                               mixins.CreateModelMixin):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class TestimonialDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, 
                        mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)
'''
'''
class TestimonialList(APIView):

    def get(self, request):
        testimonials = Testimonial.objects.all()
        serializer = TestimonialSerializer(testimonials, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TestimonialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestimonialDetail(APIView):

    def get_object(self, id):
        try:
            return Testimonial.objects.get(id=id)
        except Testimonial.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        testimonial = self.get_object(id)
        serializer = TestimonialSerializer(testimonial)
        return Response(serializer.data)

    def put(self, request, id):
        testimonial = self.get_object(id)
        serializer = TestimonialSerializer(testimonial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        testimonial = self.get_object(id)
        testimonial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
