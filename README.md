# GeoDataAPI
This is an API (Django DRF) that requires JWT authentication and is used to add, retrieve and delete geolocation data.

## Heroku
It has been deployed to Heroku: https://geoappapi.herokuapp.com/account/api/register/ <br />
The DRF browsable API is enable, but one should use e.g. Postman with JWT tokens.

## Endpoints
/account/api/register/ POST <br />
/account/api/token POST <br />
/account/api/token/refresh POST <br /> 

/api/add/ POST <br />
/api/list/ GET <br />
/api/< pk > GET DELETE ; ip is set as the pk <br /> 
/api/url/< url > GET <br />

## JWT Authorization
After successful registration, user receives two tokens:
- access token: active for 15 min
- refresh token: active for 24h
- use /account/api/token + refresh token to get a new access token

## Registration
Register at: https://geoappapi.herokuapp.com/account/api/register/ <br />
See the below example what to post to register: <br />
{ <br />
&nbsp;&nbsp; "username": "johnsmith", <br />
&nbsp;&nbsp; "email": "johnsmith@example.com", <br />
&nbsp;&nbsp; "password": "Password123", <br />
&nbsp;&nbsp; "password2": "Password123" <br />
}

## Adding, viewing and deleting geo data
- add data at /api/add/ <br />
- delete data at /api/<pk>
- list of all data at /api/list/ GET 
- view individual items at /api/<pk> OR /api/url/<url>
- below you can see what you can add (url is optional): 

{

&nbsp;&nbsp;                    "ip": "140.82.114.4", <br />
&nbsp;&nbsp;                    "url": "https://github.com", <br />
&nbsp;&nbsp;                    "continent_code": "NA", <br />
&nbsp;&nbsp;                    "country_name": "United States", <br />
&nbsp;&nbsp;                    "region_name": "California", <br />
&nbsp;&nbsp;                    "city": "San Francisco", <br />
&nbsp;&nbsp;                    "zip": "94107", <br />
&nbsp;&nbsp;                    "latitude": 37.76784896850586, <br />
&nbsp;&nbsp;                    "longitude": -122.39286041259766, <br />
&nbsp;&nbsp;                    "is_eu": false <br />
} 

## Filtering
- filtering is avaiable at /api/list/ 
- available filters: ['continent_code', 'country_name', 'region_name', 'city', 'zip', 'is_eu']

## Pagination
- 'PAGE_SIZE': 5

## Throttling
- throttle rates: 'user': '20/day'

## Tests
- see geoip_app/tests.py
- see use_app/tests.py
