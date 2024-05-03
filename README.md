# Commission Tracker Final

Created by Kyra Evjen, Beth Nipper, and Ken Dompier
Kyra - Backend, Javascript, CRUD Implementation, 
Beth - Backend, Javascript, CRUD Implementation, 
Ken - Frontend, Javascript, Stylizing & CSS

**How to run:**
 Make sure all requirements are installed (if any appear still missing after trying to run, pip install those)
- Create a folder named 'logs' + Add 'app.log' file to store logs
- Create an .env file with your MongoDB connection, MONGO_URI and a SECRET_KEY.
- .\venv\scripts\activate
- uvicorn main:app --reload

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


# Backend Code

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

# Frontend Code

**user.js & login.html**
HTML Structure:
Ensure that your HTML file contains elements with the following IDs:
- loginForm: Form element for user login.
- signupForm: Form element for user signup.
- showSignupForm:Element to trigger display of signup form.
- showLoginForm: Element to trigger display of login form.
- loginFormContainer: Container for the login form.
- signupFormContainer: Container for the signup form.
- Backend Integration:
- This code interacts with a backend server for user authentication. You need to have endpoints /login and /signup on your server to handle login and signup requests respectively. These endpoints should accept POST requests with JSON payloads containing username and password fields.

Functions:
- loginUser(username, password): Asynchronously sends a login request to the /login endpoint with the provided username and password. Returns a Promise that resolves with the response data if successful, otherwise throws an error.
- signupUser(username, password): Asynchronously sends a signup request to the /signup endpoint with the provided username and password. Returns a Promise that resolves with the response data if successful, otherwise throws an error.
Event Listeners:
- Event listeners are attached to the login and signup form submission events. When a user submits the form, the corresponding function is called to handle the request.
- Additional event listeners are attached to buttons or elements to toggle between displaying the login and signup forms.

**main.js & index.html**
index.html file serves as the main interface for a commission tracking application. It includes components for displaying commissions, adding new commissions, editing existing commissions, and deleting commissions. Here's an overview of the components included in this file:

**Navbar:** A navigation bar with links to different sections of the application, including "Commissions", "Portfolio", "Payment", and "Login".

**Main Content:**
Title: Displays the title of the page ("Commissions").
Add New Commission Button: Button to trigger the modal for adding a new commission.
Commissions Display Area: Area where the list of commissions will be displayed.

**Modals:**
- Modal for Adding a New Commission: Form for users to input details of a new commission.
- Modal for Editing a Commission: Form for users to edit details of an existing commission.
- Deleting a Commission: Confirmation modal for deleting a commission. (This code exists in the HTML but is not a function that is implemented but is a feature to be added in the future)

**Scripts:** JavaScript scripts are included to handle user interactions, such as adding, editing, and deleting commissions, as well as fetching data from a backend API.

Main.js file contains functionality for handling user interactions and data management within the commission tracking application. Here's a summary of the functionality included in this file:

Commission Management:
- Functions to fetch commissions from the backend API and refresh the UI with the latest data.
- Functions to add, edit, and delete commissions.

Modal Handling:
- Functions to populate the edit modal with commission details when editing a commission.
- Event listeners for form submissions within the modals to handle adding and editing commissions.

Date Selection:
- Event listeners to capture date selection for commission start dates.

Dropdown Selection:
- Event listeners to capture user selection for commission status using dropdown menus.

Progress Bar Management:
- Functions to update progress bars based on selected commission status.

Error Handling:
- Basic error handling for failed API requests or form submissions.

**Portfolio.js & Portfolio.html**

Portfolio.js file contains the functionality for the Portfolio page, It handles actions such as: 
- Fetching existing portfolio items from the backend server.
- Adding new portfolio items.
- Editing existing portfolio items.
- Deleting portfolio items.

Portoflio.html file defines the structure and layout of the Portfolio page of the web application. It includes the following features:
- Navigation bar for easy access to other pages (Commissions, Portfolio, Payment, Login).
- Display area for existing portfolio items.
- Modal for adding new portfolio items.
- Modal for editing existing portfolio items.


**Payment.js & Payment.html**
Payment.js file contains the functionality for the Payment page. It handles actions such as:
- Fetching existing payments from the backend server.
- Adding new payments.
- Editing existing payments.
- Deleting payments.

Payment.html file defines the structure and layout of the Payment page of the web application. It includes the following features:
- Navigation bar for easy access to other pages (Commissions, Portfolio, Payment, Login).
- Display area for existing payment transactions.
- Modal for adding new payment transactions.
- Modal for editing existing payment transactions.


**pfstyles.css**
- :host: Applies padding to the host element.
- div.gallery: Defines the styling for the gallery container, including borders.
- div.gallery:hover: Defines the styling when hovering over the gallery container.
- div.gallery img: Styles the images within the gallery to be responsive.
- div.desc: Defines the styling for the description of each image.
- *: Sets the box-sizing property to border-box for all elements.
- .responsive: Defines the styling for each image in the responsive grid layout.
- @media queries: Adjusts the layout for different screen sizes to ensure responsiveness.
- Adjusts the width of .responsive elements based on screen width.
- Ensures proper layout on screens with a maximum width of 700px and 500px.
- .clearfix:after: Clears floats to ensure proper layout.


  **styles.css**
- html, body: Sets basic styles for the HTML document and body, including height, width, margin, overflow, and font family.
- .app: Styles for the main application container, defining its height, width, background color, border, border radius, padding, and overflow behavior.
- Animated square tile pattern: Defines an animated background pattern with alternating squares.
- .logo: Styles for the application logo.
- .navbar-brand:hover img: Styles for the logo on hover, including a size increase with a smooth transition effect.
- .header-text: Styles for the header text.
- #addNew: Styles for the "Add New Transaction" button, including background color, padding, border radius, and cursor.
- Progress Bars: Styles for progress bars used in the application.
- Form Layout: Styles for adjusting the layout and spacing of form elements.
- .fa-plus: Styles for the plus icon used in the application.
- #commissions: Styles for the commission container, defining its layout, borders, padding, and overflow behavior.
- .options: Styles for options within the commission container.
- #msg and #msg2: Styles for error messages displayed in the application.
- .card: Styles for cards used in the application, defining their width, height, and border.
- Form Input Fields: Styles for input fields in login and signup forms, including padding and width.
- Form Buttons: Styles for buttons in login and signup forms, including margin-top for alignment.
- Labels: Styles for labels in login and signup forms, including margin-bottom for spacing.
- .centered-form: Styles for centering forms vertically within the viewport.
- .hidden: Styles for hiding elements, including opacity, transform for animation, and pointer-events.


**faviconFiremax.ico** : Can be replaced by your prefered icon/artist logo. This is Kyra's Favicon / Artist Logo as default
![image](https://github.com/KyraEvjen/CommissionTrackerFinal/assets/156963640/f60baee1-8d86-4756-b5bf-a297a18fa301)


SFX Folder
- Contains sounds for the application

Visual Folder
- Contains exploding gif that was planned to be used in future update when deleting commissions

