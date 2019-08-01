const ageBtn = $('#age-btn');
const ageContainer = $('#age');
const countryContainer = $('#country');
const countryBtn = $('#country-btn');
const industryContainer = $('#industry');
const industryBtn = $('#industry-btn');
const roleContainer = $('#role');
const roleBtn = $('#role-btn');
const experienceContainer = $('#experience');
const experienceBtn = $('#experience-btn');
const activitiesContainer = $('#activities');

function assign(btn, toHide, toShow) {
    btn.click(function () {
        toHide.hide();
        toShow.removeAttr('hidden');
    });
}

assign(ageBtn, ageContainer, countryContainer);
assign(countryBtn, countryContainer, industryContainer);
assign(industryBtn, industryContainer, roleContainer);
assign(roleBtn, roleContainer, experienceContainer);
assign(experienceBtn, experienceContainer, activitiesContainer);
