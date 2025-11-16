from functools import wraps
from flask import request, jsonify

# Simple dummy auth decorator for local testing.
# In your real project replace this with actual JWT validation that returns user info.
def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.headers.get('Authorization', '')
        # Expect header: Authorization: Bearer <user-id>
        if not auth.startswith('Bearer '):
            return jsonify({'error': 'Authorization header missing or invalid'}), 401
        token = auth.split(' ', 1)[1].strip()
        if not token.isdigit():
            return jsonify({'error': 'Invalid token format. For local testing use numeric user-id as token.'}), 401
        # For demo purposes, user object is a dict with id
        user = {'id': int(token)}
        return func(user, *args, **kwargs)
    return wrapper
