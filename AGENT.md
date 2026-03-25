# Introduction
LIFESIGHT is an app where patients and doctors can connect, in a seamless, unified interface where patients can track their wearable health data in one place, AI can analyse trands and interperet a  user's healthcare/lifestyle/fitness goals. Strong consent mechanisms in place, and sharing controls will be present in the app.

Patients can upload health data that includes
- sleep patterns
- heart rate
Patients can also link their doctor and GP to their account.
Patients should also have access control on this data, and be able to decide what they want shared.
Doctors can manage multiple patients where the doctor can see the shared data.

Doctors and Patients should also have a chat history with the AI.
Doctors will be able to have a central dashboard for multiple patients, and AI will periodically analyse if patient's health is critical or in an emergency state.

# Tech stack

The project will use:
- React as the frontend
- Fastapi as the backend
- PostgreSQL as the RDBMS

Everything will be seperated into docker containers.

# DATABASE DESIGN

```
notation chen

users [icon: user, color: blue] {
  id string pk
  name string
  membershipId string
  usedFreeTrial datetime
  createdAt datetime
}

membership [color: blue] {
  id string pk
  ownerId string
  isFreeTrial boolean
  createdAt datetime
}

membership_users[color: blue] {
  membershipId string pk
  userid string pk
  createdAt datetime
}

day [color: purple] {
  id string pk
  userid string
  createdAt datetime
}

foods [color: red] {
  id string pk
  name string|null
  imagelink string
  nutritionalInformationId string
  quantity int
  createdAt datetime
}

day_foods [color: purple] { // string
  dayid string pk
  foodid string pk
  createdAt datetime
}

nutritional_information [color: red] {
  id string pk
  name string
  energy int
  fat int
  ofWhichSaturates int 
  carbohydrates int
  ofWhichSugars int
  fibre int
  protien int
  salt int
  createdAt datetime
}

ingredient [color: yellow] {
  id string pk
  standardisedName string
  descriptionFromInternet string
  keydangers string // allergies, carcinogens
  keynegatives string // endocrin disruptors & minor
  keybenefits string // health benefits
  createdAt datetime
}

webSources [color: green] {
  id string pk
  title string
  author string
  url string
  description string
  createdAt datetime
}

ingredient_webSources [color: green] { // another junction
  ingredientid string pk
  sourceid string pk
  createdAt datetime
}

food_ingredient [color: orange] { // junction
  foodid string pk
  ingredientid string pk
  createdAt datetime
}

ingredientname_ingredient [color: yellow] { // another junction
  ingredientname string pk 
  ingredientid string pk
  createdAt datetime
}

ingredient.id - ingredient_webSources.ingredientid
webSources.id - ingredient_webSources.sourceid

// foods.id > food_ingredientname.foodid
//food_ingredientname.ingredientname - ingredientname_ingredient.ingredientname
// ingredient.id - ingredientname_ingredient.ingredientid
food_ingredient.foodid - foods.id
food_ingredient.ingredientid - ingredient.id


day.id < day_foods.dayid
foods.id - day_foods.foodid
foods.nutritionalInformationId > nutritional_information.id

ingredientname_ingredient.ingredientid > ingredient.id

users.id - day.userid

membership.ownerId - users.id
membership.id < membership_users.membershipId 
users.id - membership_users.userid
```
```
```
