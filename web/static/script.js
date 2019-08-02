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
    if ($('#media_sources_container').hasClass('active')) {
        $(this).hide();
        $('button[type=submit]').removeClass('d-none');
    } else {
        $('.active').addClass('d-none').removeClass('active').next().removeClass('d-none').addClass('active');
        $(this).text('Skip');
    }
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