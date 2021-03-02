function removeRace(raceId) {

    console.log("Envoie des données ...")
    console.log("Course à supprimé : " + raceId)
    const url = '/remove_race/'

    body_data = {
        'raceId': raceId,
    }

    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(body_data)
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log(data)
        });

        $( "#raceContainer" ).load(window.location.href + " #raceContainer > *" );

    
}
