# Digital Evidence Cataloging System (DECS)

DECS is a secure and role-based digital platform designed to manage, store, retrieve, and audit digital evidence in criminal investigations. The system ensures integrity, traceability, and ease of access to digital assets for various roles including Admins, Investigators, and Analysts.

## 🚀 Features

- 🔐 **Role-Based Access Control** (Admin, Investigator, Analyst)
- 📂 **Digital Evidence Upload** with metadata
- 🧾 **Hash Verification** for data integrity
- 🔍 **Advanced Search & Filtering** by case, date, etc.
- 🛡️ **Audit Trail** for all activities
- 📊 **Report Generation** (PDF/CSV)
- 🧠 **User-Friendly Interface** with HTML & Jinja2
- 🗂️ **MongoDB-based Storage** with secure handling

---

## 📌 Project Modules

### 👤 User Management
- Registration & Login
- Role-based dashboards

### 📁 Evidence Management
- Upload files with metadata
- File hashing for verification
- Categorize by case ID

### 🔎 Search & View
- Keyword, date range, case-based search
- Role-based access to evidence

### 🧾 Audit Logs
- Tracks all activities
- Ensures chain of custody

---

## 🛠️ Tech Stack

| Layer       | Technology                    |
|-------------|-------------------------------|
| Frontend    | HTML, CSS, Bootstrap, Jinja2  |
| Backend     | Flask (Python)                |
| Database    | MongoDB                       |
| Auth        | Flask-Login, Role-based auth  |
| Versioning  | Git & GitHub                  |

---

## 🖥️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/AjayJoshi99/decs.git
   cd decs
2. **Run the app**
  ```bash
  python main.py
```

**🤝 Contributors**
Ajay Joshi

**📬 Contact**
For queries or contributions, reach out at:  
📧 ajay.joshi1908@gmail.com
