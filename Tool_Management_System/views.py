from django.http import JsonResponse
from django.shortcuts import render
from toolmanagement_app.models import Tool
from software_usage_tracking.models import SystemMonitor
from django.db.models import Q
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            if 'open_time' in data and data['open_time']:
                SystemMonitor.objects.create(
                    system_number=data.get('system_number'),
                    user=data.get('user'),
                    processid=data.get('processid'),
                    date=data.get('date'),
                    software=data.get('software'),
                    open_time=data.get('open_time'),
                    close_time=data.get('close_time', None)
                )
            if 'close_time' in data and data['close_time']:
                monitor_entry = SystemMonitor.objects.filter(processid=data['processid']).first()
                if monitor_entry:
                    monitor_entry.close_time = data['close_time']
                    monitor_entry.save()

            return JsonResponse({"message": "Data successfully stored in the database."}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


def software_usage_tracking(request):
    if request.method == "POST":
        searchSystem_number = request.POST.get('searchSystem_number')
        searchUser = request.POST.get('searchUser')
        searchDate = request.POST.get('searchDate')
        searchSoftware = request.POST.get('searchSoftware')

        if searchSystem_number == "None" and searchUser == "None" and searchDate == "None" and searchSoftware == "None":
            systemmonitor = SystemMonitor.objects.all()
        else:
            query = Q()
            if searchSystem_number != "None":
                query &= Q(system_number=searchSystem_number)
            if searchUser != "None":
                query &= Q(user=searchUser)
            if searchDate != "None":
                query &= Q(date=searchDate)
            if searchSoftware != "None":
                query &= Q(software=searchSoftware)
            systemmonitor = SystemMonitor.objects.filter(query)

        unique_system_number = SystemMonitor.objects.values_list('system_number', flat=True).distinct()
        unique_user = SystemMonitor.objects.values_list('user', flat=True).distinct()
        unique_date = SystemMonitor.objects.values_list('date', flat=True).distinct()
        unique_software = SystemMonitor.objects.values_list('software', flat=True).distinct()
        data = {
            'tools': systemmonitor,
            'unique_system_number': unique_system_number,
            'unique_user': unique_user,
            'unique_date': unique_date,
            'unique_software': unique_software,
        }
        return render(request, 'SystemMonitor.html', {'tools': data})
    else:
        systemmonitor = SystemMonitor.objects.all()
        unique_system_number = SystemMonitor.objects.values_list('system_number', flat=True).distinct()
        unique_user = SystemMonitor.objects.values_list('user', flat=True).distinct()
        unique_date = SystemMonitor.objects.values_list('date', flat=True).distinct()
        unique_software = SystemMonitor.objects.values_list('software', flat=True).distinct()
        data = {
            'tools': systemmonitor,
            'unique_system_number': unique_system_number,
            'unique_user': unique_user,
            'unique_date': unique_date,
            'unique_software': unique_software,
        }
        return render(request, 'SystemMonitor.html', {'tools': data})



def tools(request):
    if request.method == "POST":
        searchProject = request.POST.get('searchProject')
        searchPlatform = request.POST.get('searchPlatform')
        searchFile_name = request.POST.get('searchFile_name')
        searchKeyword = request.POST.get('searchKeyword')

        if searchProject == "None" and searchPlatform == "None" and searchFile_name == "None" and searchKeyword == "":
            tools = Tool.objects.all()
        else:
            query = Q()
            if searchProject != "None":
                query &= Q(project_name=searchProject)
            if searchPlatform != "None":
                query &= Q(platform=searchPlatform)
            if searchFile_name != "None":
                query &= Q(developer=searchFile_name)
            tools = Tool.objects.filter(query)

        unique_projects = Tool.objects.values_list('project_name', flat=True).distinct()
        unique_platform = Tool.objects.values_list('platform', flat=True).distinct()
        unique_developer = Tool.objects.values_list('developer', flat=True).distinct()
        data = {
            'tools': tools,
            'unique_projects': unique_projects,
            'unique_platform': unique_platform,
            'unique_developer': unique_developer
        }
        return render(request, 'index.html', {'tools': data})
    else:
        tools = Tool.objects.all()
        unique_projects = Tool.objects.values_list('project_name', flat=True).distinct()
        unique_platform = Tool.objects.values_list('platform', flat=True).distinct()
        unique_developer = Tool.objects.values_list('developer', flat=True).distinct()
        data = {
            'tools': tools,
            'unique_projects': unique_projects,
            'unique_platform': unique_platform,
            'unique_developer': unique_developer
        }
        return render(request, 'index.html', {'tools': data})
