from django.urls import include, path

from .views import classroom, citizens, gendarmes

urlpatterns = [
    path('', classroom.home, name='home'),

    path('citizens/', include(([
        path('', citizens.QuizListView.as_view(), name='quiz_list'),
        path('interests/', citizens.citizenInterestsView.as_view(), name='citizen_interests'),
        path('taken/', citizens.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', citizens.take_quiz, name='take_quiz'),
    ], 'classroom'), namespace='citizens')),

    path('gendarmes/', include(([
        path('', gendarmes.QuizListView.as_view(), name='quiz_change_list'),
        path('quiz/add/', gendarmes.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', gendarmes.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', gendarmes.QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/', gendarmes.QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/question/add/', gendarmes.question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', gendarmes.question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', gendarmes.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'classroom'), namespace='gendarmes')),
]
