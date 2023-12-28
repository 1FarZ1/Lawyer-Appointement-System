# @app.post("/appointments/")
# async def create_appointment(appointment: AppointmentCreate, current_user: User = Depends(get_current_active_user)):
#     # Retrieve lawyer based on appointment data
#     lawyer = await Lawyer.query.where(Lawyer.id == appointment.lawyer_id).first()

#     # Validate available time slot with lawyer's schedule
#     if not lawyer.is_available_at(appointment.date, appointment.time):
#         raise HTTPException(
#             status_code=409,
#             detail="Lawyer is not available at the chosen time. Please choose another time."
#         )

#     # Create new appointment object
#     new_appointment = Appointment(
#         user_id=current_user.id,
#         lawyer_id=lawyer.id,
#         date=appointment.date,
#         time=appointment.time,
#         description=appointment.description,
#     )

#     # Save the appointment to the database
#     await new_appointment.save()

#     # Send confirmation email or notification to user and lawyer

#     return {"message": "Appointment created successfully"}