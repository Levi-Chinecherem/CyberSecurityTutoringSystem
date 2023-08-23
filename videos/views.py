# videos/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Video
from django.db.models import Q
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def video_search(request):
    videos = Video.objects.all()

    if request.method == 'POST':
        query = request.POST.get('query')
        videos = videos.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(author__icontains=query))

    context = {'videos': videos}

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        video_list_html = render_to_string('videos/video_search.html', context)
        return JsonResponse({'video_list_html': video_list_html})
    else:
        return render(request, 'videos/video_search.html', context)

@login_required   
def saved_videos(request):
    saved_videos = Video.objects.filter(saved=True)
    return render(request, 'videos/saved_videos.html', {'saved_videos': saved_videos})

@login_required
def save_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    
    if request.method == 'POST':
        video.saved = True  # Mark the video as saved
        video.save()  # Save the changes
        
        # Return a JSON response to indicate success
        return JsonResponse({'message': 'Video saved successfully.'})
    
    return render(request, 'videos/saved_video.html', {'video': video})

@login_required
def mark_as_unsaved(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.saved = False  # Mark the video as unsaved
    video.save()  # Save the changes
    
    # Return a JSON response to indicate success
    return JsonResponse({'message': 'Video unsaved successfully.'})

@login_required
def video_detail(request, video_id):  # Add this view
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'videos/video_detail.html', {'video': video})

@login_required
def watched_videos(request):
    watched_videos = Video.objects.filter(watched=True)
    return render(request, 'videos/watched_videos.html', {'watched_videos': watched_videos})

@login_required
def mark_as_watched(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.watched = True
    video.save()
    return JsonResponse({'message': 'Video marked as watched.'})

@login_required
def mark_as_unwatched(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.watched = False
    video.save()
    return JsonResponse({'message': 'Video marked as unwatched.'})
