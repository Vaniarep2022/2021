from django.shortcuts import render

def blog_detail(request):
    return render(request, 'blog_detail.html')

def blog_index(request):
    user_text=request.GET['username']
    blog_index=user_text[::-1]
    return render(request,'blog_index.html', {'word':blog_index})