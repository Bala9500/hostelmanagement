from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('tenantdetails/',views.tenantdetails,name='tenantdetails'),
    path('reportdetails/',views.reportdetails,name='reportdetails'),
    path('logout/',views.logout,name='logout'),
    path('report/',views.report,name='report'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('update-report-status/<int:id>/',views.update_report_status,name='update_report_status'),
]

