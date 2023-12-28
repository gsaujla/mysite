from django.contrib import admin
from django.urls import path, include
from .views import firsthello, q_detail, results, vote , index

urlpatterns=[
    path('',index,name="first5"),
    path('<int:q_id>/', q_detail,name = "only_qid"),
    path('<int:q_id>/results/', results,name = "only_qid"),
    path('<int:q_id>/vote/', vote ,name = "only_qid"),

]