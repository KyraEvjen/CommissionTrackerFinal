Created by Kyra Evjen, Beth Nipper, and Ken Dompier

How to run:
Make sure all requirements are installed (if any appear still missing after trying to run, install those)
.\venv\scripts\activate
uvicorn main:app --reload

Create a Logs Folder + Add app.log file to store logs
Create an .env file with your MongoDB connection, MONGO_URI and a SECRET_KEY.

**Login Page**
![image](https://github.com/KyraEvjen/CommissionTrackerFinal/assets/156963640/c06eb2e0-11ff-42c9-982a-508b8644f10f)
**Commission Page**
![image](https://github.com/KyraEvjen/CommissionTrackerFinal/assets/156963640/a849f130-4327-4e11-8d41-a5ca3c69e7be)
**Payments Page**
![image](https://github.com/KyraEvjen/CommissionTrackerFinal/assets/156963640/03cc71dc-9321-4c4d-b04e-587052cb758b)
**Portfolio Page**
![image](https://github.com/KyraEvjen/CommissionTrackerFinal/assets/156963640/95beaee6-df9d-4a7f-80cd-4a8847d191e7)
**Add Commission Model**
**Add Portfolio Item Model**

**Backend Code**

**Commission.py**

_Endpoints_
Add Commission, POST /commissions
- Adds a new commission to the database.
Get Commissions, GET /commissions
- Retrieves all commissions from the database.
Get Commission by ID, GET /commissions/{id}
- Retrieves a commission by its ID from the database.
Update Commission, PUT /commissions/{commission_id}
- Updates an existing commission by its ID.
Delete Commission, DELETE /commissions/{commission_id}
- Deletes a commission by its ID.


**logging_setup.py**

Console Logging: Logs are displayed on the console.

File Logging: Logs are saved to a file named app.log in the logs directory. Log files are rotated daily.


**main.py** 

_Endpoints_
- /: Displays the login page.
- /commissions: Handles commission-related operations.
- /portfolios: Handles portfolio-related operations.
- /payments: Handles payment-related operations.
- /users: Handles user-related operations.

_Structure_
- main.py: Contains the FastAPI application setup.
- commission.py: Defines commission-related endpoints and logic.
- portfolio.py: Defines portfolio-related endpoints and logic.
- payment.py: Defines payment-related endpoints and logic.
- user.py: Defines user-related endpoints and logic.
- frontend/: Contains frontend files (e.g., HTML, CSS, JavaScript).
- Logging is configured using the logging_setup module.
CORS (Cross-Origin Resource Sharing) is enabled to allow requests from any origin.

Static files (e.g., HTML, CSS, JavaScript) are served from the frontend directory.


**model.py**
Represents a commission with the following fields:
- `_id`: Commission ID
- `mongodb_id`: MongoDB ID (aliased as `_id`)
- `title`: Commission title
- `description`: Commission description
- `status`: Commission status
- `width`: Width of the commission
- `color`: Color of the commission
- `date`: Date of the commission

Commission Request Model

Represents a request body for creating or updating a commission with the following fields:
- `title`: Commission title
- `description`: Commission description
- `status`: Commission status
- `width`: Width of the commission
- `color`: Color of the commission
- `date`: Date of the commission

User Model

Represents a user with the following fields:
- `username`: User's username
- `password`: User's password

Portfolio Model

Represents a portfolio with the following fields:
- `_id`: Portfolio ID
- `mongodb_id`: MongoDB ID (aliased as `_id`)
- `name`: Portfolio name
- `image`: URL of the portfolio image
- `description`: Portfolio description

Portfolio Request Model

Represents a request body for creating or updating a portfolio with the following fields:
- `name`: Portfolio name
- `image`: URL of the portfolio image
- `description`: Portfolio description

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

**Frontend Code**
