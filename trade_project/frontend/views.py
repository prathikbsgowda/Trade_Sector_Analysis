import requests
from django.shortcuts import render

FASTAPI_BASE_URL = "http://fastapi:8001"  

def index(request):
    report_data = None
    error = None

    if request.method == "POST":
        sector = request.POST.get("sector")
        headers = {
            "x-api-key": "AIzaSyBqxWR_hgaUW1mbTQpTsgiGiuAmAUmKS8Q"  
        }

        try:
            response = requests.get(f"{FASTAPI_BASE_URL}/analyze/{sector}", headers=headers)
            if response.status_code == 200:
                report_data = response.json()
            else:
                error = response.json().get("detail", "Unknown error")
        except Exception as e:
            error = str(e)

    return render(request, "index.html", {"report": report_data, "error": error})
