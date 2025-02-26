# Auth Module API Documentation

This document provides detailed information about the `auth_module` API, including endpoints, parameters, and responses.

## Authentication Endpoints

### 1. Register a User
- **Endpoint**: `POST /auth/register`
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
Response:
Success (200):
json
{
  "code": 200,
  "message": "注册成功",
  "data": {
    "username": "string",
    "user_id": integer
  }
}
Failure (400):
json
{
  "code": 400,
  "message": "用户名已存在",
  "data": null
}
Description: Registers a new user with the provided username and password.
2. User Login
Endpoint: POST /auth/login
Request Body:
json
{
  "username": "string",
  "password": "string"
}
Response:
Success (200):
json
{
  "code": 200,
  "message": "登录成功",
  "data": {
    "token": "string"
  }
}
Failure (401):
json
{
  "code": 401,
  "message": "用户名或密码错误",
  "data": null
}
Description: Authenticates a user and returns a JWT token.
3. Send Verification Code
Endpoint: POST /auth/send_verify_code
Request Body:
json
{
  "user_id": integer,
  "verify_type": "string" (e.g., "phone", "email"),
  "content": "string" (e.g., phone number or email)
}
Response:
Success (200):
json
{
  "code": 200,
  "message": "验证码已发送",
  "data": {
    "code": "string"
  }
}
Failure (500):
json
{
  "code": 500,
  "message": "发送失败: error message",
  "data": null
}
Description: Sends a verification code (e.g., SMS or email) to the specified content.
4. Verify Code
Endpoint: POST /auth/verify_code
Request Body:
json
{
  "content": "string" (e.g., phone number or email),
  "code": "string" (verification code)
}
Response:
Success (200):
json
{
  "code": 200,
  "message": "验证成功",
  "data": null
}
Failure (400):
json
{
  "code": 400,
  "message": "验证失败",
  "data": null
}
Description: Verifies the provided verification code.
Development Guide
Prerequisites
Python 3.8+
Virtual environment (venv)
Installed dependencies: pip install -r requirements.txt (if used)
Setup
Clone the repository:
bash
git clone https://github.com/drunksoul2021/auth_module.git
cd auth_module
Create and activate a virtual environment:
bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
Install dependencies:
bash
pip install .
Run tests:
bash
pytest tests/ -v
Contributing
Fork the repository, make changes, and submit a pull request.
Ensure tests pass and add new tests for new features.
License
MIT License - see the LICENSE file for details.
```