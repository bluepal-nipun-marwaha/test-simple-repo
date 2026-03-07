# SDK Guide

This guide explains how to use the **Python SDK Client** for interacting with the fictional User & Project Management API.

The SDK provides a simple interface for managing users and projects through a high-level client.

---

# Installation

Clone the repository or copy the SDK file into your project.

Example:

```
git clone <repository-url>
```

Import the SDK in your Python project.

```
from sdk_client import SDKClient
```

---

# Initializing the Client

Before using the SDK, initialize the client with your API base URL and API key.

Example:

```python
from sdk_client import SDKClient

sdk = SDKClient(
    base_url="https://api.example.com",
    api_key="your_api_key"
)
```

---

# User Management

The SDK provides several methods for managing users.

---

## create_user(name, email)

Creates a new user in the system.

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| name | string | Name of the user |
| email | string | Email address of the user |

### Example

```python
sdk.create_user(
    name="Alice",
    email="alice@example.com"
)
```

### Expected Response

```
{
  "status": "success",
  "endpoint": "users"
}
```

---

## get_user(user_id)

Retrieves information about a user.

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| user_id | integer | Unique ID of the user |

### Example

```python
sdk.get_user(1)
```

---

## update_user_email(user_id, new_email)

Updates the email address of a user.

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| user_id | integer | ID of the user |
| new_email | string | Updated email address |

### Example

```python
sdk.update_user_email(
    user_id=1,
    new_email="alice_new@example.com"
)
```

---

## delete_user(user_id)

Deletes a user from the system.

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| user_id | integer | ID of the user to delete |

### Example

```python
sdk.delete_user(1)
```

---

# Project Management

The SDK also provides methods for managing projects.

---

## create_project(name, owner_id)

Creates a new project.

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| name | string | Name of the project |
| owner_id | integer | ID of the user who owns the project |

### Example

```python
sdk.create_project(
    name="AI Documentation Tool",
    owner_id=1
)
```

---

## list_projects()

Retrieves all projects available to the current user.

### Example

```python
sdk.list_projects()
```

### Example Response

```
{
  "status": "success",
  "endpoint": "projects"
}
```

---

# Example Workflow

Below is a simple workflow demonstrating typical SDK usage.

```python
from sdk_client import SDKClient

sdk = SDKClient(
    base_url="https://api.example.com",
    api_key="demo_key"
)

sdk.create_user("Alice", "alice@example.com")

sdk.get_user(1)

sdk.update_user_email(
    user_id=1,
    new_email="alice_new@example.com"
)

sdk.create_project(
    name="AI Documentation Tool",
    owner_id=1
)

sdk.list_projects()
```

---

# Error Handling

The current SDK is a simplified example and does not include advanced error handling.

In a production SDK, additional features would include:

- HTTP response validation
- exception handling
- retry logic
- authentication refresh

---

# Notes for Documentation Automation Testing

This SDK repository is used for testing automated documentation update systems.

Example test scenario:

TC-003 — SDK guide update when method signature changes

Steps:

1. Modify a method signature in the SDK code.
2. Push the commit to the repository.
3. The documentation system detects the change.
4. The SDK guide is automatically updated.

Example change:

Original:

```
create_user(name, email)
```

Updated:

```
create_user(name, email, role)
```

The documentation should update to include the **role** parameter.

---