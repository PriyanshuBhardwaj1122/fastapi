from pydantic_settings import BaseSettings,SettingsConfigDict
from typing import Optional
class Settings(BaseSettings):
    database_hostname:str
    database_port:str
    database_password:Optional[str]=None
    database_name:str
    algorithm:str
    access_token_expire_minutes:int
    secret_key:str
    database_username:str

    model_config=SettingsConfigDict(
        env_file=".env"
    )

settings=Settings()    

