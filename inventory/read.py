from django.conf import settings
import json
from django.shortcuts import render

managementjson = settings.MEDIA_ROOT / 'report' / 'management.json'

def management(request):
    try:
        with open(managementjson) as f:
            data = json.load(f)
    except:
        data = {}
    
    jsonData = json.dumps(data)

    context = {'jsonData':jsonData}
    context.update(data)

    return render(request,'ims/management.html')