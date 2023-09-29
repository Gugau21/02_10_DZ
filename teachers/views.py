from django.http import HttpResponse
from teachers.models import Teacher

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the students index.")
def teachers_view(request):
    teachers = Teacher.objects.order_by("id")
    text = " ".join([str(q)+"<br>" for q in teachers])
    return HttpResponse(text)