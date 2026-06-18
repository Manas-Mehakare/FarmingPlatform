# AgriBizness

AgriBizness is a role-based agricultural marketplace developed using Django and PostgreSQL. The platform connects farmers and corporate buyers through a centralized marketplace where agricultural products can be listed, managed, and purchased.

Farmers can create and manage product listings, while registered users can browse products, place orders, and track order status. The system includes inventory validation, automatic price calculation, and role-specific dashboards.

## Features

### User Management
- User Registration
- User Login and Logout
- Role-Based Access Control
  - Farmer
  - Corporate

### Product Management
- Add Products
- Edit Products
- Delete Products
- View Product Details
- Marketplace Listings

### Order Management
- Place Orders
- Automatic Total Price Calculation
- Inventory Validation
- Quantity Availability Checks
- Order Tracking

### Order Status
- Pending
- Shipping
- Delivered
- Cancelled

### Additional Features
- Farmer Dashboard
- Corporate Orders Dashboard
- Hindi Localization Support
- Responsive Interface using Bootstrap 5

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Django | Web Framework |
| PostgreSQL | Database |
| Bootstrap 5 | Frontend Styling |
| HTML/CSS | User Interface |
| Django Authentication | User Management |

## Project Structure

```text
AgriBizness/
│
├── AgriBizness/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── mainApp/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── locale/
│   └── hi/
│
├── manage.py
├── .env
└── .gitignore
```

## Available Pages

- Home
- About
- Marketplace
- Product Details
- Sign Up
- Login
- Farmer Dashboard
- Add Product
- Edit Product
- Delete Product
- Farmer Orders
- Corporate Orders
- Update Order Status

## Installation

### Clone the Repository

```bash
git clone https://github.com/Manas-Mehakare/FarmingPlatform.git
cd FarmingPlatform
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create PostgreSQL Database

```sql
CREATE DATABASE agribizness;
```

### Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=agribizness
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Business Logic

### Product Management

- Farmers can create product listings.
- Farmers can edit their own products.
- Farmers can delete their own products.

### Ordering System

- Users can place orders on available products.
- Quantity availability is validated before order creation.
- Orders exceeding available stock are rejected.
- Total order price is calculated automatically.

### Order Tracking

Farmers can update order status through the dashboard:

- Pending
- Shipping
- Delivered
- Cancelled

## Future Enhancements

- Product Search and Filtering
- Product Categories
- Product Images
- Payment Gateway Integration
- Email Notifications
- Analytics Dashboard
- Mobile Application Support

## Author

Manas Mehakare

B.Tech Computer Science and Engineering (AI)  
MIT-ADT University, Pune

GitHub: https://github.com/Manas-Mehakare

## License

This project was developed for educational purposes.
