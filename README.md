# Dz-Mouhami

- The Backend Source code for the Dz Mouhami project for the software enginnering module in first year superios class in Estin School , A Website to Seach for lawyers and make an appointement with them , also  the user can review lawyers and search for lawyer based on their needs
- the api is currently hosted on <https://dz-mouhami.onrender.com/>

## Features

- **Authentication**:
  - Login with Google OAuth
  - Login for lawyers
  - Sign up for new lawyers
  - Check email availability
  
- **User Management**:
  - Retrieve all users
  - Retrieve user profile
  - Delete user account
  - Update user email, profile picture, and password
  
- **Appointment Management**:
  - Create appointments
  - Retrieve lawyer appointments
  - Retrieve pending appointments for lawyers
  - Retrieve all appointments
  - Respond to appointments by lawyers
  
- **Review Management**:
  - Retrieve reviews of a lawyer
  - Add a review for a lawyer
  - Retrieve reviews given by a lawyer
  
- **Lawyer Management**:
  - Retrieve highest-rated lawyers
  - Retrieve details of a lawyer
  - Retrieve schedule of a lawyer
  - Retrieve all lawyers
  - Retrieve accepted and pending lawyers
  - Update lawyer profile
  - Respond to lawyer requests
  
- **Location Management**:
  - Retrieve list of wilayas
  - Retrieve list of cities within a wilaya
  
- **Category Management**:
  - Retrieve all available categories for lawyers

## Api Endpoints

### Authentication Endpoints

- **loginWithGoogle**: `GET /api/auth/google-auth`
- **login-lawyer**: `POST /api/auth/login`
- **sign up new lawyer**: `POST /api/auth/register-lawyer`
- **check-email**: `POST /api/auth/check-email`

### User Endpoints

- **get all users**: `GET /api/users`
- **get user**: `GET /api/users/lawyer/me`
- **delete user**: `DELETE /api/users/1`
- **update email**: `PATCH /api/users/email`
- **update profile picture**: `PATCH /api/users/1/image`
- **update password**: `PATCH /api/users/password`

### Appointment Endpoints

- **create appointment**: `POST /api/appointements/create`
- **get lawyer appointments**: `GET /api/appointements/`
- **get lawyer pending appointments**: `GET /api/appointements/lawyer/pending`
- **get all appointments**: `GET /api/appointements/`
- **respond appointment**: `POST /api/appointements/lawyer/respond`

### Review Endpoints

- **get reviews of lawyer**: `GET /api/reviews/3`
- **add review**: `POST /api/reviews/add`
- **get my reviews**: `GET /api/reviews/lawyer`

### Lawyer Endpoints

- **highest rated**: `GET /api/lawyers/highest_rated?limit=3`
- **get lawyer**: `GET /api/lawyers/1`
- **get lawyer schedule**: `GET /api/lawyers/1`
- **get all lawyers**: `GET /api/lawyers`
- **get accepted lawyers**: `GET /api/lawyers/accepted`
- **get pending lawyers**: `GET /api/lawyers/pending`
- **update profile**: `PATCH /api/lawyers/`
- **respond lawyer**: `PATCH /api/lawyers/lawyer/response`

### Location Endpoints

- **get wilayas**: `GET /api/location/wilaya`
- **get cities**: `GET /api/location/cities/16`

### Category Endpoints

- **get all categories**: `GET /api/categories`

## Installation

# Installation

To run the Dz-mouhami FastAPI application locally, follow these steps:

1. **Clone the Repository:**

- git clone <https://github.com/yourusername/dz-mouhami.git>

2. **Navigate to the Project Directory:**

- cd dz-mouhami

3. **Install Dependencies:**

- pip install -r requirements.txt

4. **Set Up Environment Variables:**

- Create a `.env` file in the root directory.
- Add necessary environment variables like database connection details, API keys, etc.

5. **Run the Application:**

- uvicorn main:app --reload

6. **Access the API:**

- Once the server is running, access the API endpoints using a tool like Postman or your web browser.

7. **Start Developing:**

- You're now ready to start developing and testing your FastAPI application!

Make sure to customize environment variables and configurations based on your specific setup

## Links

- No Links For Now

### Written by Fares Bekkouche
