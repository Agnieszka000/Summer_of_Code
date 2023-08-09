/* Wykorzystaj endpoint https://reqres.in/api/users?page=1 do pobrania listy użytkowników. */

fetch('https://reqres.in/api/users?page=1')
    .then(r => r.json())
    .then(data => {
        let people = data.data;
        for (let i=0; i < people.length; i++) {
        console.log('IMIE: ' + people[i].first_name);
        console.log('NAZWISKO: ' + people[i].last_name);
        console.log('EMAIL: ' + people[i].email);
        console.log("----");
        }
    })