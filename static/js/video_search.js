// videos/static/videos/js/video_search.js
$(document).ready(function() {
    $("#search-form").submit(function(event) {
        event.preventDefault();
        const query = $("input[name='query']").val();
        $.ajax({
            type: "POST",
            url: "",
            data: {
                query: query,
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function(response) {
                $("#video-list").html(response.video_list_html);
            }
        });
    });
    
    $("#nav-toggle").click(function() {
        $("#hidden-nav").toggleClass("hidden");
    });
});
