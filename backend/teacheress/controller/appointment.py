from .routing import router, cbv
from typing import AnyStr, List
from teacheress.models import Appointment

appointments = [
    dict(date="2020-11-09 09:00", title="Arbeit1", text="Dies ist ein längerer text.", tags=["7b"]),
    dict(date="2020-11-09 10:00", title="Arbeit2", text="Dies ist ein längerer text.", tags=["7a"]),
    dict(date="2020-11-09 12:00", title="Arbeit3", text="Dies ist ein längerer text.", tags=["7b"]),
]
appointments = [Appointment.parse_obj(_) for _ in appointments]

@cbv(router)
class AppointmentController:

    @router.get("/appointment")
    def get(self, ) -> List[Appointment]:
        return appointments

    @router.get("/appointment/{item_id}")
    def get_by_id(self, item_id: AnyStr) -> Appointment:
        return appointments[0]

