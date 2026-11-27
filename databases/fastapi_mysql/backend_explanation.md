# FastAPI – JWT, WebSocket and CORS

## 1. What is FastAPI?

FastAPI is a Python web framework used to build APIs.

A framework is a collection of ready-made tools and code that helps developers build applications easily.

**Why FastAPI?**
- Build REST APIs.
- Perform CRUD operations.
- Connect with databases like MySQL.
- Implement JWT authentication.
- Build real-time applications using WebSockets.

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}
```

Run the application:

```bash
uvicorn app:app --reload
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 2. What is JWT?

JWT stands for **JSON Web Token**.

JWT is a token-based authentication mechanism used to verify the identity of a user.

### Example

Imagine you have a Student Management Application.

1. Admin enters username and password.
2. FastAPI verifies the credentials.
3. If correct, FastAPI generates a JWT token.
4. Frontend receives the token.
5. Frontend sends this token when accessing protected APIs.
6. Backend verifies the token and allows access.

### Why JWT?

Without JWT, the user might need to send username and password with every request.

With JWT, the user logs in once and uses the generated token for subsequent authenticated requests.

### What is a Secret Key?

A secret key is a confidential value used by the backend to sign and verify JWT tokens.

- Helps verify that the token has not been modified.
- Only the backend should know this key.
- In production, use a strong random key stored in an environment variable.

### JWT Structure

A JWT contains three parts:

```text
HEADER.PAYLOAD.SIGNATURE
```

| Part | Purpose |
|---|---|
| Header | Contains token type and signing algorithm |
| Payload | Contains user information and expiration |
| Signature | Verifies token integrity and authenticity |

**Header Example:**

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

**Payload Example:**

```json
{
  "sub": "admin",
  "role": "admin"
}
```

**Signature:** Generated using the header, payload, and secret key.

Note: JWT payload is encoded, not encrypted by default. Do not store passwords or sensitive information in it.

### Complete JWT Process

```text
User Enters Username & Password
              |
              v
       Frontend Sends
         POST /login
              |
              v
        FastAPI Backend
              |
              v
      Validate Credentials
              |
              v
       Generate JWT Token
              |
              v
       Send Token to Frontend
              |
              v
       Frontend Stores Token
              |
              v
       Access Protected API
              |
              v
     Authorization: Bearer TOKEN
              |
              v
        Backend Verifies Token
              |
         +----+----+
         |         |
       Valid     Invalid
         |         |
         v         v
       Allow     Reject
       Access    Request
```

**Important:** Generating a token and verifying a token are different operations. You must implement token verification to protect APIs.

### What is Bearer Token?

Bearer is an authentication scheme used to send an access token to the backend.

Example:

```http
Authorization: Bearer abc123
```

- Authorization: HTTP request header.
- Bearer: Authentication scheme.
- abc123: Example token value.

---

## 3. What is WebSocket?

Normally, REST APIs follow a request-response model.

The frontend sends a request, and the backend sends a response.

### REST API Communication

```text
Frontend  -------- Request --------> FastAPI

Frontend  <------- Response -------- FastAPI
```

If the frontend needs new information, it generally sends another request.

### WebSocket Communication

WebSocket creates a continuous connection between the frontend and backend.

Both can send messages to each other whenever needed.

```text
          WebSocket Connection

Frontend  <========================> FastAPI

             Two-way Communication
```

This is called **Full-Duplex Communication**.

Examples:
- Chat applications.
- Live notifications.
- Live stock price updates.
- Online gaming.
- Real-time dashboards.

### Understand FastAPI WebSocket Code

**Step 1: Create WebSocket Endpoint**

```python
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
```

- `@app.websocket("/ws")` creates a WebSocket endpoint.
- `/ws` is the URL used by the frontend.
- `async` allows asynchronous communication.
- `websocket` represents the connection.

Frontend connection:

```javascript
const ws = new WebSocket("ws://127.0.0.1:8000/ws");
```

**Step 2: Accept the Connection**

```python
await websocket.accept()
```

FastAPI accepts the frontend's WebSocket connection.

**Step 3: Create an Infinite Loop**

```python
while True:
```

We use `while True` to continuously receive messages from the frontend.

**Step 4: Receive a Message**

```python
message = await websocket.receive_text()
```

Frontend sends:

```javascript
ws.send("Hello Server");
```

Backend receives:

```python
message = "Hello Server"
```

**Step 5: Send a Response**

