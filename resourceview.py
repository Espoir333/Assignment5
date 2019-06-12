 BIN +0 Bytes (100%) TechReviewProject/TechReviewApp/__pycache__/models.cpython-36.pyc 
Binary file not shown.
  BIN +44 Bytes (120%) TechReviewProject/TechReviewApp/__pycache__/urls.cpython-36.pyc 
Binary file not shown.
  BIN +292 Bytes (190%) TechReviewProject/TechReviewApp/__pycache__/views.cpython-36.pyc 
Binary file not shown.
  17  TechReviewProject/TechReviewApp/templates/TechReviewApp/types.html 
@@ -0,0 +1,17 @@
{% extends 'base.html' %}
{% block content %}
<h2>Product Types</h2>
<table class="table">
<tr>
    <th>Type Name</th>
    <th>Type Description</th>
</tr>
{% for t in types_list %}
  <tr>
      <td>{{ t.techtypename }}</td>
      <td>{{ t.techdescription }}</td>
  </tr>
  {% endfor %}
</table>

{% endblock %} 
  2  TechReviewProject/TechReviewApp/templates/base.html 
@@ -16,7 +16,7 @@ <h1>Tech Reviews</h1>
<a class="navbar-brand" href="{% url 'index' %}">Tech Reviews</a> 
</div> 
<ul class="nav navbar-nav"> 
<li>Dummy</li>
<li><a href="{% url 'types' %}">Types</a></li>
<li>Dummy</li> 
</ul> 
</div> 
  1  TechReviewProject/TechReviewApp/urls.py 
@@ -4,5 +4,6 @@
#this is a comment
urlpatterns=[
    path('', views.index, name='index'),
    path('getTypes/', views.getTypes, name='types')
]

  8  TechReviewProject/TechReviewApp/views.py 
@@ -1,5 +1,11 @@
from django.shortcuts import render
from .models import TechType, Product, Review

# Create your views here.
def index(request):
    return render(request, 'TechReviewApp/index.html') 
    return render(request, 'TechReviewApp/index.html')

def getTypes(request):
    types_list=TechType.objects.all()
    context={'types_list' : types_list }
    return render(request, 'TechReviewApp/types.html', context=context) 
