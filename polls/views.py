from django.http import HttpResponse, HttpResponseRedirect

from .models import Question, Choice
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)
#     #return HttpResponse("Hello, world. You're at the polls index.")
#Tutorial 3>>
#from django.template import loader
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

#Oficial using method render to do more easily
from django.shortcuts import render 
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    #render dos parametros> objecto request y la plantilla,  y uno opcional para el contexto
    return render(request, 'polls/index.html', context)

from django.http import Http404
#Tutorial # 3
def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})
    
    #ide = "You're at the Question: " + str(question_id)
    #return render(request, 'polls/detail.html', {'ide':ide, 'num':question_id})

 #Keni, recuerde que %s significa lo que sigue imprimire en lugar de eso
def results(request, question_id):
    try:
        #El intentara solicitar un id, si no existe levantara un error
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("La Question: " + str(question_id) + ",  no existe")

    return render(request, 'polls/result.html', {'question': question })


##ESTE  METHOD ES EL MAS USADO
# from django.shortcuts import get_object_or_404
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/result.html', {'question': question})


from django.shortcuts import get_object_or_404, render
from django.urls import reverse
def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        #usted debe saber que request.Post es un objeto diccionario
        #que permite acceder a los dats mediante una name clave
        #en este caso choice, que fue declarado por name en el html 
        #y retorna el ID de la opcion seleccionada
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/result.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #Siempre debes retornar un HttpResponseRedirect
        #Para evitar que un bobo de hackee esas cosas

        return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))


#Tu sabes estas vistas son funciones cuyo parametro request es el que devolvera HttpResponse
# y question_id sera lo que se le pase opcional
