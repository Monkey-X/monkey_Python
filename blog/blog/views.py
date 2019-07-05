from django.shortcuts import render

def page_not_found(request):
    return render_to_response('404.html',{"content":"this is 404 error"})