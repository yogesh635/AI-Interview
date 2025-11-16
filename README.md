# Session Management API (Emotion Detection)

This is a small Flask project that implements session management for interview sessions used in an emotion detection pipeline.

## Features
- Start a session: `POST /session/start`
- Mark processing: `POST /session/processing/<session_id>`
- Mark completed: `POST /session/complete/<session_id>`
- Get session info: `GET /session/<session_id>`

## Quick start (local)
1. Create virtualenv (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python app.py
   ```
4. Use HTTP client (Postman / curl). For demo auth, pass `Authorization: Bearer 1` where `1` is the numeric user id.

## Example (curl)
Start session:
```bash
curl -X POST http://localhost:5000/session/start -H "Authorization: Bearer 1"
```

Set processing:
```bash
curl -X POST http://localhost:5000/session/processing/1 -H "Authorization: Bearer 1"
```

Complete:
```bash
curl -X POST http://localhost:5000/session/complete/1 -H "Authorization: Bearer 1"
```

Get details:
```bash
curl http://localhost:5000/session/1 -H "Authorization: Bearer 1"
```

## Notes
- This project uses a simple numeric-token based dummy auth helper for local testing. Replace `utils/jwt_helper.py` with your real JWT validator that returns the `user` object.
