// videos/static/videos/js/video_detail.js
$(document).ready(function() {
    $("#mark-watched").click(function(event) {
        event.preventDefault();
        const videoId = $(this).data("video-id");
        
        if (window.confirm("Mark this video as watched?")) {
            $.ajax({
                type: "POST",
                url: "{% url 'mark_as_watched' 0 %}".replace('0', videoId),
                data: {
                    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
                },
                success: function(response) {
                    // Display success message
                    $(".success-message").text(response.message).show();
                    // Update UI or perform further actions if needed
                    $("#mark-watched").addClass("hidden");
                    $("#mark-unwatched").removeClass("hidden");
                },
                error: function(xhr, status, error) {
                    // Handle error
                    alert("An error occurred. Video could not be marked as watched.");
                }
            });
        }
    });

    $("#mark-unwatched").click(function(event) {
        event.preventDefault();
        const videoId = $(this).data("video-id");
        
        if (window.confirm("Mark this video as unwatched?")) {
            $.ajax({
                type: "POST",
                url: "{% url 'mark_as_unwatched' 0 %}".replace('0', videoId),
                data: {
                    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
                },
                success: function(response) {
                    // Display success message
                    $(".success-message").text(response.message).show();
                    // Update UI or perform further actions if needed
                    $("#mark-watched").removeClass("hidden");
                    $("#mark-unwatched").addClass("hidden");
                },
                error: function(xhr, status, error) {
                    // Handle error
                    alert("An error occurred. Video could not be marked as unwatched.");
                }
            });
        }
    });

    $("#nav-toggle").click(function() {
        $("#hidden-nav").toggleClass("hidden");
    });
});
