# Dz-Mouhami

- The Backend Source code for the Dz Mouhami project for the software enginnering module in first year superios class in Estin School , A Website to Seach for lawyers and make an appointement with them , also  the user can review lawyers and search for lawyer based on their needs
- the api is currently hosted on <https://dz-mouhami.onrender.com/>

## Features

## EndPoints

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

## Tips

## Links

### Written by Fares Bekkouche
