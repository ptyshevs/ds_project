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

function assign(trigger, toHide, toShow) {
    trigger.change(function () {
        toHide.hide();
        toShow.removeAttr('hidden');
    });
}

assign(ageInput, ageContainer, countryContainer);
assign(countryInput, countryContainer, industryContainer);
assign(industryInput, industryContainer, roleContainer);
assign(roleInput, roleContainer, experienceContainer);
assign(experienceInput, experienceContainer, activitiesContainer);
