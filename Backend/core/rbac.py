from fastapi import Depends, HTTPException, status
from core.auth_dependency import verify_token


def require_roles(allowed_roles: list):
    """
    Role-based access dependency.

    Usage:
    current_user = Depends(require_roles(["admin"]))
    """

    def role_checker(current_user: dict = Depends(verify_token)):

        user_role = current_user.get("role") # Assuming JWT payload has a "role" field , payload = {"sub": "user123", "role": "admin", "type": "access"}

        if user_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action"
            )

        return current_user

    return role_checker