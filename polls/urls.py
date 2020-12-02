from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    #path(route, view, name)
    path('', views.index, name='index'),
    #a partir de ahora no sola se le pasara a request sino tambien question id
    #request =<HttpRequest object>, question_id = 34
    #polls/34/
    path('<int:question_id>/', views.detail, name='detail'),

    #polls/34/detail/
    path('<int:question_id>/results/',views.results, name= 'results'),

    #polls/34/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
