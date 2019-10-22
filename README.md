# Bingo

## About

Bingo is a simple app for tracking a simplified corpo-bingo-styled game where
players are assigned daily quests for certain work-related phrases.
The player marks the number of times the phrase was spoken that day
and receives an equivalent in points.

This application provides both a frontend page for displaying each player's
phrase and total points, as well as a set of REST endpoints for
outside interactions.

## Setup

Hook up `draw_app.app:app` as the WSGI endpoint
in your HTTP server of choice.

See <https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment>
for reference.

## Front-end

A simple front-end is available at `/draw/`
and redirected to from base URL (`/`).

## REST API endpoints

### $ `GET /draw/api/daily`

#### Description

Returns a list of today's assignments.

#### Example response

```json
{
  "Player1": {
    "quote": "Phrase1",
    "points": 1
  },
  "Player2": {
    "quote": "Phrase2",
    "points": 12
  },
  "Player3": {
    "quote": "Phrase3",
    "points": 0
  }
}
```

### $ `GET /draw/api/players/<player:string>/points`

#### Description

Returns the current score of the given player.

#### Example response

```json
{
  "Player1": 0
}
```

### $ `POST /draw/api/players/<player:string>/points`

#### Description

Allows modifying a given player's score.
Returns the player's score after the modification.

#### Arguments

* "action" (string)

|action |result                           |
|-------|---------------------------------|
|"add"  |Increments the player's score    |
|"reset"|Resets the player's score to zero|

Example:

``` shell script
curl -X POST -d '{"action": "add"}' <app>/draw/api/players/Player1/points
```

#### Example response

```json
{
  "Player1": 1
}
```
