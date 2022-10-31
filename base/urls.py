from django.urls import path
from . import views

urlpatterns = [

	path( '', views.home, name = 'home' ),

	path( 'profile/', views.profile, name = 'profile' ),

	path( 'posts/', views.posts, name = 'posts' ),

	path( 'post/<int:id>', views.post, name = 'post' ),

	path( 'sign-up/', views.signUp, name = 'sign-up' ),

	path( 'sign-in/', views.signIn, name = 'sign-in' ),

]
