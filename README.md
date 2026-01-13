# NextAct Todo App

Ứng dụng quản lý công việc và ghi chú thông minh với tính năng tự động ưu tiên hóa nhờ AI.

## 🎯 Tính Năng

- **Xác thực người dùng**: Đăng ký, đăng nhập an toàn với mã hóa password
- **Quản lý ghi chú**: Tạo, chỉnh sửa, xóa các ghi chú công việc
- **Ưu tiên hóa thông minh**: Sử dụng mô hình ML để tự động gợi ý mức độ ưu tiên
- **Theo dõi trạng thái**: Đánh dấu công việc là "todo", "doing", "done"
- **Hạn chót**: Đặt ngày hạn cho các công việc
- **Thêm nhanh**: Tính năng thêm công việc nhanh chóng
- **Hỗ trợ AI**: Tích hợp Google Generative AI cho các gợi ý thêm

## 🛠️ Công Nghệ

### Backend
- **FastAPI**: Framework web hiện đại, tính năng cao
- **SQLAlchemy**: ORM cho cơ sở dữ liệu
- **PostgreSQL**: Cơ sở dữ liệu quan hệ
- **JWT**: Xác thực token
- **Passlib**: Mã hóa password an toàn
- **Scikit-learn**: Mô hình machine learning

### Frontend
- HTML5
- CSS3
- JavaScript (Vanilla)

### AI & ML
- **Google Generative AI**: Hỗ trợ AI thông minh
- **Joblib**: Lưu và tải mô hình ML

## 📋 Yêu Cầu

- Python 3.8+
- PostgreSQL
- pip (Package manager)

## 🚀 Cài Đặt

### 1. Clone repository
```bash
git clone <repository-url>
cd nextact-todo
```

### 2. Tạo virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 4. Cấu hình cơ sở dữ liệu

Tạo cơ sở dữ liệu PostgreSQL và chạy schema:
```bash
psql -U <username> -d <database_name> -f database/schema.sql
```

### 5. Cấu hình biến môi trường

Tạo file `.env` trong thư mục `backend/`:
```
DATABASE_URL=postgresql://username:password@localhost/database_name
SECRET_KEY=your-secret-key-here
GOOGLE_API_KEY=your-google-api-key
```

### 6. Chạy ứng dụng
```bash
uvicorn backend.app.main:app --reload
```

Ứng dụng sẽ khả dụng tại: `http://localhost:8000`

## 📁 Cấu Trúc Thư Mục

```
nextact-todo/
├── backend/
│   └── app/
│       ├── main.py           # Điểm vào chính
│       ├── auth.py           # Xác thực & đăng nhập
│       ├── notes.py          # Quản lý ghi chú
│       ├── nextact.py        # Ưu tiên hóa AI
│       ├── database.py       # Kết nối DB
│       ├── models.py         # Mô hình SQLAlchemy
│       └── schemas.py        # Pydantic schemas
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── app.js
│   └── templates/
│       ├── login.html
│       ├── register.html
│       └── dashboard.html
├── model/
│   ├── nextact_model.joblib
│   ├── train_nextact_model.py
│   └── nextact_todo_dataset_2000_diverse_vi.csv
├── database/
│   └── schema.sql
├── requirements.txt
└── README.md
```

## 🔌 API Endpoints

### Xác Thực
- `POST /api/auth/register` - Đăng ký tài khoản mới
- `POST /api/auth/login` - Đăng nhập
- `POST /api/auth/logout` - Đăng xuất

### Ghi Chú
- `GET /api/notes` - Lấy danh sách ghi chú
- `POST /api/notes` - Tạo ghi chú mới
- `PUT /api/notes/{id}` - Cập nhật ghi chú
- `DELETE /api/notes/{id}` - Xóa ghi chú

### Ưu Tiên Hóa
- `POST /api/nextact/predict` - Dự đoán mức độ ưu tiên

## 📊 Mô Hình Machine Learning

Mô hình được huấn luyện trên 2000 mẫu ghi chú đa dạng tiếng Việt để dự đoán mức độ ưu tiên của công việc.

## Bản quyền và thông tin liên hệ
Nguyễn Đào Phúc Nguyên
nguyendaophucnguyen13@gmail.com