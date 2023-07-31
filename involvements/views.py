from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from involvements.forms import InvolvementForm
from .models import Involvement
from django.shortcuts import render, get_object_or_404

def add_involvement(request, user_id):
    # Check if the user exists
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        # Handle if the user does not exist (you can redirect to an error page or show an error message)
        return render(request, 'user_not_found.html')

    if request.method == 'POST':
        form = InvolvementForm(request.POST)
        if form.is_valid():
            # Create a new Involvement object and associate it with the user
            involvement = form.save(commit=False)
            involvement.user = user
            involvement.save()

        # print(involvement)
        # Redirect to a success page or the user's profile page
        return redirect('users-home')
    form = InvolvementForm()
    return render(request, 'involvements/add_involvement.html',{'form' : form, 'user_id': user_id })

def view_involvements(request, user_id):
    # Get the user or return a 404 error if not found
    user = get_object_or_404(User, pk=user_id)
    # Get all involvements associated with the user
    involvements = Involvement.objects.filter(user=user)

    return render(request, 'involvements/view_involvements.html', {'user': user, 'involvements': involvements})

def update(request, involvement_id):
    involvement = get_object_or_404(Involvement, pk=involvement_id)
    user = involvement.user
    if request.method == 'POST':
        form = InvolvementForm(request.POST, instance=involvement)
        if form.is_valid():
            form.save()
            involvements = Involvement.objects.filter(user=user)
            return render(request, 'involvements/view_involvements.html', {'user': user, 'involvements': involvements})
    else:
        form = InvolvementForm(instance=involvement)

    return render(request, 'involvements/update.html',{'form' : form })

def delete(request, involvement_id):
    inv = get_object_or_404(Involvement, pk=involvement_id)
    user = inv.user
    inv.delete()
    involvements = Involvement.objects.filter(user=user)
    return render(request, 'involvements/view_involvements.html', {'user': user, 'involvements': involvements})