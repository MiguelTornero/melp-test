# Melp Backend
Backend application that connects to a relational database and allows for simple CRUD operations.
## Requirements
* Python 3.12+
* PIP 23.3+
* A PostgreSQL database, or a SQLite database
## Installation
To install the application, simply clone the repository and install the dependencies:
```bash
pip3 install -r requirements.txt
```
For development, it is recommended to create a virtual environment first.  
## Running the application
To run the application, you must first declare the enviroment variable `SQLALCHEMY_DATABASE_URI`, which should contain the URI that SQLAlchemy will use to connect to the database. After that, simply run the `gunicorn` command with the desired options. For example:
```bash
export SQLALCHEMY_DATABASE_URI="postgresql://postgres:password@localhost/postgres" # local database
gunicorn -b 0.0.0.0:5000 "app:app" # binds to port 5000
```
While the application is running, several API endpoints will be available through HTTP (described in the section [API Endpoints](#api-endpoints)).
## Database initialization
This repository also includes initialization commands for the database, through the `manage.py` file. To create the Restaurant table, declare the `SQLALCHEMY_DATABASE_URI` environment variable simply run this command:
```bash
python3 manage.py initiate_db # SQLALCHEMY_DATABASE_URI should be declared beforehand
```
If you wish to populate the database using a CSV file, you can use this command:
```bash
python3 manage.py load_csv /path/to/file.csv # SQLALCHEMY_DATABASE_URI should be declared beforehand
```
The CSV file should contain field names and values consistent with the Restaurant schema. Here's an example of a valid CSV file:
```csv
id,rating,name,site,email,phone,street,city,state,lat,lng
851f799f-0852-439e-b9b2-df92c43e7672,1,"Barajas, Bahena and Kano",https://federico.com,Anita_Mata71@hotmail.com,534 814 204,82247 Mariano Entrada,Mérida Alfredotown,Durango,19.4400570537131,-99.1270470974249
4e17896d-a26f-44ae-a8a4-5fbd5cde79b0,0,Hernández - Lira,http://graciela.com.mx,Brandon_Vigil@hotmail.com,570 746 998,93725 Erick Arroyo,Mateofurt,Hidalgo,19.437904276995,-99.1286576775023
```
## API Enpoints
### `GET /restaurant`
Returns a list of all the restaurants (default limit: 500)
#### Response
Returns a JSON response with the following schema:
```json
{
    "city": string,
    "email": string,
    "id": string,
    "lat": number,
    "lng": number,
    "name": string,
    "phone": string,
    "rating": number,
    "site": string,
    "state": string,
    "street": string
}[]
```
#### Example
Request:
```http
GET /restaurant
```
Response:
```json
[
    {
        "city": "Mérida Alfredotown",
        "email": "Anita_Mata71@hotmail.com",
        "id": "851f799f-0852-439e-b9b2-df92c43e7672",
        "lat": 19.4400570537131,
        "lng": -99.1270470974249,
        "name": "Barajas, Bahena and Kano",
        "phone": "534 814 204",
        "rating": 1,
        "site": "https://federico.com",
        "state": "Durango",
        "street": "82247 Mariano Entrada"
    },
    {
        "city": "Mateofurt",
        "email": "Brandon_Vigil@hotmail.com",
        "id": "4e17896d-a26f-44ae-a8a4-5fbd5cde79b0",
        "lat": 19.437904276995,
        "lng": -99.1286576775023,
        "name": "Hernández - Lira",
        "phone": "570 746 998",
        "rating": 0,
        "site": "http://graciela.com.mx",
        "state": "Hidalgo",
        "street": "93725 Erick Arroyo"
    },
    ...
]
```

### `GET /restaurant/<id>`
Returns the data of a restaurant with a certain ID.
#### Path parameters
* `id`: The ID of the restaurant to retrieve.
#### Response
Returns a JSON response with the following schema:
```json
{
    "city": string,
    "email": string,
    "id": string,
    "lat": number,
    "lng": number,
    "name": string,
    "phone": string,
    "rating": number,
    "site": string,
    "state": string,
    "street": string
}
```
#### Example
Request:
```http
GET /restaurant/4e17896d-a26f-44ae-a8a4-5fbd5cde79b0
```
Response:
```json
{
    "city": "Mateofurt",
    "email": "Brandon_Vigil@hotmail.com",
    "id": "4e17896d-a26f-44ae-a8a4-5fbd5cde79b0",
    "lat": 19.437904276995,
    "lng": -99.1286576775023,
    "name": "Hernández - Lira",
    "phone": "570 746 998",
    "rating": 0,
    "site": "http://graciela.com.mx",
    "state": "Hidalgo",
    "street": "93725 Erick Arroyo"
}
```
#### Errors
The API uses the following error codes:
* `404 Not Found`: No restaurant was found with the specified ID.

### `PATCH /restaurant/<id>`
Updated the data of a restaurant with a certain ID.
#### Path parameters
* `id`: The ID of the restaurant to update.
#### Body
The body of the request should contain JSON data with the following schema:
```json
{
    "city"?: string,
    "email"?: string,
    "id"?: string,
    "lat"?: number,
    "lng"?: number,
    "name"?: string,
    "phone"?: string,
    "rating"?: number,
    "site"?: string,
    "state"?: string,
    "street"?: string
}
```
#### Response
Returns the amount of rows updated, with the following JSON schema:
```json
{
    "changed_rows": number
}
```
#### Example
Request:
```http
PATCH  /restaurant/2b8f5a44-1e8b-44ec-9b25-0edc5b64b7e6
```
```json
{
    "rating": 4
}
```
Response:
```json
{
    "changed_rows": 1
}
```
#### Errors
The API uses the following error codes:
* `404 Not Found`: No restaurant was found with the specified ID.
* `500 Internal Server Error`: An error ocurred while updating the database

### `POST /restaurant/`
Updated the data of a restaurant with a certain ID.
#### Body
The body of the request should contain JSON data with the following schema:
```json
{
    "city": string,
    "email": string,
    "id": string,
    "lat": number,
    "lng": number,
    "name": string,
    "phone": string,
    "rating": number,
    "site": string,
    "state": string,
    "street": string
}
```
#### Response
Returns the id of the restaurant, with the following JSON schema:
```json
{
    "id": string
}
```
#### Example
Request:
```http
POST  /restaurant
```
```json
{   
    "id": "abcdefghi",
    "city": "Test city",
    "email": "test@email.com",
    "lat": 12,
    "lng": 34,
    "name": "Test name",
    "phone": "123456789",
    "rating": 4,
    "site": "https://test.com",
    "state": "CDMX",
    "street": "Test street"
}
```
Response:
```json
{
    "id": "abcdefghi"
}
```
#### Errors
The API uses the following error codes:
* `500 Internal Server Error`: An error ocurred while updating the database
* `400 Bad Request`: One of the elements of the request was malformed

### `DELETE /restaurant/<id>`
Deletes a restaurant with a certain ID from the database.
#### Path parameters
* `id`: The ID of the restaurant to delete.
#### Response
Returns a JSON response with the following schema, containing the amount of rows deleted:
```json
{
    "rows_deleted": number
}
```
#### Example
Request:
```http
DELETE /restaurant/4e17896d-a26f-44ae-a8a4-5fbd5cde79b0
```
Response:
```json
{
    "rows_deleted": 1
}
```
#### Errors
The API uses the following error codes:
* `404 Not Found`: No restaurant was found with the specified ID.

### `GET /restaurants/statistics`
Gets rating statistics from restaurants inside a specified radius.
#### Query parameters
* `latitude`: Latitude of the center of the circle
* `longitude`: Longitude of the center of the circle
* `radius`: Radius of the circle3
#### Response
Returns a JSON object with the amount of restaurants inside the radius, as well as the average and standard deviation of their ratings, using the following schema:
```json
{
    "count": number,
    "avg": number,
    "std": number
}
```
#### Example
Request:
```http
GET restaurants/statistics?latitude=19.4331364103761&longitude=-99.1239206144939&radius=1000
```
Response
```json
{
    "avg": 2,
    "count": 9,
    "std": 1.4142135623730951
}
```
#### Errors
* `500 Internal Server Error`: An error ocurred while accessing the database
* `400 Bad Request`: One of the elements of the request was malformed
* `404 Not Found`: No restaurants were found inside the radius
