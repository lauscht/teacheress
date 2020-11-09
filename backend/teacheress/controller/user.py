from .routing import router, cbv
from typing import AnyStr
from teacheress.models import User

@cbv(router)
class UserController:

    @router.get("/user/{item_id}")
    def get(self, item_id: AnyStr) -> User:
        user = User(name="Tobias Lausch", email="toby@lauscht.com")
        return user

