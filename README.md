# 🤸🏽‍♀️fitHub

> A finance membership tracker.

fitHub is a full-stack web application designed to manage fitness club memberships, finances, and communications. It features role-based access control, real-time chat functionality, and comprehensive class scheduling.


## 📋 Table of Contents

- [Tech Stack](#-tech-stack)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [License](#-license)


## 🛠 Tech Stack

## Frontend (Client)
- **Framework:** [Next.js](https://nextjs.org/)
- **Styling:** Tailwind CSS, Autoprefixer, PostCSS
- **Components:** PrimeReact, React Icons, Hamburger React
- **Animations:** Framer Motion
- **Data Visualization:** React Chartjs 2
- **Calendar:** React Big Calendar
- **Utilities:** Moment.js, Classnames, React Use, React Hot Toast

## Backend (Server)
- **Framework:** [Django](https://www.djangoproject.com/)
- **API:** Django REST Framework
- **Real-time:** Django Channels, Daphne, Twisted
- **Database:** PostgreSQL (hosted via Supabase)
- **Authentication:** PyJWT (JSON Web Tokens)
- **Networking:** Requests, Urllib3, Autobahn





## ✨ Features

- **Role-Based Access Control:** Distinct functionality for Members, Coaches, and Treasurers.
- **Class Management:**
  - Coaches can create classes and view schedules.
  - Members can browse available classes and sign up.
- **Finance Tracking:**
  - Treasurers can track finance logs and coach salaries.
  - Automatic calculation of payment balances.
- **Member Logs:**
  - Tracking of member attendance and membership status approval.
  - Management of prepaid fees and payment status.
- **Message Platform:**
  - Real-time chat features using WebSockets.
  - Chat history retrieval and room management.
- **User Authentication:**
  - Secure registration, login, and logout using JWT cookies.
  - Password reset and profile management.





## 🚀 Getting Started

## Prerequisites
- Node.js (v18+)
- Python (v3.10+)
- PostgreSQL database

## Backend Setup (Server)

1. **Navigate to the server directory:**
   ```bash
   cd server


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```



3. **Run Migrations:**
```bash
python manage.py migrate

```


4. **Start the Server:**
```bash
python manage.py runserver

```



## Frontend Setup (Client)

1. **Navigate to the client directory:**
```bash
cd client

```


2. **Install dependencies:**
```bash
npm install

```



3. **Start the Development Server:**
```bash
npm run dev

```



4. **Access the App:**
Open [http://localhost:3000] in your browser.

## 🔐 Environment Variables

The project requires environment variables for database connections and security keys.

* **Server:** Create a `.env` file in the `server` directory. Refer to `.env.example`.
* **Client:** Ensure any necessary public API keys are configured in `.env.local` if applicable.

## 📄 License

This project is licensed under the MIT License.

**Copyright (c) 2026 RAJ**


