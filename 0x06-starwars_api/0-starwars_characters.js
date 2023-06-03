#!/usr/bin/node
/*
Write a script that prints all characters of a Star Wars movie:
from the sarewars API: https://swapi-api.hbtn.io/api/films/:id
*/

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
    if (error) {
        console.log(error);
    }
    if (response.statusCode === 200){
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
);
