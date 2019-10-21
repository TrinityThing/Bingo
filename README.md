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

### `GET /draw/rest/`

#### Description

Returns a list of today's assignments.

#### Example response

```json
{
  "Player1": "Phrase1",
  "Player2": "Phrase2",
  "Player3": "Phrase3"
}
```

### `POST /draw/rest/addPoints`

#### Description

Allows giving players points for completed quests.
