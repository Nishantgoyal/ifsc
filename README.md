# IFSC Site

- [how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04)

## Site Modules

### Database

- Mongo DB

### Backend

- Parses RBI data and dumps to database
- MicroServices
  1. Get Bank URLs
     - Download RBI Home page
     - Parse RBI Home page
     - Get list of Banks and dump to mongo
  2. Fetch List of Banks and download the raw file

### Frontend

- Fetches data from mongo and displays as HTML
  - Home Page
  - Bank Lists
