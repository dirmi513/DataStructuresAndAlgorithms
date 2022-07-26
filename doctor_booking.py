class Weekday(Enum):
  MONDAY = 0
  TUESDAY = 1
  WEDNESDAY = 2
  THURSDAY = 3
  FRIDAY = 4
  SATURDAY = 5
  SUNDAY = 6
  
  @classmethod
  def weekday_from_int(self, weekday: int) -> Weekday:
    try:
      cls.Weekday(weekday)
    except:
      raise NotAWeekdayError("The provided value is not a weekday")


class Insurance:
  def __init__(self, provider: str, id: int) -> None:
    self.provider = provider
    self.id = id
    
    
class Doctor:
  def __init__(
    self, 
    name: str, 
    phone: str, 
    specialty: str, 
    insurances_taken: Optional[Set[Insurance]] = set()
  ) -> None:
    self.name = name
    self.phone = phone
    self.specialty = specialty 
    self.insurances_taken = insurances_taken 
    self.patients: Set[Patient] = set()
    self.weekday_to_hours_available: Dict[Weekday, Tuple[datetime.datetime, datetime.datetime]] = dict()
    self.days_off: Set[datetime.date] = set() 
    self.appointments: Set[datetime.datetime] = set()
  
  def add_patient(self, patient: Patient) -> bool:
    if patient.insurance not in self.insurances_taken:
      raise InsuranceNotTakenError()
    
    if patient in self.patients:
      return False
    
    self.patients.add(patient)
  
  def new_appointment(self, patient: Patient, date: datetime.datetime) -> bool:
    weekday = Weekday.weekday_from_int(date.weekday())
    if self.weekday_to_hours_available:
    
               
class Patient:
  def __init__(
    self, 
    first_name: str, 
    last_name: str, 
    phone: int, 
    address: str, 
    insurance: Insurance
  ) -> None:
    self.first_name = first_name
    self.last_name = last_name
    self.phone = phone
    self.address = address
    self.insurance_id = insurance_id
    self.insurance = insurance
    self.appointments = deque([])
  
  def book_appointment(
    self, 
    year: int,
    month: int,
    day: int,
    start_hour: int,
    start_minute: int,
    doctors_office: DoctorsOffice
  ) -> bool:
    if not doctors_office.existing_patient(self):
      try:
        doctors_office.add_patient(self)
      except InsuranceNotTakenError:
        return False
    
    start_time = datetime.datetime(
      year=year, 
      month=month, 
      day=day, 
      hour=start_hour, 
      minute=start_minute
    )
    if not doctors_office.is_time_slot_available(
      date, start_time
    ):
      raise TimeSlotNotAvailableError(
        "Time slot is not available anymore, please try a different time slot."
      )
      
    appointment_booked = doctors_office.book_appointment(
      self, date, start_time
    )
    if appointment_booked:
      return True
    
    return False

    
  
  def cancel_appointment(    
    self, 
    date: datetime.Date, 
    start_time: str,
    doctors_office: DoctorsOffice
  ) -> bool:
    return True
                              
#     doctors_office.cancel_appointment(self, date, start_time
                              
class DoctorsOffice:
  def __init__(self, name: str, address: str, phone: int) -> None:
    self.office_name = name
    self.address = address
    self.phone = phone
    self.doctors: Set[Doctor] = set()
                                      
  def add_doctor(self, doctor: Doctor) -> None:
    seld.doctors.add(doctor)
  
  def book_appointment(self, doctor: Optional[Doctor]) -> bool:
    if doctor:
                              
                                      
