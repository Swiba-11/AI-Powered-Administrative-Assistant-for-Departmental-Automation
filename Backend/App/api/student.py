from fastapi import APIRouter, Depends
from app.core.security import require_role
from app.models.user import User

router = APIRouter(
    prefix="/student",
    tags=["Student"]
)

@router.get("/dashboard")
def student_dashboard(current_user: User = Depends(require_role("student"))):
    return {
        "message": f"Welcome Student {current_user.username}"
    }
