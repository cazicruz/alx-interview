#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';
request(url, function (error, response, body) {
    if (error) {
        console.log(error);
    } else {
        const characters = JSON.parse(body).characters;
        for (let i = 0; i < characters.length; i++) {
        request(characters[i], function (error, response, body) {
            if (error) {
            console.log(error);
            } else {
            console.log(JSON.parse(body).name);
            }
        });
        }
    }
    }
```

### 1. Star Wars Wedge Antilles
Write a script that prints the number of movies where the character “Wedge Antilles” is present.
- The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
- Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
- You must use the module request


// Path: 1-starwars_characters.js
#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
    if (error) {
        console.log(error);
    } else {
        const results = JSON.parse(body).results;
        let count = 0;
        for (let i = 0; i < results.length; i++) {
            const characters = results[i].characters;
            for (let j = 0; j < characters.length; j++) {
                if (characters[j].includes('18')) {
                    count++;
                }
            }
        }
        console.log(count);
    }
}
```
