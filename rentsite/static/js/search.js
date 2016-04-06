/**
 * Created by votetob on 28.03.16.
 */
$('document').ready(function(){
    $("#sliders").each(function(index){
        $(this).find('input').slider();
    });



    $('.dropdown-menu').on('click', function(e){
        e.stopPropagation();
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var options_list = [];
    function ajaxCall(query){
    $.ajax({
        url: '',
        type: 'POST',
        data: query,
        dataType: 'json',
        success: function(response){
            console.log(response);
            var newPlaces = $.map(response, function(place, i){
                var singlePlace = $('<div class="col-md-4"><section><a class="container place_mini"></a></section></div>');
                var insideSinglePlace = $(singlePlace).find('a');
                $.map(place, function(field, i){
                    var singleField =  $('<div></div>');
                    singleField.addClass(field[0]);
                    singleField.text(field[1]);
                    insideSinglePlace.append(singleField)
                });

                singlePlace.find(".price").text(place.price);
                singlePlace.find("");
                return singlePlace;
            });

            var results = $('.results');
            results.empty();
            results.append(newPlaces).fadeIn();


        }

    })
}
    function getSearchQuery(){
        var query = {};
        $('.checkbox').each(function(index){
            var option = $(this).find('.dropdown-menu');
            var selected_options = [];
            $(option).find('a').each(function(index, value2){
                if ($(value2).find('input').is(":checked")){
                    selected_options.push($(value2).find('label').text().trim());
                }
                });
            if (selected_options.length != 0){
                query[option.attr('id')] = selected_options;
            }


        });
        $('.slider').each(function(){
            if ($(this).find('input').val() != '')
            query[$(this).find('input').attr('id')] = $(this).find('input').val()
        });

        return query
}


    $('.btn-success').on('click', function(e){
        var query = getSearchQuery();
        ajaxCall(query);
    });






});