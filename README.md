# backend
This backend service was built to provide meat-related information for the Bangkit Capstone Project CAP0366 team. Currently this service is a simple service built using Flask and deployed on GCP's Cloud Run. As a source of information, we utilize the news public API (https://newsapi.org). For further development, it is possible to collect information without needing to rely on public APIs.
## Dependencies
- Flask
- requests

To Install dependencies, run
```
pip install Flask requests
```

## How To Run
### Locally
To run the program locally, make sure you have installed dependencies. Then you can run the program with the command,
```
python main.py
```

### Using Docker
- To run the program with the docker, you need to build the image with the command,
    ```
    docker build --tag backend:tag .
    ```
- Then run the image with docker with the command,
    ```
    docker run --rm -p 8080:8080 -e URL_PUBLIC_NEWS_API="https://newsapi.org/..." backend

    ```

> **_Note:_** Don't forget to complete the URL_PUBLIC_NEWS_API environment variable according to your needs. To use the API from newsapi.org, you need to get an API key by registering on the website.