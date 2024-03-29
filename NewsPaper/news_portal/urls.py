from django.urls import path
from .views import (PostList,
                    PostDetail,
                    PostSearch,
                    PostCreate,
                    PostUpdate,
                    PostDelete,
                    AppointmentView,
                    CategoryDetailView,
                    subscribe)

urlpatterns = [
    path('', PostList.as_view(), name='news'),
    path('search/', PostSearch.as_view(), name='search'),
    path('add/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('make_appointment/', AppointmentView.as_view(), name='make_appointment'),
    path('categories/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),

]
