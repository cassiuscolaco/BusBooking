from django.shortcuts import render
from rest_framework import viewsets
from .models import MumbaiRoute
from .serializers import MumbaiRouteSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from requests import *

try:
	url="http://127.0.0.1:8000/mumbairoute"
	he = {
			"Authorization": "Token 391a3fead4bcc8d9e3152f28e39497a3e5dcac7c"
	}
	res = get(url, headers=he)
	print(res.status_code)
	if res.status_code == 200:
			data = res.json()
			msg = data["msg"]
			print(msg)
	else:
			print("bad credentials")
except Exception as e:
		print("issue" , e)
def home(request):
    if request.method == "POST":
        route = request.POST.get("route")
        if route == "1":
            res = "To Khodadad Circle (Dadar T.T.)"
            msg = str(res)
        elif route == "2":
            res = "To Bandra Colony Bus Station"
            msg = str(res)
        elif route == "3":
            res = "To Navy Nagar(Colaba)"
            msg = str(res)
        elif route == "4":
            res = "To Goregaon Oshiwara Depot"
            msg = str(res)
        elif route == "6":
            res = "To Colaba Depot (Electric House)"
            msg = str(res)
        elif route == "7":
            res = "To Vijay Vallabh Chowk"
            msg = str(res)
        elif route == "8":
            res = "To Chhatrapati Shivaji Maharaj Terminus (C.S.M.T.)"
            msg = str(res)
        elif route == "9":
            res = "To Antop Hill Bus Station"
            msg = str(res)
        elif route == "11":
            res = "To Bandra Colony Bus Station"
            msg = str(res)
        elif route == "14":
            res = "To Dr.Shyamaprasad Mukherjee Chowk (Museum)"
            msg = str(res)
        elif route == "15":
            res = "To Mantralaya"
            msg = str(res)
        elif route == "22":
            res = "To Vijay Vallabh Chowk (Pydhonie)"
            msg = str(res)
        elif route == "25":
            res = "To Kurla Depot"
            msg = str(res)
        elif route == "25 A":
            res = "To Vihar Lake"
            msg = str(res)
        elif route == "27":
            res = "To Vaishali Nagar (Mulund-W)"
            msg = str(res)
        elif route == "28":
            res = "To Swami Dayanand Saraswati Chowk"
            msg = str(res)
        elif route == "35":
            res = "To Comrade P.K.Kurne Chowk"
            msg = str(res)
        elif route == "37":
            res = "To J.Mehta Marg"
            msg = str(res)
        elif route == "39":
            res = "To Veer Hutatma Bhai Kotwal Udyan (Plaza)"
            msg = str(res)
        elif route == "44":
            res = "To Dr.Shyamaprasad Mukherjee Chowk (Museum)"
            msg = str(res)
        elif route == "45":
            res = "To M.M.R.D.A.Colony(Extension) Mahul"
            msg =  str(res)
        elif route == "46":
            res = "To Mallet Bunder Check Post"
            msg =  str(res)
        elif route == "49":
            res = "To M.M.R.D.A.Colony (Extension) Mahul"
            msg =  str(res)
        elif route == "50":
            res = "To Mallet Bunder Check Post"
            msg = str(res)
        elif route == "52":
            res = "To Shrawan Yashwante Chowk (Kala Chowky)"
            msg = str(res)
        elif route == "56":
            res = "To Veer Hutatma Bhai Kotwal Udyan (Plaza)"
            msg = str(res)
        elif route == "57":
            res = "To Kamala Nehru Park (Malabar Hill)"
            msg = str(res)
        else:
            msg = "Please enter valid route number !!"
        return render(request, "home.html", {"msg": msg})
    else:
        return render(request, "home.html")

class MumbaiRouteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MumbaiRoute.objects.all()
    serializer_class = MumbaiRouteSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

			
