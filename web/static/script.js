const ageInput = $('input[type=radio][name=age]');
const ageContainer = $('#age');
const countryContainer = $('#country');
const countryInput = $('input[type=radio][name=country]');
const industryContainer = $('#industry');
const industryInput = $('input[type=radio][name=industry]');
const roleContainer = $('#role');
const roleInput = $('input[type=radio][name=role]');
const experienceContainer = $('#experience');
const experienceInput = $('input[type=radio][name=experience]');
const activitiesContainer = $('#activities');

const nextSectionButton = $('#next_section');
const primaryToolContainer = $('#primary_tool_container');
const cloudServicesContainer = $('#cloud_services_container');
const regularLanguagesContainer = $('#regular_languages_container');
const visualLibsContainer = $('#visual_libs_container');
const dataContainer = $('#data_container');
const onlinePlatformsContainer = $('#online_platforms_container');
const mediaSourcesContainer = $('#media_sources_container');


function assign(trigger, toHide, toShow) {
    trigger.change(function () {
        toHide.hide();
        toShow.removeAttr('hidden');
    });
}

nextSectionButton.click(function () {
    if ($('#online_platforms_container').hasClass('active')) {
        $(this).hide();
        $('button[type=submit]').removeClass('d-none');
    } else {
        $(this).text('Skip');
    }
    $('.active').addClass('d-none').removeClass('active').next().removeClass('d-none').addClass('active');

});

$('.form-check').click(function (){
    nextSectionButton.text('Next');
});

assign(ageInput, ageContainer, countryContainer);
assign(countryInput, countryContainer, industryContainer);
assign(industryInput, industryContainer, roleContainer);
assign(roleInput, roleContainer, experienceContainer);
assign(experienceInput, experienceContainer, activitiesContainer);

if ($('#salary_distribution').length) {
    var trace1 = {
        x: window.labels,
        y: window.probabilities,
        type: 'bar',
        marker: {
            color: 'rgb(142,124,195)'
        }
    };

    var data = [trace1];

    var layout = {
        title: 'Your Salary Distribution',
        font: {
            family: 'Raleway, sans-serif'
        },
        showlegend: false,
        xaxis: {
            tickangle: -45,
            gridwidth: 1
        },
        yaxis: {
            zeroline: false,
            gridwidth: 1
        },
        bargap: 0.05
    };

    Plotly.newPlot('salary_distribution', data, layout);
}
$(document).ready(function () {
if ($('#langs_recommendations').length) {
    console.log(window.langs_keys);
    console.log(window.langs_values);
    var trace2 = {
        x: window.langs_keys,
        y: window.langs_values,
        type: 'bar',
        marker: {
            color: 'rgb(142,124,195)'
        }
    };

    var data2 = [trace2];

    var layout2 = {
        title: 'Languages Recommendations',
        font: {
            family: 'Raleway, sans-serif'
        },
        showlegend: false,
        xaxis: {
            tickangle: -45,
            gridwidth: 1
        },
        yaxis: {
            zeroline: false,
            gridwidth: 1
        },
        bargap: 0.05
    };

    Plotly.newPlot('langs_recommendations', data2, layout2);
}
if ($('#frameworks_recommendations').length) {
    var trace3 = {
        x: window.frameworks_keys,
        y: window.frameworks_values,
        type: 'bar',
        marker: {
            color: 'rgb(142,124,195)'
        }
    };

    var data3 = [trace3];

    var layout3 = {
        title: 'Frameworks Recommendations',
        font: {
            family: 'Raleway, sans-serif'
        },
        showlegend: false,
        xaxis: {
            tickangle: -45,
            gridwidth: 1
        },
        yaxis: {
            zeroline: false,
            gridwidth: 1
        },
        bargap: 0.05
    };

    Plotly.newPlot('frameworks_recommendations', data3, layout3);
}
if ($('#courses_recommendations').length) {
    var trace4 = {
        x: window.courses_keys,
        y: window.courses_values,
        type: 'bar',
        marker: {
            color: 'rgb(142,124,195)'
        }
    };

    var data4 = [trace4];

    var layout4 = {
        title: 'Courses Recommendations',
        font: {
            family: 'Raleway, sans-serif'
        },
        showlegend: false,
        xaxis: {
            tickangle: -45,
            gridwidth: 1
        },
        yaxis: {
            zeroline: false,
            gridwidth: 1
        },
        bargap: 0.05
    };

    Plotly.newPlot('courses_recommendations', data4, layout4);
}
if ($('#sources_recommendations').length) {
    var trace5 = {
        x: window.courses_keys,
        y: window.courses_values,
        type: 'bar',
        marker: {
            color: 'rgb(142,124,195)'
        }
    };

    var data5 = [trace5];

    var layout5 = {
        title: 'Courses Recommendations',
        font: {
            family: 'Raleway, sans-serif'
        },
        showlegend: false,
        xaxis: {
            tickangle: -45,
            gridwidth: 1
        },
        yaxis: {
            zeroline: false,
            gridwidth: 1
        },
        bargap: 0.05
    };

    Plotly.newPlot('sources_recommendations', data5, layout5);
}
});
