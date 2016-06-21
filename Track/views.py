from django.shortcuts import render
from Track.forms import TrackForm, GenreForm
from Track.models import Track, Genre
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def addTrack(request):

	message = "Add a new Track"
	if request.method == "POST":

		form = TrackForm(request.POST)
		data = request.POST

		try:

			genre = Genre.objects.get(genreId=data["trackGenre"])
			track = Track.objects.create(trackTitle=data["trackTitle"], trackRating=data["trackRating"], trackGenre=genre)
	
		except:

			return render(request, "track/track.html", {"trackForm": form, "message": "Couldn't save track"})
		message = "Your track " + data["trackTitle"] + " got added. " + message
	trackForm = TrackForm()
	return render(request, "track/track.html", {"trackForm": trackForm, "message": message})


@csrf_exempt
def listTrack(request):

	if request.method == "POST":

		data = request.POST

		try:
		
			if data["trackTitle"]:

				track = Track.objects.filter(trackTitle=data["trackTitle"])

			elif data["genre"]:

				genre = Genre.objects.get(genreName=data["genre"])
				track = Track.objects.filter(trackGenre=genre)

			elif data["trackTitle"] and data["genre"]:

				genre = Genre.objects.get(genreName=data["genre"])
				track = Track.objects.filter(trackGenre=genre, trackTitle=data["trackTitle"])
			return render(request, "track/list.html", {"status": True, "tracks": track})

		except:

			return render(request, "track/list.html", {"status": False})
	tracks = Track.objects.all()
	return render(request, "track/list.html", {"tracks": tracks})


@csrf_exempt
def addGenre(request):

	message = "Add a new Genre"
	if request.method == "POST":

		form = GenreForm(request.POST)
		data = request.POST

		try:
			
			genre = Genre.objects.create(genreName=data["genreName"])

		except:

			return render(request, "track/genre.html", {"genreForm": form})
		message = "Your genre " + data["genreName"] + " got added. " + message
	genreForm = GenreForm()
	return render(request, "track/genre.html", {"genreForm": genreForm, "message": message})


@csrf_exempt
def listGenre(request):

	if request.method == "POST":

		data = request.POST

		try:
		
			genre = Genre.objects.filter(genreName=data["genreName"])
			return render(request, "track/genrelist.html", {"status": True, "genre": genre})

		except:

			return render(request, "track/genrelist.html", {"status": False})
	genre = Genre.objects.all()
	return render(request, "track/genrelist.html", {"genre": genre})








