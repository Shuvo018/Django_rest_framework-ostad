# Django_rest_framework-ostad

### 1. Authentication
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/api/register/` | Register a new user |
| **POST** | `/api/login/` | Login and obtain an authentication token |


### 2. Book Model
● Title
● Author
● Price
● Published Date

### 3. Book APIs
APIs using `ModelViewSet`.
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/api/books/` | Retrieve all books |
| **POST** | `/api/books/` | Create a new book |
| **GET** | `/api/books/<id>/` | Retrieve a single book |
| **PUT** | `/api/books/<id>/` | Update a book |
| **PATCH** | `/api/books/<id>/` | Partially update a book |
| **DELETE** | `/api/books/<id>/` | Delete a book |

### 4. Filtering, Searching & Ordering

#### Filter by Author

GET /api/books/?author=J.K. Rowling

#### Search by Title

GET /api/books/?search=Harry

####  Order by Price

GET /api/books/?ordering=price

GET /api/books/?ordering=-pric

### 5. Pagination

GET /api/books/?page=2

### 6. Throttling

Configure throttling as follows:

● Anonymous Users: 20 requests per minute

● Authenticated Users: 50 requests per minute


## Setup & Run

### Prerequisites

- Python 3.11+

---

### 1. Clone the Repository

```bash
git clone https://github.com/Shuvo018/Django_rest_framework-ostad.git
cd Django_rest_framework-ostad
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```


### 6. Run the Development Server

```bash
python manage.py runserver
```

App: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Admin: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---