# Teacheress

A SPA PWA project for organization planning.
Here we create an offline capable web app that allows to organize appointments.

What defines an appointment:
- date & time, title and comment
- additionally an appointment may be assigned several customer tags for ordering. E.g. class 7.b.

Todos:
- week based view for planing
- predefined slots from a template (e.g. coffee break each day at 10:30) should be defineable
- tag based view
- search capability

## Requirements

Frontend PWA
- angular.io
- angular pwa
    https://angular.io/api/service-worker

Backend Service
- python3.8
- fast api

## Structure

`app` containes the angular web app
[`backend`](backend/Readme.md) contains a python fast api backend service.
