from django.urls import path
from .views import RoomListView, BookingListView, RoomDetailView, CancelBookingView

app_name = 'hotel'

urlpatterns = [
    # path('room_list/',RoomList.as_view(), name='RoomList'),
    # path('homepage/',HomePageView, name='HomePageView'),
    path('room_list/',RoomListView, name='RoomListView'),
    path('booking_list/',BookingListView.as_view(), name='BookingListView'),
    # path('book/', BookingView.as_view(), name='Booking_view'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(), name='CancelBookingView'),
]