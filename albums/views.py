from django.views.generic import View
from django.http import JsonResponse
import json
from .forms import AlbumForm
from .models import Album

class AlbumView(View) :
    def get(self, request, *args, **kwargs) :
        AllAlbumsData = list(Album.objects.values())
        return JsonResponse({'Albums' : AllAlbumsData}, safe=False)

    def Registering_Album(self, Body):
        Album_To_Resgiser = {
            "album_name" : Body["album_name"],
            "abum_date" : Body["abum_date"], 
            "album_cost" : Body["album_cost"], 
        }
        return Album_To_Resgiser

    def Create_Album(self, Body) :
        return Album(
            album_name = Body["album_name"],
            abum_date = Body["abum_date"],
            album_cost = Body["album_cost"], 
        )

    def post(self, request, *args, **kwargs):
        Body = json.loads(request.body)
        Album_To_Register = self.Create_Album(Body)
        New_Album = self.Registering_Album(Body)
        valitationState = AlbumForm(New_Album)
        if valitationState.is_valid():
            Album_To_Register.save()
            return JsonResponse({'Album added' : New_Album}, status = 200, safe = False) #Ok
        else:
            return JsonResponse(data = json.loads(valitationState.errors.as_json()), status = 422) # 422 Unprocessable Entity
