from django.shortcuts import render

arr_posts = [

	{ 'id': 1, 'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam' },
	{ 'id': 2, 'text': 'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur' },
	{ 'id': 3, 'text': 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum' },

]

def home(request):

    return render( request, 'home.html' )

def profile(request):

    return render( request, 'posts.html' )

def posts(request):

    return render( request, 'posts.html', { 'posts' : arr_posts } )

def post(request, id):

    return render( request, 'post.html', { 'id' : id, 'post': arr_posts[id-1] } )

def signUp(request):

    return render( request, 'sign-up.html' )

def signIn(request):

    return render( request, 'sign-in.html' )

