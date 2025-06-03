from django.shortcuts import render, redirect, get_object_or_404
from .models import Lead
from django.contrib.auth.models import User

def lead_list(request):
    leads = Lead.objects.all()
    users = User.objects.all()

    # Поиск по имени
    query = request.GET.get('q')
    if query:
        leads = leads.filter(name__icontains=query)

    # Фильтр по статусу
    status = request.GET.get('status')
    if status:
        leads = leads.filter(status=status)

    # Фильтр по исполнителю
    assignee = request.GET.get('assignee')
    if assignee:
        leads = leads.filter(assignee_id=assignee)

    return render(request, 'leads/lead_list.html', {
        'leads': leads,
        'users': users,
        'current_status': status,
        'current_assignee': assignee,
        'current_query': query,
    })
def create_lead(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        status = request.POST.get('status')
        information = request.POST.get('information')
        assignee_id = request.POST.get('assignee')

        assignee = None
        if assignee_id:
            assignee = User.objects.get(id=assignee_id)

        Lead.objects.create(
            name=name,
            status=status,
            information=information,
            assignee=assignee
        )
        return redirect('lead_list')

    users = User.objects.all()
    return render(request, 'leads/create_lead.html', {'users': users})
    
def add_to_queue(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    lead.in_queue = True
    lead.save()
    return redirect('lead_list')

def lead_update(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    users = User.objects.all()

    if request.method == 'POST':
        lead.name = request.POST.get('name')
        lead.status = request.POST.get('status')
        lead.information = request.POST.get('information')
        assignee_id = request.POST.get('assignee')
        lead.assignee = User.objects.get(id=assignee_id) if assignee_id else None
        lead.save()
        return redirect('lead_list')

    return render(request, 'leads/lead_update.html', {'lead': lead, 'users': users})