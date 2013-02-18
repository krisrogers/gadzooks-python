function filterTests (group) {
    console.log(group);
    if (group) {
        $('#tests').find('.test').hide();
        $('#tests').find('.group-'+group).show();
    }
    else {
        $('#tests').find('.test').show();
    }
}

function showContent (id, link) {
    // Show the correct content
    $('#main-content').children().each(function (i, el) {
        el = $(el);
        if (el.attr('id') == id) {
            el.show();
        }
        else {
            el.hide();
        }
    });
    // Deactivate links
    $('#nav-header').children().removeClass('active');
    $('.sidebar-nav').find('li').removeClass('active');
    if (link) {
        $(link).addClass('active');
    }
}

function toggleTestDescription(link) {
    $(link).parent().find('.test-description').toggle();
}