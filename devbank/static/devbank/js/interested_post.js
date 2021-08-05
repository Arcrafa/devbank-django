const axios = require('axios').default;

document.getElementById('fullname')

join_us = document.getElementById('join_us');

join_us.addEventListener("join_us_click", function(e) { console.log(e.detail) });


var event = new CustomEvent("join_us_click", {
console
});
join_us.dispatchEvent(event);