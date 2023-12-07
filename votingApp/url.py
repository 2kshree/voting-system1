from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('reg',views.register,name='reg'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('aadhaar',views.aadhaar,name='aadhaar'),
    path('aadhaar1',views.aadhaar_next,name='aadhaar1'),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    path('voters',views.voters,name='voters'),
    path('voterlist',views.voterlist,name='voterlist'),
    path('voter_details/<int:code>',views.voter_details,name='voter_details'),
    path('mine_block/<int:code>',views.mine_block,name='mine_block'),
    path('view_chain',views.view_chain,name='view_chain'),
    path('adminpage',views.admin1,name='adminpage'),
]