from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, EmailStr

class UserBase(BaseModel):
    id: int
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr # need email for resetting passwords
    created_at: datetime

class MembershipBase(BaseModel):
    id: int
    owner_id: int
    is_free_trial: bool
    created_at: datetime

class MembershipUsersBase(BaseModel):
    membership_id: int
    user_id: int
    created_at: datetime

class DayBase(BaseModel):
    id: int
    user_id: int
    created_at: datetime

class DayFoodBase(BaseModel):
    day_id: int
    food_id: int
    created_at: datetime

class FoodBase(BaseModel):
    id: int
    description: str
    user_id: int
    name: str
    image_name: str
    image_path: str
    nutritional_information_id: str
    quantity: str
    created_at: datetime

class NutritionalInformationBase(BaseModel):
    id: int
    per_amount: int
    per_amount_measurement: int
    energy: int
    fat: int
    of_which_saturates: int
    carbohydrates: int
    of_which_sugars: int
    fibre: int
    protien: int
    salt: int
    created_at: int

class FoodIngredientBase(BaseModel):
    food_id: int 
    ingredient_id: int
    created_at: datetime

class IngredientNameIngredientBase(BaseModel):
    ingredient_name: str
    ingrendient_id: int
    created_at: datetime

class IngredientBase(BaseModel):
    id: int
    standardized_name: str
    key_dangers: str
    key_negatives: str
    key_benefits: str
    created_at: datetime

class IngredientWebSourceBase(BaseModel):
    ingredient_id: int
    source_id: int
    created_at: datetime

class WebSourceBase(BaseModel):
    id: int
    title: str
    author: str
    url: str
    description: str
    created_at: datetime
