from ninja import ModelSchema, Schema
from attendence.models import App_Custom_User,Miqaat,Venue,Miqaat_Registration
class Custom_User_Schema(ModelSchema):
    class Meta:
        model=App_Custom_User
        fields=["username","name","its","sabeel","email","phone_number","role","password"]


class Venue_Schema(ModelSchema):
    class Meta:
        model=Venue
        fields="__all__"


class Miqaat_Schema(ModelSchema):
    venue:Venue_Schema
    class Meta:
        model=Miqaat
        fields="__all__"

class Miqaat_Registration_Schema(ModelSchema):
    class Meta:
        model=Miqaat_Registration
        fields="__all__"

class Miqaat_Registration_Schema_Post(Schema):
    miqaat_id:int
    sabeel_id:str
    user_count:int        


