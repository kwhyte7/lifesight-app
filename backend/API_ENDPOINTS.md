# LifeSight Backend API Endpoints

## Base URL
All endpoints are relative to `http://localhost:8000/api`

## Authentication
Most endpoints require authentication. Include a valid JWT token in the Authorization header:
```
Authorization: Bearer <token>
```

## Endpoints

### 1. Chat Endpoints

#### POST /api/chat
Send a message to the AI assistant.

**Request Body:**
```json
{
  "message": "string",
  "conversation_id": "string (optional)",
  "user_id": "string (optional)"
}
```

**Response:**
```json
{
  "id": "string",
  "reply": "string",
  "conversation_id": "string",
  "timestamp": "string (ISO 8601)"
}
```

#### GET /api/chat/history
Retrieve chat history for the authenticated user.

**Query Parameters:**
- `limit`: number (optional, default: 50)
- `offset`: number (optional, default: 0)
- `conversation_id`: string (optional)

**Response:**
```json
{
  "messages": [
    {
      "id": "string",
      "content": "string",
      "sender": "user|ai",
      "timestamp": "string (ISO 8601)",
      "conversation_id": "string"
    }
  ],
  "total": 100
}
```

#### DELETE /api/chat/history
Clear chat history for the authenticated user.

**Query Parameters:**
- `conversation_id`: string (optional) - If provided, clears only that conversation

**Response:**
```json
{
  "success": true,
  "message": "History cleared"
}
```

### 2. Health Data Endpoints

#### GET /api/health/summary
Get a health summary for the authenticated patient.

**Response:**
```json
{
  "patient_id": "string",
  "summary": {
    "resting_heart_rate": {
      "current": 65,
      "trend": "stable",
      "change_percentage": -2
    },
    "sleep": {
      "average_duration_hours": 7.5,
      "quality_score": 85,
      "trend": "improving"
    },
    "activity": {
      "daily_steps": 8500,
      "active_minutes": 45,
      "trend": "stable"
    }
  },
  "last_updated": "string (ISO 8601)"
}
```

#### GET /api/health/alerts
Get health alerts for the authenticated user (patient or doctor).

**Query Parameters:**
- `status`: "active|resolved|all" (optional, default: "active")
- `severity`: "low|medium|high|critical" (optional)

**Response:**
```json
{
  "alerts": [
    {
      "id": "string",
      "patient_id": "string",
      "type": "heart_rate|sleep|activity|custom",
      "severity": "low|medium|high|critical",
      "message": "string",
      "timestamp": "string (ISO 8601)",
      "status": "active|resolved",
      "resolved_at": "string (ISO 8601) (optional)"
    }
  ]
}
```

### 3. Patient-Doctor Endpoints

#### GET /api/patients
Get list of patients for the authenticated doctor.

**Query Parameters:**
- `search`: string (optional)
- `status`: "active|inactive|all" (optional, default: "active")
- `limit`: number (optional, default: 20)
- `offset`: number (optional, default: 0)

**Response:**
```json
{
  "patients": [
    {
      "id": "string",
      "name": "string",
      "email": "string",
      "last_activity": "string (ISO 8601)",
      "health_status": "good|fair|poor|critical",
      "alerts_count": 3
    }
  ],
  "total": 50
}
```

#### GET /api/patients/{patient_id}/data
Get health data for a specific patient (doctor access only).

**Query Parameters:**
- `data_type`: "sleep|heart_rate|activity|all" (optional, default: "all")
- `start_date`: string (ISO 8601) (optional)
- `end_date`: string (ISO 8601) (optional)
- `granularity`: "hourly|daily|weekly|monthly" (optional, default: "daily")

**Response:**
```json
{
  "patient_id": "string",
  "data": {
    "sleep": [
      {
        "date": "string (YYYY-MM-DD)",
        "duration_minutes": 450,
        "deep_sleep_minutes": 120,
        "rem_sleep_minutes": 90,
        "light_sleep_minutes": 210,
        "awake_minutes": 30,
        "quality_score": 85
      }
    ],
    "heart_rate": [
      {
        "timestamp": "string (ISO 8601)",
        "bpm": 65,
        "context": "resting|active|sleeping"
      }
    ]
  }
}
```

### 4. Consent Management

#### GET /api/consent
Get consent settings for the authenticated user.

