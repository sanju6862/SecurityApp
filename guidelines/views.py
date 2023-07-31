from django.shortcuts import render, redirect, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from guidelines.forms import DocumentForm, GuidelineForm
from .models import Guideline, Document, Media

@login_required
def guideline_list(request):
    guidelines = Guideline.objects.all()
    documents = Document.objects.all()
    media = Media.objects.all()
    
    return render(request, 'guidelines/guideline_list.html', {
        'guidelines': guidelines,
        'documents': documents,
        'media': media,
    })


@login_required
def add_guideline(request):
    if request.method == 'POST':
        form = GuidelineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guideline_list')
    else:
        form = GuidelineForm()
    return render(request, 'guidelines/add_guideline.html', {'form': form})


@login_required
def add_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('guideline_list')
    else:
        form = DocumentForm()
    return render(request, 'guidelines/add_document.html', {'form': form})


@login_required
def update_guideline(request, guideline_id):
    guideline = get_object_or_404(Guideline, pk=guideline_id)

    if request.method == 'POST':
        form = GuidelineForm(request.POST, instance=guideline)
        if form.is_valid():
            form.save()
            return redirect('guideline_list')
    else:
        form = GuidelineForm(instance=guideline)

    return render(request, 'guidelines/update_guideline.html', {'form': form, 'guidline': guideline})


@login_required
def delete_guideline(request, guideline_id):
    guideline = get_object_or_404(Guideline, pk=guideline_id)
    guideline.delete()
    return redirect('guideline_list')


@login_required
def delete_resource(request, resource_id):
    resource = get_object_or_404(Document, pk=resource_id)
    resource.delete()
    return redirect('guideline_list')