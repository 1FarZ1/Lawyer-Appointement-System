
from fastapi import APIRouter,Depends,HTTPException, Request,status
from typing import List
from app.enums import RoleEnum

from app.models import Appointement,Lawyer,User
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.repository import appointement as appointementRepository ,user as userRep ,  lawyer as lawyerRep

from app.schemas import AppointementSchema
from app.utils.check_permission import check_permission
from app.v1.routers.lawyer import ApproveSchema
from datetime import datetime




router = APIRouter(
    prefix="/api/appointements",
    tags=["appointements"],
)




@router.get("/")
async def get_appointements(request:Request ,db: Session = Depends(get_db)):
#     check_permission(request.state.user,[

# ])
    result:List[Appointement] = appointementRepository.get_all_appointements(db)
    return result

@router.get("/lawyer")
async def get_lawyer_appointements(request:Request ,db: Session = Depends(get_db)):
    check_permission(request.state.user,[
        RoleEnum.LAWYER
])
    id = request.state.user['id']
    result:List[Appointement] = appointementRepository.get_lawyer_appointements(db,lawyer_id=id)
    return result


@router.get('/user')
async def get_user_appointements(request:Request ,db: Session = Depends(get_db)):
#     check_permission(request.state.user,[
#         RoleEnum.USER
# ])
    id = request.state.user['id']
    result:List[Appointement] = appointementRepository.get_user_appointements(db,user_id=id)
    return result


@router.get('/lawyer/approved')
async def get_lawyer_approved_appointements(request:Request ,db: Session = Depends(get_db)):
    check_permission(request.state.user,[
        RoleEnum.LAWYER
])
    id = request.state.user['id']
    result:List[Appointement] = appointementRepository.get_lawyer_accepted_appointements(db,lawyer_id=id)
    return result




@router.get('/lawyer/pending')
async def get_lawyer_pending_appointements(request:Request ,db: Session = Depends(get_db)):
    check_permission(request.state.user,[
        RoleEnum.LAWYER
])
    id = request.state.user['id']
    result:List[Appointement] = appointementRepository.get_lawyer_pending_appointements(db,lawyer_id=id)
    return result




def parse_time(time_str: str):
    return datetime.strptime(time_str, "%I%p").time()


def parse_time_range(time_range: str):
    start_time, end_time = time_range.split("-")
    return parse_time(start_time), parse_time(end_time)
def is_lawyer_available(appointment_date: str, appointment_time_range: str, lawyer_schedules: list):
    appointment_day = datetime.strptime(appointment_date, "%A").strftime("%A")
    for schedule in lawyer_schedules:
        

        if schedule.day_of_week == appointment_day :
                appointment_start_time,appointment_end_time = parse_time_range(appointment_time_range)
                schedule_start_time = datetime.strptime(schedule.start_time, "%H:%M:%S").time()
                schedule_end_time = datetime.strptime(schedule.end_time, "%H:%M:%S").time()

                print(
                    f"Checking schedule: {schedule.day_of_week} {schedule_start_time}-{schedule_end_time}"
                )
        
                print(
                    f"Checking appointment: {appointment_day} {appointment_start_time}-{appointment_end_time}"
                )



                if schedule_start_time == appointment_start_time and schedule_end_time == appointment_end_time:
                    return True



        
        
    return False


@router.post("/create")
async def create_appointement(request: Request, 
    appointementSchema:AppointementSchema,
                              db: Session = Depends(get_db) ):
        
        await check_permission(
            request.state.user, [
            RoleEnum.USER,
        ]
        )

        id = request.state.user['id']


    


        lawyer =  lawyerRep.get_lawyer_by_id(db,appointementSchema.lawyer_id)
        if not lawyer:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Lawyer not found"
            )
        
    
        result = lawyerRep.get_lawyer_schedules(db,appointementSchema.lawyer_id)

        if is_lawyer_available(appointementSchema.date, appointementSchema.time, result):
            print("Lawyer is available for appointment.")
        else:
            print("Lawyer is not available for appointment at the specified time.")



        # result = appointementRepository.create_appointement(db,appointementSchema,id)
        return result 
  
    

@router.post("/lawyer/respond")
async def respond_appointement(request: Request, approaveSchema:ApproveSchema , db: Session = Depends(get_db)):
    check_permission(request.state.user,[
        RoleEnum.LAWYER
])
    if not appointementRepository.get_appointement_by_id(db,approaveSchema.id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Appointement not found"
        )
    lawyer_id = request.state.user['id']
    if  not appointementRepository.appointement_belong_to_lawyer(db,approaveSchema.id,lawyer_id=lawyer_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="you cant respond to this appointement"
        )

    result = appointementRepository.respond_appointement(db,approaveSchema.id,"Approved" if approaveSchema.is_Approved else "Rejected")
    return result


