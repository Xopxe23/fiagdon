from src.api.users.router import fastapi_users

current_user = fastapi_users.current_user()

current_active_verified_user = fastapi_users.current_user(active=True, verified=True)

current_superuser = fastapi_users.current_user(active=True, superuser=True)
