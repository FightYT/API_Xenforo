from pydantic import BaseModel, Field

# class me(BaseModel):
#     code: int  = Field(alias="code")
#     json: dict = Field(alias="json")
#     requests: dict = Field(alias="request")

class GetME(BaseModel):
    creation_watch_state: str
    interaction_watch_state: str
    content_show_signature: bool
    email_on_conversation: bool
    push_on_conversation: bool
    receive_admin_email: bool
    show_dob_year: bool
    show_dob_date: bool
    location: str
    website: str
    about: str
    signature: str
    allow_view_identities: str
    allow_post_profile: str
    allow_receive_news_feed: str
    allow_send_personal_conversation: str
    visible: bool
    activity_visible: bool
    timezone: str
    custom_title: str

    code: int
    request: dict

class Error(BaseModel):
    error_code:str
    request:dict