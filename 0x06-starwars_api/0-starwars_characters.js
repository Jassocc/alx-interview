#!/usr/bin/node
// script for task 0

const request = require('request');
const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  process.exit(1);
}
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    return;
  }
  const film = JSON.parse(body);
  const chars = film.characters;
  if (!chars || chars.length === 0) {
    return;
  }
  const charsReq = chars.map(charUrl => {
    return new Promise((resolve, reject) => {
      request(charUrl, (error, response, body) => {
        if (error) {
          return;
        }
        if (response.statusCode !== 200) {
          return;
        }
        const chars = JSON.parse(body);
        resolve(chars.name);
      });
    });
  });
  Promise.all(charsReq)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => {
      console.log(error);
    });
});
