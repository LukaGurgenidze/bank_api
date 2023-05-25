# Fake Bank API

The Fake Financial Institution API provides a backend HTTP API for bank employees to manage bank accounts and perform transactions. It allows creating new accounts, transferring amounts between accounts, and retrieving account balances and transfer history.

## Prerequisites

Before running the project locally, ensure you have installed [Python](https://www.python.org/downloads/) on your device. 


## Getting Started

To run the Fake Bank API on your local machine, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/your-username/fake-financial-institution-api.git
   ```

2. Navigate to the project directory:
   ```
   cd backend
   ```

3. Create a virtual environment:
    ```
    python -m venv venv
    ```

4. Activate the virtual environment:\
    For Windows:
    ```
    venv\Scripts\activate
    ```
    For macOS/Linux:
    ```
    source venv/bin/activate
    ```

5. Install the project dependencies:
   ```
   pip install -r requirements.txt
    ```

6. Set up the database:
   ```
    python manage.py migrate
    ```

7. Start the development server:
   ```
    python manage.py runserver
    ```

8. The API will be accessible at http://localhost:8000/swagger

9. To create a user, run the following command and follow the instructions:
    ```
    python3 manage.py createsuperuser
    ```
    This will enable you to login through http://localhost:8000/admin and browse the database

## API Endpoints
POST /api/account/add: Create a new bank account for a customer.\
GET /api/accounts/{account_id}/balance: Retrieve the balance for a given account.\
POST /api/transactions/transfer: Transfer an amount between two accounts.\
GET /api/accounts/{account_id}/transfer-history: Retrieve the transfer history for a given account.\