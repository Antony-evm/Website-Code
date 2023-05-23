// navigate to home page, article page, topic page

/**
 * Navigates to the home page.
 */
function goToHome() {
    window.location.replace(window.location.origin);
}

/**
 * Navigates to a specific topic page.
 * @param {string} topic - The topic to navigate to.
 */
function goTo(topic) {
    window.location.replace(`${window.location.origin}/topics/${topic}`);
}

/**
 * Navigates to a specific article page.
 * @param {string} article - The article to navigate to.
 */
function goToArticle(article) {
    window.location.replace(`${window.location.origin}/topics/article/${article}`);
}


// open, close navigation bar

/**
 * Toggles the navigation bar.
 */
function change_navbar() {
    var x = document.getElementById('navbar_list_button');
    x.classList.toggle("change");
    var target = document.getElementById("navbar_list");
    if (target.style.display === 'none') {
        target.style.display = 'inline-block';
    } else {
        target.style.display = 'none';
    }
}


// sort & search functions
var timer = null;

// topics

/**
 * Handles the keyup event for the topic search filter.
 */
$("#search_filter_topics").keyup(function() {
    var text = $(this).val();
    var state = $('#state_topics').val();
    clearTimeout(timer);

    var req;

    var inner_function = function() {
        if (req != null) {
            req.abort();
        }
        req = $.ajax({
            url: '/topics',
            type: 'get',
            data: {
                jsdata: text,
                state: state
            },
            success: function(response) {
                $("#container").html(jQuery(response).find('#container').html());
                req = null;
            }
        });
    };

    timer = setTimeout(inner_function, 100);
});

/**
 * Handles the click and mouseleave events for the topic sorting.
 */
$('#sort_topics').on('click mouseleave', function(event) {
    var state_change = document.getElementById('state_change_topics');
    if (event.type === 'mouseleave') {
        state_change.value = 0;
    } else {
        state_change.value = 1;
        var form = document.getElementById('topics_sort_search');
        form.submit();
    }
});

// categories

/**
 * Handles the keyup event for the article search filter.
 */
$("#search_filter_article").keyup(function() {
    var slug = $("#category_identifier").val();
    var text = $(this).val();
    var state = $("#state_article").val();
    clearTimeout(timer);

    var req;

    var inner_function = function() {
        if (req != null) {
            req.abort();
        }
        req = $.ajax({
            url: `/topics/${slug}`,
            type: 'get',
            data: {
                jsdata: text,
                state: state
            },
            success: function(response) {
                $("#container_articles").html(jQuery(response).find('#container_articles').html());
                req = null;
            }
        });
    };

    timer = setTimeout(inner_function, 100);
});

/**
 * Handles the click and mouseleave events for the article sorting.
 */
$('#sort_article').on('click mouseleave', function(event) {
    var state_change = document.getElementById('state_change_articles');
    if (event.type === 'mouseleave') {
        state_change.value = 0;
    } else {
        state_change.value = 1;
        var form = document.getElementById('articles_sort_search');
        form.submit();
    }
});


// flash messages

/**
 * Closes the flash alert message.
 */
function close_alert() {
    var alert = document.getElementById("alert");
    alert.style.display = 'none';
}

// Hides the flash alert message after 3000 milliseconds (3 seconds).
window.setTimeout(function() {
    $('#alert').fadeOut('slow');
}, 3000);