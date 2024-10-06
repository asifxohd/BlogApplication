# BlogApplication

BlogApplication is a full-stack web application built with a React frontend and a Django backend. This README provides instructions for setting up and running the application both locally and in a Docker environment, as well as deployment steps for EC2 with Nginx.

## Table of Contents
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Local Setup](#local-setup)
- [Docker Setup](#docker-setup)
- [Configuration](#configuration)
- [Deployment to EC2 with Nginx](#deployment-to-ec2-with-nginx)

## Project Structure

``` git clone https://github.com/asifxohd/BlogApplication.git ```

The project is organized into two main folders:
- `BlogApplication/frontend/`: Contains the React application
- `BlogApplication/backend/`: Contains the Django application

## Prerequisites

- Node.js and npm (for frontend)
- Python 3.x and pip (for backend)
- Docker and Docker Compose (for containerized setup)
- PostgreSQL (for local setup)

## Local Setup

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up the `.env` file:
   ```
   SECRET_KEY=your_secret_key
   POSTGRES_DB=blog
   POSTGRES_USER=your_postgres_user
   POSTGRES_PASSWORD=your_postgres_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

6. Run migrations:
   ```
   python manage.py migrate
   ```

7. Start the Django server:
   ```
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Update the `baseUrl` in the frontend configuration:
   - Open `src/axios/axiosInstance.js`
   - Set `baseURL` to `http://localhost:8000/api/`
   - Open `constents.js`
   - Set `baseURL` to `http://localhost:8000/api/`


4. Start the React development server:
   ```
   npm run dev
   ```

The application should now be running locally, with the frontend on `http://localhost:5173` and the backend on `http://localhost:8000`.

## Docker Setup

1. Ensure Docker and Docker Compose are installed on your system.

2. Navigate to the project root (Backend) directory containing the `docker-compose.yml` file.

3. Build and start the containers:
   ```
   docker-compose up --build
   ```

4. The application will be accessible at `http://localhost:8000`, and the API at `http://localhost:8000`.

## Configuration

### Frontend Configuration

- For local development:
  - In `frontend/src/axios/axiosInstance.js`, set:
    ```javascript
    baseURL: 'http://localhost:8000/api/'
    ```

- For Docker environment:
  - In `frontend/src/axios/axiosInstance.js`, set:
    ```javascript
    baseURL: 'http://localhost:8000/api/'
    ```

### Backend Configuration

- For local development:
  - In `backend/.env`, set:
    ```
    DB_HOST=localhost
    ```

- For Docker environment:
  - In `backend/.env`, set:
    ```
    DB_HOST=postgres_container
    ```


## API Documentation

1.The API documentation for this project is generated using Swagger (OpenAPI). You can access the interactive API documentation when the backend server is running.
To view the API documentation:

Ensure the backend server is running.
Open a web browser and navigate to:

Local development: ```http://localhost:8000/swagger/```
Docker environment:``` http://localhost:8000/swagger/```
Prod environment:```https://cyclehubonline.shop/swagger/```



## Deployment to EC2 with Nginx

1. Launch an EC2 instance with Ubuntu.

2. SSH into your EC2 instance.

3. Install Docker and Docker Compose:
   ```
   sudo apt update
   sudo apt install docker.io docker-compose
   ```

4. Clone your repository:
   ```
   git clone [your-repo-url]
   cd [your-repo-name]
   ```

5. Create a `.env` file in the backend directory with production settings.

6. Build and run your Docker containers:
   ```
   docker-compose up -d --build
   ```

7. Install and configure Nginx:
   ```
   sudo apt install nginx
   ```

8. Create an Nginx configuration file:
   ```
   sudo nano /etc/nginx/sites-available/blogapp
   ```

9. Add the following configuration:
   ```nginx
   server {
       listen 80;
       server_name your_domain.com;

       location / {
           proxy_pass http://localhost:3000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }

       location /api/ {
           proxy_pass http://localhost:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

10. Enable the Nginx configuration:
    ```
    sudo ln -s /etc/nginx/sites-available/blogapp /etc/nginx/sites-enabled
    sudo nginx -t
    sudo systemctl restart nginx
    ```

11. Set up SSL with Let's Encrypt (optional but recommended):
    ```
    sudo apt install certbot python3-certbot-nginx
    sudo certbot --nginx -d your_domain.com
    ```

Your BlogApplication should now be deployed and accessible via your domain name.
