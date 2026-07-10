# Django_rest_framework-ostad


### 3. Book APIs

Create the following APIs using `ModelViewSet`.

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/api/books/` | Retrieve all books |
| **POST** | `/api/books/` | Create a new book |
| **GET** | `/api/books/<id>/` | Retrieve a single book |
| **PUT** | `/api/books/<id>/` | Update a book |
| **PATCH** | `/api/books/<id>/` | Partially update a book |
| **DELETE** | `/api/books/<id>/` | Delete a book |


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