# tests/test_models.py
from auth_module.models import UserStorage, VerifyStorage
from abc import ABC

class MockUserStorage(UserStorage):
    def find_by_username(self, username):
        return {"user_id": 1, "username": username, "password_hash": "hash", "salt": "salt"}

    def save_user(self, user_data):
        print(f"Saving user: {user_data}")

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

if __name__ == "__main__":
    user_storage = MockUserStorage()
    verify_storage = MockVerifyStorage()

    # 测试UserStorage
    user = user_storage.find_by_username("testuser")
    print("Found user:", user)
    user_storage.save_user({"username": "testuser", "password_hash": "hash", "salt": "salt"})
    user_storage.update_user(1, {"last_login_time": "2025-02-25"})
    user_storage.log_login(1, "password", "127.0.0.1", 1)

    # 测试VerifyStorage
    verify_storage.save_verify_code(1, "phone", "1234", "1234567890", "2025-02-25 12:00:00")
    is_valid = verify_storage.check_verify_code("1234567890", "1234")
    print("Verify code valid:", is_valid)
    verify_storage.update_verify_status("1234567890", "1234", 1)