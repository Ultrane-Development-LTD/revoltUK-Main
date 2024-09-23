window.onload = function() {
    var adBlockerDetected = false;
    var adTest = document.createElement('div');
    adTest.innerHTML = '&nbsp;';
    adTest.className = 'adsbox';
    document.body.appendChild(adTest);
    window.setTimeout(function() {
        if (adTest.offsetHeight === 0) {
            adBlockerDetected = true;
        }
        document.body.removeChild(adTest);
        if (adBlockerDetected) {
            // Display a message
            alert("It seems you are using an ad blocker. Please consider disabling it for our site.");
        }
    }, 100);
};