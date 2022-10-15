from django.views.generic import View
from django.http import JsonResponse
import json
from .forms import ArtistForm
from .models import Artist  

class ArtistView(View) :
    def get(self, request, *args, **kwargs) :
        Body = json.loads(request.body)
        if Body["prefix filter"] != "" :
            AllArtistsData = list(
                Artist.objects.values().filter(stage_name__startswith=Body["prefix filter"])
            )
        elif Body["order"] == "sort by name" :
            AllArtistsData = list(Artist.objects.values().order_by('stage_name'))
        else :
            AllArtistsData = list(Artist.objects.values())    
        return JsonResponse({'Artists' : AllArtistsData}, safe=False)

    def Registering_Artist(self, Body):
        Artist_To_Resgiser = {
            "stage_name" : Body["stage_name"],
            "social_link_field" : Body["social_link_field"],  
        }
        return Artist_To_Resgiser

    def Create_Artist(self, Body) :
        return Artist(
            stage_name = Body["stage_name"],
            social_link_field = Body["social_link_field"], 
        )

    def post(self, request, *args, **kwargs):
        Body = json.loads(request.body)
        Artist_To_Register = self.Create_Artist(Body)
        New_Artist = self.Registering_Artist(Body)
        valitationState = ArtistForm(New_Artist)
        if valitationState.is_valid():
            Artist_To_Register.save()
            return JsonResponse({'Artist added' : New_Artist}, status = 200, safe = False) #Ok
        else:
            return JsonResponse(data = json.loads(valitationState.errors.as_json()), status = 422) # 422 Unprocessable Entity

class SingleArtistView(View) :
    def get(self, request, *args,  **kwargs):
        Get_Artist = list(Artist.objects.filter(id=kwargs["id"]).values())
        if len(Get_Artist) != 0:
            return JsonResponse(Get_Artist, status = 302, safe = False) # Found 
        else:
            return JsonResponse(data = "User Not Found", status = 404, safe = False) # Not Found

    def delete(self, request, *args, **kwargs):
        Get_User = list(Artist.objects.filter(id=kwargs["id"]).values())
        if len(Get_User) != 0:
            Artist.objects.filter(id=kwargs["id"]).delete()
            return JsonResponse(data = "User is deleted", status = 200, safe = False) # OK
        else :
            return JsonResponse(data = "User Not Found", status = 404, safe = False) # Not Found

    def Registering_Artist(self, Body):
        Artist_To_Resgiser = {
            "stage_name" : Body["stage_name"],
            "social_link_field" : Body["social_link_field"],  
        }
        return Artist_To_Resgiser

    def Update_Artist(self, Body, id) :
        return Artist.objects.filter(id=id).update(
            stage_name = Body["stage_name"],
            social_link_field = Body["social_link_field"],
        )

    def put(self, request, *args, **kwargs):
        Body = json.loads(request.body)
        Get_Artist = list(Artist.objects.filter(id=kwargs["id"]).values())
        if len(Get_Artist) != 0:
            # Validating user
            To_Validate_Artist = self.Registering_Artist(Body)
            valitationState = ArtistForm(To_Validate_Artist)
            if valitationState.is_valid():
                # Updating with body attributes
                self.Update_Artist(Body, kwargs["id"])
                return JsonResponse("User is Updated", status = 200, safe = False) # OK
            else:
                return JsonResponse(data = json.loads(valitationState.errors.as_json()), status = 422) # 422 Unprocessable Entity 
