let textbox = document.getElementById("message");

let time_clear = setTimeout(function() {
    location.reload();
}, 5000);

textbox.onkeydown = function(e) {
    clearTimeout(time_clear)
    time_clear = setTimeout(function() {
        location.reload();
    }, 5000)
};