**Response:**
```json
{
  "consents": [
    {
      "id": "string",
      "data_type": "sleep|heart_rate|demographics|medications|allergies|lab_results",
      "granted_to": "doctor|organisation|research",
      "granted_to_id": "string",
      "granted_at": "string (ISO 8601)",
      "expires_at": "string (ISO 8601) (optional)",
      "status": "active|revoked|expired",
      "access_level": "view|download|share_with_third_party|use_for_research"
    }
  ]
}
```

#### POST /api/consent
Update consent settings.

**Request Body:**
```json
{
  "data_type": "sleep|heart_rate|demographics|medications|allergies|lab_results",
  "granted_to": "doctor|organisation|research",
  "granted_to_id": "string",
  "access_level": "view|download|share_with_third_party|use_for_research",
  "expires_at": "string (ISO 8601) (optional)"
}
```

**Response:**
```json
{
  "id": "string",
  "success": true,
  "message": "Consent updated"
}
```

#### DELETE /api/consent/{consent_id}
Revoke a consent.

**Response:**
```json
{
  "success": true,
  "message": "Consent revoked"
}
```

### 5. Authentication

#### POST /api/auth/login
Authenticate a user.

**Request Body:**
```json
{
  "email": "string",
  "password": "string"
}
```

**Response:**
```json
{
  "access_token": "string",
  "token_type": "bearer",
  "expires_in": 3600,
  "user": {
    "id": "string",
    "email": "string",
    "name": "string",
    "user_type": "patient|doctor|admin"
  }
}
```

#### POST /api/auth/register
Register a new user.

**Request Body:**
```json
{
  "email": "string",
  "password": "string",
  "name": "string",
  "user_type": "patient|doctor"
}
```

**Response:**
```json
{
  "access_token": "string",
  "token_type": "bearer",
  "expires_in": 3600,
  "user": {
    "id": "string",
    "email": "string",
    "name": "string",
    "user_type": "patient|doctor"
  }
}
```

#### POST /api/auth/refresh
Refresh an access token.

**Request Body:**
```json
{
  "refresh_token": "string"
}
```

**Response:**
```json
{
  "access_token": "string",
  "token_type": "bearer",
  "expires_in": 3600
}
```

### 6. Emergency Access

#### POST /api/emergency/request
Request emergency access to patient data (doctor only).

**Request Body:**
```json
{
  "patient_id": "string",
  "reason": "string",
  "duration_hours": 24
}
```

**Response:**
```json
{
  "id": "string",
  "patient_id": "string",
  "doctor_id": "string",
  "reason": "string",
  "status": "pending|approved|denied",
  "expires_at": "string (ISO 8601)",
  "requested_at": "string (ISO 8601)"
}
```

#### POST /api/emergency/{request_id}/approve
Approve an emergency access request (patient or admin only).

**Response:**
```json
{
  "success": true,
  "message": "Emergency access approved"
}
```

## Error Responses

All endpoints may return the following error responses:

**400 Bad Request:**
```json
{
  "error": "validation_error",
  "message": "Invalid request parameters",
  "details": {
    "field": ["error message"]
  }
}
```

**401 Unauthorized:**
```json
{
  "error": "unauthorized",
  "message": "Authentication required"
}
```

**403 Forbidden:**
```json
{
  "error": "forbidden",
  "message": "Insufficient permissions"
}
```

**404 Not Found:**
```json
{
  "error": "not_found",
  "message": "Resource not found"
}
```

**429 Too Many Requests:**
```json
{
  "error": "rate_limit_exceeded",
  "message": "Too many requests, please try again later"
}
```

**500 Internal Server Error:**
```json
{
  "error": "internal_error",
  "message": "An unexpected error occurred"
}
```

## Rate Limiting

- Authentication endpoints: 5 requests per minute
- Chat endpoints: 20 requests per minute
- Health data endpoints: 30 requests per minute
- Other endpoints: 60 requests per minute

## WebSocket Endpoints

### /ws/chat
WebSocket connection for real-time chat.

**Messages:**
- `{"type": "message", "content": "string", "conversation_id": "string"}`
- `{"type": "typing", "conversation_id": "string", "is_typing": boolean}`

**Responses:**
- `{"type": "message", "content": "string", "sender": "ai", "timestamp": "string"}`
- `{"type": "typing", "sender": "user|ai", "is_typing": boolean}`
