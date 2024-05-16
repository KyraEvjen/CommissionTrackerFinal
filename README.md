# Commission Tracker, Final Project

Created by Kyra Evjen, Beth Nipper, and Ken Dompier

## Overview

This project is a commission tracker web application designed to help users manage their commissions, portfolios, and payments efficiently.

### Team Roles
- Kyra: Backend, Javascript, CRUD Implementation
- Beth: Backend, Javascript, CRUD Implementation
- Ken: Frontend, Javascript, Stylizing & CSS

## How to Run

1. Ensure all requirements are installed.
2. Create a folder named 'logs' and add an 'app.log' file to store logs.
3. Create an `.env` file with your MongoDB connection, `MONGO_URI`, and a `SECRET_KEY`.
4. Create virtual environment with `python -m venv venv`.
6. Activate the virtual environment with `.\venv\scripts\activate`.
7. Run the application using Uvicorn: `uvicorn main:app --reload`.

## Screenshots

**Login Page**
![image](https://github.com/KyraEvjen/CommissionTrackerFinal/assets/156963640/c06eb2e0-11ff-42c9-982a-508b8644f10f)
**Commission Page**
![image](https://github.com/KyraEvjen/CommissionTrackerFinal/assets/156963640/a849f130-4327-4e11-8d41-a5ca3c69e7be)
**Payments Page**
![image](https://github.com/KyraEvjen/CommissionTrackerFinal/assets/156963640/03cc71dc-9321-4c4d-b04e-587052cb758b)
**Portfolio Page**
![image](https://github.com/KyraEvjen/CommissionTrackerFinal/assets/156963640/95beaee6-df9d-4a7f-80cd-4a8847d191e7)
**Add Commission Model**
![image](https://github.com/KyraEvjen/CommissionTrackerFinal/assets/156963640/f8f998c2-012c-475c-9976-46c7efca993f)
**Add Portfolio Item Model**
![image](https://github.com/KyraEvjen/CommissionTrackerFinal/assets/156963640/7a3bf50a-f3dc-4fc3-8a8a-3eb1ef9eff01)


## Backend Code

### Commission.py

#### Endpoints
- Add Commission: `POST /commissions`
- Get Commissions: `GET /commissions`
- Get Commission by ID: `GET /commissions/{id}`
- Update Commission: `PUT /commissions/{commission_id}`
- Delete Commission: `DELETE /commissions/{commission_id}`


### logging_setup.py

- Console Logging: Logs are displayed on the console.
- File Logging: Logs are saved to a file named `app.log` in the `logs` directory. Log files are rotated daily.

### main.py

#### Endpoints
- `/`: Displays the login page.
- `/commissions`: Handles commission-related operations.
- `/portfolios`: Handles portfolio-related operations.
- `/payments`: Handles payment-related operations.
- `/users`: Handles user-related operations.

#### Structure
- `main.py`: Contains the FastAPI application setup.
- `commission.py`: Defines commission-related endpoints and logic.
- `portfolio.py`: Defines portfolio-related endpoints and logic.
- `payment.py`: Defines payment-related endpoints and logic.
- `user.py`: Defines user-related endpoints and logic.
- `frontend/`: Contains frontend files (e.g., HTML, CSS, JavaScript).


**model.py**

Represents a commission with the following fields:
- `_id`: Commission ID
- `mongodb_id`: MongoDB ID (aliased as `_id`)
- `title`: Commission title
- `description`: Commission description
- `status`: Commission status
- `width`: Width of the status bar
- `color`: Color of the status bar
- `date`: Date commission started

Commission Request Model

Represents a request body for creating or updating a commission with the following fields:
- `title`: Commission title
- `description`: Commission description
- `status`: Commission status
- `width`: Width of the status bar
- `color`: Color of the status bar
- `date`: Date commission started

User Model

Represents a user with the following fields:
- `username`: User's username
- `password`: User's password

Portfolio Model

Represents a portfolio with the following fields:
- `_id`: Portfolio ID
- `mongodb_id`: MongoDB ID (aliased as `_id`)
- `name`: Portfolio Item name
- `image`: URL of the portfolio image
- `description`: Item description

Portfolio Request Model

Represents a request body for creating or updating a portfolio with the following fields:
- `name`: Portfolio item name
- `image`: URL of the portfolio image
- `description`: Item description

Payment Model

Represents a payment with the following fields:
- `_id`: Payment ID
- `mongodb_id`: MongoDB ID (aliased as `_id`)
- `status`: Payment status
- `amount`: Payment amount

Payment Request Model

Represents a request body for creating or updating a payment with the following fields:
- `status`: Payment status
- `amount`: Payment amount


**payment.py**

Routes

POST /payments
- Creates a new payment.

GET /payments
- Retrieves all payments.
  
GET /payments/{id}
- Retrieves a payment by its ID.

PUT /payments/{payment_id}
- Updates a payment by its ID.

DELETE /payments/{payment_id}
- Deletes a payment by its ID.

**portoflio.py**

Routes

POST /portfolios
- Creates a new portfolio.
  
GET /portfolios
- Retrieves all portfolios.
  
GET /portfolios/{id}
- Retrieves a portfolio by its ID.
  
PUT /portfolios/{portfolio_id}
- Updates a portfolio by its ID.
  
DELETE /portfolios/{portfolio_id}
- Deletes a portfolio by its ID.

**security.py**
- The hash_password function takes a plain text password as input and returns its hashed version.
- The verify_password function takes a plain text password and its hashed version as inputs and returns True if the password matches the hash, otherwise False.

**user_manager.py**
- User Creation and authentication
- MongoDB integration for storin guser data securely
- Password hashing for enhanced security

**user.py**
_API Endpoints_

POST /signup: Create a new user account.
- Request Body: JSON object containing username and password.
- Response: JSON object with message and user ID.

POST /login: Log in with existing user credentials.
- Request Body: JSON object containing username and password.
- Response: JSON object with message, username, and JWT token.

GET /users/me: Get details of the current logged-in user.
- Authentication: Bearer token.
- Response: JSON object with user details.

Authentication
Authentication is done using JWT (JSON Web Tokens).
The SECRET_KEY provided in the .env file is used to encode and decode JWT tokens.
User passwords are hashed using bcrypt for security.

Plans to implement functional Admin/User roles are reminent in the user.py code, but are not currently functional. It is a feature to be added in the future.

## Frontend Code

### user.js & login.html

#### HTML Structure
- Ensure the HTML file contains elements with specific IDs for login and signup forms.

#### Backend Integration
- Interacts with a backend server for user authentication. Requires endpoints `/login` and `/signup` on the server.

#### Functions
- `loginUser(username, password)`: Sends a login request to the `/login` endpoint.
- `signupUser(username, password)`: Sends a signup request to the `/signup` endpoint.

#### Event Listeners
- Attached to form submission events for login and signup.
- Additional listeners for toggling between login and signup forms.

### main.js & index.html

#### Main Content
- Navbar: Navigation links to different sections of the application.
- Title: Displays the title of the page ("Commissions").
- Add New Commission Button: Triggers modal for adding a new commission.
- Commissions Display Area: Displays the list of commissions.

#### Modals
- Modal for Adding a New Commission
- Modal for Editing a Commission
- Deleting a Commission (feature to be added in the future)

#### Scripts
- Handles user interactions, data management, and API requests.

### Portfolio.js & Portfolio.html

#### Functionality
- Manages portfolio items: fetching, adding, editing, and deleting.

#### Structure
- Similar to main.js & index.html, but tailored for portfolio management.

### Payment.js & Payment.html

#### Functionality
- Manages payment transactions: fetching, adding, editing, and deleting.

#### Structure
- Similar to portfolio.js & portfolio.html, but for payments.

### Styles

#### pfstyles.css
- Defines styles specific to portfolio pages.

#### styles.css
- Defines general styles for the application.

## Assets

### Favicon
![Favicon](https://github.com/KyraEvjen/CommissionTrackerFinal/assets/156963640/f60baee1-8d86-4756-b5bf-a297a18fa301)

### SFX Folder
- Contains sounds for the application.

### Visual Folder
- Contains visual assets, including GIFs.
