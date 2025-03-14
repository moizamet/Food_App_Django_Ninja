from ninja import NinjaAPI
from ninja_extra import Router
from ninja_jwt.authentication import JWTAuth
from django.db import connection
from attendence.schema import Custom_User_Schema,Miqaat_Schema,Miqaat_Registration_Schema,Miqaat_Registration_Schema_Post
from attendence.models import App_Custom_User,Miqaat,Miqaat_Registration
from django.shortcuts import get_object_or_404

router=Router()


@router.get("/")
def home(request):
    return {"Status":"Success"}

@router.get("/protected",auth=JWTAuth())
def getProtected(request):
    print("Protected Route")
    return {"Status":"This is protected route"}


@router.post("/custom_user",response=Custom_User_Schema)
def create_custom_user(request,request_body:Custom_User_Schema):
    print("adding user model")
    userid=request_body.username
    print(userid)
    print(request_body.model_dump())
    user_obj=App_Custom_User(username=request_body.username,
                             name=request_body.name,
                             its=request_body.its,
                             sabeel=request_body.sabeel,
                             phone_number=request_body.phone_number,
                             email=request_body.email)
    user_obj.set_password(request_body.password)
    user_obj.save()
    created_user=get_object_or_404(App_Custom_User,username=userid)
    print(created_user)
    return created_user


@router.get("/custom_user",response=Custom_User_Schema,auth=JWTAuth())
def get_custom_user(request,userid:str):
    print("finding user with userid")
    print(userid)
    retreive_user=get_object_or_404(App_Custom_User,username=userid)
    return retreive_user

@router.get("/all_miqaat",response=list[Miqaat_Schema],auth=JWTAuth())
def get_all_miqaats(request):
    return Miqaat.objects.all()



#Miqaat Registerations
@router.get("/miqaat_registration/{miqaat_id}",response=list[Miqaat_Registration_Schema],auth=JWTAuth())
def get_all_miqaat_registrations(request,miqaat_id:str):
    registrations=Miqaat_Registration.objects.filter(miqaat=miqaat_id,sabeel_id=request.user.sabeel)
    return registrations


@router.get("/miqaat_registration_all/{miqaat_id}",response=list[Miqaat_Registration_Schema],auth=JWTAuth())
def get_all_miqaat_registrations(request,miqaat_id:str):
    registrations=Miqaat_Registration.objects.filter(miqaat=miqaat_id)
    return registrations


@router.post("/miqaat_registration",response=Miqaat_Registration_Schema,auth=JWTAuth())
def register_for_miqaat(request,request_body:Miqaat_Registration_Schema_Post):
    print("Registering models for miqaat registration")
    print(request_body.model_dump())
    miqaat=get_object_or_404(Miqaat,id=request_body.miqaat_id)
    registration=Miqaat_Registration.objects.create(miqaat=miqaat,
                                                    sabeel_id=request.user.sabeel,
                                                    user_count=request_body.user_count)
    return registration

@router.put("/miqaat_registration",response=Miqaat_Registration_Schema,auth=JWTAuth())
def update_miqaat_registration(request,request_body:Miqaat_Registration_Schema_Post):
    print("Updating Miqaat Registration")
    miqaat_registration_obj=get_object_or_404(Miqaat_Registration,
                                              miqaat=request_body.miqaat_id,
                                              sabeel_id=request.user.sabeel)
    miqaat_registration_obj.user_count=request_body.user_count
    miqaat_registration_obj.save()
    return miqaat_registration_obj


@router.delete("/miqaat_registration",auth=JWTAuth())
def remove_miqaat_registration(request,request_body:Miqaat_Registration_Schema_Post):
    print("Deleting registration")
    miqaat_registration_object=get_object_or_404(Miqaat_Registration,
                                                 miqaat=request_body.miqaat_id,
                                                 sabeel_id=request.user.sabeel)
    if (miqaat_registration_object):
        miqaat_registration_object.delete()
    return {"Status":"Success"}

@router.get("/family_members",response=list[Custom_User_Schema],auth=JWTAuth())
def get_family_members(request,user_id:str):    
    retreive_user=get_object_or_404(App_Custom_User,username=user_id)
    print(f"Sabeel is: {retreive_user.sabeel}")
    if (retreive_user!=None):
        members=App_Custom_User.objects.filter(sabeel=retreive_user.sabeel)
        return members
    
    return list[retreive_user]




    
