from django.urls import include, path

from classroom.views import classroom, citizens, gendarmes

urlpatterns = [
    path('', include('classroom.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/citizen/', citizens.citizenSignUpView.as_view(), name='citizen_signup'),
    path('accounts/signup/gendarme/', gendarmes.gendarmeSignUpView.as_view(), name='gendarme_signup'),
]
