# Shorty - URL Shortener w/ Django & DRF

Basic Web App using Django for front/back-end and Django Rest Framework to implement API and APIView.

## Setup

Clone

```bash
git clone https://github.com/matheusclmb/Shorty-Django-Version.git
```

Create VENV

```bash
$ python3 -m venv env
$ source env/bin/activate
```

Install Requirements

```bash
$ pip install -r requirements.txt
```

Run Server

```bash
$ python3 manage.py runserver
```

## Tests

Run all tests:

```bash
$ python manage.py test
```


#### OBS:

This project have tests using Selenium Library, in order to use you need to have Geckodriver in the project folder or in `env/bin`.
If you are running to problems make sure you have Firefox installed and the exact PATH on Selenium function `driver = webdriver.Firefox(executable_path="/user/your/path/to/geckodriver")`


## API Documentation


| Parameter   | Type     | Description                                 |
| :---------- | :------- | :------------------------------------------ |
| `shortcode` | `string` | **Required**. Shortcode of a shortened URL. |

#### Return the original URL and the shortcode.

```
  GET /api/shorten/${shortcode}
```

```
200 OK
Content-Type: "application/json"

{
  "url": "http://example.com",
  "shortcode": "example"
}
```

#### Return the stats of the shortcode

```
  GET /api/stats/${shortcode}
```

```
200 OK
Content-Type: "application/json"

{
  "startDate": "2012-04-23T18:25:43.511Z",
  "lastSeenDate": "2012-04-23T18:25:43.511Z",
  "redirectCount": 1,
  "shortcode": "example",
  "url": "http://example.com",
}
```
