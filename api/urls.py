from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.journal_views import Journals, JournalDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('journals/', Journals.as_view(), name='journals'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('journals/<int:pk>/', JournalDetail.as_view(), name='journal_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
