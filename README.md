# URL-Mask - Gemini API Wrapper

**URL-Mask** is a wrapper API around the **Gemini API** that allows you to make requests to Gemini while masking the actual Gemini URL. Instead of revealing the Gemini API URL, it routes the requests through a custom URL of your choosing.

Built using **FastAPI**, this project allows you to expose a custom API endpoint that interacts with the Gemini API behind the scenes.

## Features

- **Custom URL Masking**: Requests to the Gemini API are routed through your custom URL, keeping the Gemini URL hidden.
- **Seamless Integration**: It acts as a middleware, making it easy to integrate Gemini functionality into your application without exposing the Gemini API endpoint.
- **Security**: By masking the Gemini URL, it adds an extra layer of security and abstraction between your users and the Gemini API.
- **Easy to Use**: Simple API calls with no additional complexity—just pass the same Gemini API requests through the wrapper.
- **FastAPI**: Built on FastAPI, providing high performance and asynchronous request handling.

## How It Works

1. **API Request**: You make a request to the **URL-Mask** API with the same parameters as you would with the original Gemini API.
2. **Proxying to Gemini**: The **URL-Mask** API internally proxies the request to the Gemini API, keeping the Gemini URL hidden from end users.
3. **Response Handling**: Once the response is received from Gemini, **URL-Mask** sends it back to the client, appearing as if the data came from your custom URL.

### Architecture

- **FastAPI** is used to create the API endpoint, handle the requests asynchronously, and ensure high performance and speed.
- It uses **HTTP requests** to proxy calls to Gemini, utilizing the Gemini API credentials securely.
- FastAPI enables **automatic interactive documentation** through **Swagger UI**, making it easy to test and interact with the API.

## Use Cases

- **Hide API URLs**: When you want to hide the actual API endpoints (such as Gemini's) and use a custom domain for your API requests.
- **Control API Access**: Masking the original API URL can help manage access to the Gemini API by adding rate limiting, logging, or authentication features.
- **Simplify API Integrations**: Create a unified API layer that consolidates requests to different services, including Gemini, under your custom domain.
- **High Performance**: Leverage FastAPI's high performance and asynchronous capabilities to handle many concurrent requests efficiently.

## Installation

To install and run **URL-Mask**, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/avocado-beans/url-mask.git
```
2. Run the server

```bash
cd url-mask
uvicorn main:app --reload
```

(Made for a totally legitimate and legal pruposes :])
