from django.urls import path
from . import views

urlpatterns = [
  
    path('',views.homeview,name='home'),
    path('notes/',views.notesview,name='notes'),
    path('delete-note/<int:pk>',views.deletenotes,name="delete-note"), #<int:id>
    path('notes_detail/<int:pk>',views.notesdetailsview.as_view(),name="notes-detail"),
    path('edit_notes/<int:pk>',views.editnotes,name="edit-notes"),
    path('homework/',views.homework,name='homework'),
    path('update_homework/<int:pk>',views.update_homework,name='update-homework'),
    path('delete_homework/<int:pk>',views.delete_homework,name='delete-homework'),
    path('edit_homework/<int:pk>',views.edithomework,name='edit-homework'),
    path('youtube',views.youtubeview,name='youtube'),
    path('books',views.booksview,name='books'),
    path('dictionary',views.dictionaryview,name='dictionary'),
    path('wiki',views.wikiview,name='wiki'),
    path('register',views.registerview,name='register')


]