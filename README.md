Created by Kyra Evjen, Beth Nipper, and Ken Dompier

How to run:
Make sure all requirements are installed (if any appear still missing after trying to run, install those)
.\venv\scripts\activate
uvicorn main:app --reload

Create a Logs Folder + Add app.log file to store logs
Create an .env file with your MongoDB connection, MONGO_URI and a SECRET_KEY.

**Backend Code**
Commission.py
_Endpoints_
Add Commission, POST /commissions
Adds a new commission to the database.
Get Commissions, GET /commissions
Retrieves all commissions from the database.
Get Commission by ID, GET /commissions/{id}
Retrieves a commission by its ID from the database.
Update Commission, PUT /commissions/{commission_id}
Updates an existing commission by its ID.
Delete Commission, DELETE /commissions/{commission_id}
Deletes a commission by its ID.


logging_setup.py
Console Logging: Logs are displayed on the console.
File Logging: Logs are saved to a file named app.log in the logs directory. Log files are rotated daily.


main.py
Endpoints
/: Displays the login page.
/commissions: Handles commission-related operations.
/portfolios: Handles portfolio-related operations.
/payments: Handles payment-related operations.
/users: Handles user-related operations.

Structure
main.py: Contains the FastAPI application setup.
commission.py: Defines commission-related endpoints and logic.
portfolio.py: Defines portfolio-related endpoints and logic.
payment.py: Defines payment-related endpoints and logic.
user.py: Defines user-related endpoints and logic.
frontend/: Contains frontend files (e.g., HTML, CSS, JavaScript).
Logging is configured using the logging_setup module.
CORS (Cross-Origin Resource Sharing) is enabled to allow requests from any origin.
Static files (e.g., HTML, CSS, JavaScript) are served from the frontend directory.


model.py
payment.py
portoflio.py
security.py
user_manager.py

**Frontend Code**
