from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import *


class SuvlarAPIView(APIView):
    def get(self, request):
        suvlar=Suv.objects.all()
        serializer=SuvSerializer(suvlar, many=True)
        return Response(serializer.data)

    def post(self, request ):
        suv=request.data
        serializer=SuvSerializer(data=suv)
        if serializer.is_valid():
            data = serializer.validated_data
            Suv.objects.create(
                brend=data.get("brend"),
                narx=data.get("narx"),
                litr=data.get("litr"),
                batafsil=data.get("batafsil"),
            )
            return Response({'success': True, 'created_data': serializer.data})
        return Response({'success': False, 'errors': serializer.errors})


class WaterAPI(APIView):
    def get(self, request, pk):
        suv = Suv.objects.filter(id=pk)
        serializer = SuvSerializer(suv)
        return Response(serializer.data)

    def put(self, request, pk):
        suv = Suv.objects.filter(id=pk)
        serializer = SuvSerializer(suv.first(), data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            suv.update(
                brend=data.get("brend"),
                narx=data.get("narx"),
                litr=data.get("litr"),
                batafsil=data.get("batafsil"),
            )
            serializer = SuvSerializer(suv.first())
            return Response({'success': True, 'updated_data': serializer.data})
        return Response({'success': False, 'errors': serializer.errors})


class MijozlarAPIView(APIView):
    def get(self, request):
        mijozlar = Mijoz.objects.all()

        search=request.query_params.get("search")

        if search is not None:
            mijozlar=Mijoz.objects.filter(
                Q(ism__icontains=search)|
                Q(tel__icontains=search)
            )

        serializer = MijozSerializer(mijozlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        mijoz = request.data
        serializer = MijozSerializer(data=mijoz)
        if serializer.is_valid():
            data = serializer.validated_data
            Mijoz.objects.create(
                ism=data.get("ism"),
                tel=data.get("tel"),
                manzil=data.get("manzil"),
                qarz=data.get("qarz"),
                user=data.get("user"),
            )
            return Response({'success': True, 'created_data': serializer.data})
        return Response({'success': False, 'errors': serializer.errors})


class ClientAPI(APIView):
    def get(self, request, pk):
        mijoz = Mijoz.objects.filter(id=pk)
        serializer = MijozSerializer(mijoz)
        return Response(serializer.data)



    def put(self, request, pk):
        mijoz = Mijoz.objects.filter(id=pk)
        serializer = MijozSerializer(mijoz.first(), data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            mijoz.update(
                ism=data.get("ism"),
                tel=data.get("tel"),
                manzil=data.get("manzil"),
                qarz=data.get("qarz"),
                user=data.get("user"),
            )
            serializer = SuvSerializer(mijoz.first())
            return Response({'success': True, 'updated_data': serializer.data})
        return Response({'success': False, 'errors': serializer.errors})


class BuyurtmaModelViewSet(ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer


class AdmintmaModelViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class HaydovchiModelViewSet(ModelViewSet):
    queryset = Haydovchi.objects.all()
    serializer_class = HaydovchiSerializer






