1 - create some artists
>>> from artists.models import Artist
>>> hamza = Artist(stage_name="Hamza Namera", social_link_field = "https://www.instagram.com/hamzanamira/")  
>>> hamza.save()
>>> amalmaher = Artist(stage_name="Amal Maher", social_link_field = "https://www.instagram.com/amalmaherofficial/")
>>> amalmaher.save()
>>> ahmed = Artist(stage_name="Ahmed shepa",social_link_field = "https://www.instagram.com/ahmedshebaofficial/")
>>> ahmed.save()

2 - list down all artists
>>> Artist.objects.all()
<QuerySet [<Artist: Hamza Namera>, <Artist: Amal Maher>, <Artist: Ahmed shepa>]>

3 - list down all artists sorted by name
>>> Artist.objects.all().order_by('stage_name')
<QuerySet [<Artist: Ahmed shepa>, <Artist: Amal Maher>, <Artist: Hamza Namera>]>

4 - list down all artists whose name starts with A
>>> Artist.objects.all().filter(stage_name__startswith='A')
<QuerySet [<Artist: Amal Maher>, <Artist: Ahmed shepa>]>

5 - in 2 different ways, create some albums and assign them to any artists
* First way
>>> from albums.models import Album
>>> m3lesh = Album(artist = hamza, album_name = "m3lesh", abum_date="2018-02-03", album_cost=5000.78)
>>> m3lesh.save()
* Second way
>>> Album.objects.create(artist=hamza, album_name = "insan", abum_date="2018-05-03", album_cost=4000.9)
<Album: insan>
>>> Album.objects.create(artist=ahmed, album_name = "ah_lw_l3bt_ya_zahr", abum_date="2020-05-03", album_cost=4000.9)
<Album: ah_lw_l3bt_ya_zahr>

6 - get the latest released album
>>> Album.objects.all().order_by("-abum_date")[0]
<Album: ah_lw_l3bt_ya_zahr>

7 - get all albums released before today
>>> Album.objects.filter(abum_date__lt="2022-01-15")
<QuerySet [<Album: m3lesh>, <Album: insan>, <Album: ah_lw_l3bt_ya_zahr>]>
>>> Album.objects.filter(abum_date__lt="2018-05-03")
<QuerySet [<Album: m3lesh>]>

8 - get all albums released today or before but not after today
>>> Album.objects.filter(abum_date__lte="2018-05-03")
<QuerySet [<Album: m3lesh>, <Album: insan>]>

9 - count the total number of albums
>>> Album.objects.all().count()
3

10 - in 2 different ways, for each artist, list down all of his/her albums

*First way
>>> for _artist in Artist.objects.all():
...      print(_artist.stage_name)
...      print(Album.objects.filter(artist=_artist))
...
Hamza Namera
<QuerySet [<Album: m3lesh>, <Album: insan>]>
Amal Maher
<QuerySet []>
Ahmed shepa
<QuerySet [<Album: ah_lw_l3bt_ya_zahr>]>

*Second way

11 - list down all albums ordered by cost then by name
>>> Album.objects.all().order_by("album_cost","album_name")
<QuerySet [<Album: ah_lw_l3bt_ya_zahr>, <Album: insan>, <Album: m3lesh>]>