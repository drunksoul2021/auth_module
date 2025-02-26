# tests/test_services.py
from auth_module import init_auth
from auth_module.models import UserStorage, VerifyStorage
from auth_module.config import load_config  # 修正为从包根目录导入 config

class MockUserStorage(UserStorage):
    def find_by_username(self, username):
        return {"user_id": 1, "username": username, "password_hash": "hashed", "salt": "salt"} if username == "testuser" else None

    def save_user(self, user_data):
        print(f"Saving user: {user_data}")
        return user_data

    def update_user(self, user_id, updates):
        print(f"Updating user {user_id} with {updates}")

    def log_login(self, user_id, login_type, ip, status, fail_reason=None):
        print(f"Logging login: {user_id}, {login_type}, {ip}, {status}, {fail_reason}")

class MockVerifyStorage(VerifyStorage):
    def save_verify_code(self, user_id, verify_type, code, content, expire_time):
        print(f"Saving verify code: {user_id}, {verify_type}, {code}, {content}, {expire_time}")

    def check_verify_code(self, content, code):
        return content == "1234567890" and code == "1234"

    def update_verify_status(self, content, code, status):
        print(f"Updating verify status: {content}, {code}, {status}")

def test_auth_module():
    config = load_config()
    auth = init_auth()
    user_storage = MockUserStorage()
    verify_storage = MockVerifyStorage()
    auth.set_storage(user_storage, verify_storage)

    # 测试注册
    result = auth.register("testuser", "password123")
    print("Register result:", result)

    # 测试登录
    result = auth.login("testuser", "password123")
    print("Login result:", result)

    # 测试发送验证码
    result = auth.send_verify_code(1, "phone", "1234567890")
    print("Send verify code result:", result)

    # 测试验证验证码
    result = auth.verify_code("1234567890", "1234")
    print("Verify code result:", result)

if __name__ == "__main__":
    test_auth_module()