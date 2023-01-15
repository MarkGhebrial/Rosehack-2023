mergeInto(LibraryManager.library, {

    UpdateLeaderboard: function (score) {
        let xhr = new XMLHttpRequest();
        xhr.open("POST", "/api/leaderboard/galaga");
        xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        let params = `score=${score}`

        xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            console.log(xhr.status);
            console.log(xhr.responseText);
        }};

        xhr.send(params);

        // Return the http response
        var returnStr = xhr.response
        var bufferSize = lengthBytesUTF8(returnStr) + 1;
        var buffer = _malloc(bufferSize);
        stringToUTF8(returnStr, buffer, bufferSize);
        return buffer;
    },

    GetLeaderboard: function (score) {
        let xhr = new XMLHttpRequest();
        xhr.open("GET", "/api/leaderboard/galaga");

        xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            console.log(xhr.status);
            console.log(xhr.responseText);
        }};

        xhr.send();

        // Return the http response
        var returnStr = xhr.response
        var bufferSize = lengthBytesUTF8(returnStr) + 1;
        var buffer = _malloc(bufferSize);
        stringToUTF8(returnStr, buffer, bufferSize);
        return buffer;
    },
});