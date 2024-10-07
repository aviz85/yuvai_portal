from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Creation, Comment
from .forms import CreationForm, CommentForm

class CreationListView(ListView):
    model = Creation
    template_name = 'core/creation_list.html'
    context_object_name = 'creations'
    paginate_by = 10

class CreationDetailView(DetailView):
    model = Creation
    template_name = 'core/creation_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

class CreationCreateView(CreateView):
    model = Creation
    form_class = CreationForm
    template_name = 'core/creation_form.html'
    success_url = reverse_lazy('creation_list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

@login_required
def add_comment(request, pk):
    creation = get_object_or_404(Creation, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.creation = creation
            comment.author = request.user
            comment.save()
            return redirect('creation_detail', pk=pk)
    return redirect('creation_detail', pk=pk)