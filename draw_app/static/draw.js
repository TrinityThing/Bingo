function pointsRequest(player_name, action) {
    let xhr = new XMLHttpRequest();
    let result = document.querySelector('#' + player_name);
    let url = "/draw/api/players/" + player_name + "/points";

    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            result.innerHTML = JSON.parse(this.responseText)[player_name];
        }
    };

    var data = JSON.stringify({"action": action});
    xhr.send(data);
}

function addPointsRequest(player_name) {
    pointsRequest(player_name, 'add')
}

function resetPointsRequest(player_name) {
    pointsRequest(player_name, 'reset')
}
