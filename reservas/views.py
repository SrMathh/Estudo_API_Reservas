from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from reservas.models import Table, Reservation
from reservas.serializers import TableSerializer , ReservationSerializer

# Viewset para gerenciar CRUD completo de mesas
class TableView(viewsets.ModelViewSet):
    queryset = Table.objects.all().order_by('number')
    serializer_class = TableSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['number']

# Viewset para gerenciar CRUD completo de reservas
class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all().order_by('reservation_date')
    serializer_class = ReservationSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['client']# Busca pelo cliente
    filterset_fields = ['table', 'reservation_date', 'status']# Filtro por data e mesa
    ordering_fields = ['reservation_date']  # Permitir ordenação por data