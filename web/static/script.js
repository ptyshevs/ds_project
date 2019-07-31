const ageBtn = $('#age-btn');
const ageContainer = $('#age');
const countryContainer = $('#country');

ageBtn.click(function(){
    ageContainer.hide();
    countryContainer.removeAttr('hidden');
});