```python
await websocket.send_text(
    "Server received: " + message
)
```

Backend sends a response to the frontend.

Frontend receives:

```javascript
ws.onmessage = function(event) {
    console.log(event.data);
};
```

**Step 6: Handle Disconnection**

```python
except WebSocketDisconnect:
    print("Client disconnected")
```

When the user closes the browser or disconnects, FastAPI detects the disconnection and raises `WebSocketDisconnect`.

### Complete WebSocket Flow

```text
       FRONTEND (JavaScript)
                |
        new WebSocket("/ws")
                |
                v
         FASTAPI BACKEND
                |
                v
        websocket.accept()
                |
                v
       Connection Established
                |
                v
             while True
                |
                v
        receive_text()
                |
                v
         Receive Message
                |
                v
           send_text()
                |
                v
          Send Response
                |
                v
       FRONTEND RECEIVES
                |
                v
          ws.onmessage()
                |
                v
          Display Message
```

---

## 4. What is CORS?

CORS stands for **Cross-Origin Resource Sharing**.

Before understanding CORS, understand what an origin means.

An origin contains three parts:

1. Protocol
2. Domain or IP address
3. Port number

Example:

```text
Frontend: http://127.0.0.1:5500

Backend:  http://127.0.0.1:8000
```

Are these two applications running on the same origin?

No, because their port numbers are different.

### Why do we need CORS?

Imagine your frontend application is developed using HTML, CSS, and JavaScript.

Your backend application is running using FastAPI.

When JavaScript tries to communicate with FastAPI, the browser applies its same-origin security policy.

CORS allows the backend to specify which frontend origins are permitted to access its resources.

---

## 5. What is Middleware?

Middleware is code that runs between an incoming request and an outgoing response.

Think of middleware as a security checkpoint.

It processes requests before they reach the API endpoint and can also process responses before they reach the frontend.

### Middleware Flow

```text
       FRONTEND
           |
           v
      HTTP REQUEST
           |
           v
        MIDDLEWARE
           |
           v
       FASTAPI API
           |
           v
        RESPONSE
           |
           v
        MIDDLEWARE
           |
           v
        FRONTEND
```

In FastAPI, we use middleware for:
- CORS handling.
- Authentication checks.
- Logging requests.
- Processing responses.

---

## 6. Understanding CORS Middleware Code

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["*"]
)
```

### 1. CORSMiddleware

```python
from fastapi.middleware.cors import CORSMiddleware
```

Imports CORS middleware from FastAPI's underlying Starlette framework.

### 2. app.add_middleware()

```python
app.add_middleware(
    CORSMiddleware,
```

Adds CORS middleware to the FastAPI application.

### 3. allow_origins

```python
allow_origins=["http://127.0.0.1:5500"],
```

Specifies which frontend origin is allowed to access the backend through a browser.

In this example, only this frontend origin is allowed:

```text
http://127.0.0.1:5500
```

If your frontend runs on another port, add that origin too.

Example:

```python
allow_origins=[
    "http://127.0.0.1:5500",
    "http://localhost:3000"
]
```

### 4. allow_methods

```python
allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
```

Specifies which HTTP methods are allowed.

| Method | Purpose |
|---|---|
| GET | Retrieve data |
| POST | Create data |
| PUT | Update complete data |
| PATCH | Update partial data |
| DELETE | Delete data |

For example, if the frontend sends a DELETE request, the configured CORS policy allows that method.

### 5. allow_headers

```python
allow_headers=["*"]
```

Allows all request headers under the configured CORS policy.

**What is an HTTP Header?**

HTTP headers contain additional information about a request or response.

Examples:

**1. Content-Type**

Specifies the format of the data being sent.

```http
Content-Type: application/json
```

**2. Authorization**

Sends the JWT token.

```http
Authorization: Bearer abc123
```

**3. Accept**

Specifies the response format expected.

```http
Accept: application/json
```

**4. Custom Header**

Developers can create their own headers.

```http
X-API-KEY: mykey123
```

Allow only selected headers:

```python
allow_headers=[
    "Content-Type",
    "Authorization",
    "Accept"
]
```

### Complete CORS Middleware Example

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}
```
### query parameter
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_user(name: str, age: int):
    return {
        "message": "User details",
        "name": name,
        "age": age
    }


if name == "main":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



# http://127.0.0.1:8000/users?name=Veera&age=30

# {
#     "message": "User created successfully",
#     "name": "Veera",
#     "age": 30
# }
```
---
