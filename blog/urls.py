from django.urls import path
from .views import HomePageView, PostPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post_detail/<int:pk>', PostPageView.as_view(), name='post_detail'),
]