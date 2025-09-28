# Well-being Check

A web application designed to collect well-being data from university students, aiming to help create a safer and more prosperous campus environment.

---

## 🚀 Demo & Certificate

- **Prototype Video Demo:** [Watch on YouTube](https://www.youtube.com/watch?v=wKnEj-UnVUo)
- **CS50 Certificate:** [View Certificate](https://certificates.cs50.io/46b6d8b5-1ce1-4121-8f30-b2060cd3acd1.pdf?size=letter)

---

## 📝 Description

This project is inspired by a CS50 final project prompt: *What will my software do? What features will it have? How will it be executed?*

**Well-being Check** is a website that gathers data from university students to help administrators and faculty make data-driven decisions, plan events, and improve the overall educational environment. The site leverages the Django web framework and integrates survey functionality to collect and analyze responses.

### Key Features

- Survey system for collecting student well-being data.
- Login system using Google OAuth 2.0 (only selected individuals/university accounts can access).
- Data analysis and visualization (potential for analytics dashboard).
- Modular Django app structure for scalability.
- Static files for images and assets.
- Extensible for event and activity management.

### Technologies Used

- **Django** (Python web framework)
- [django-form-surveys](https://github.com/irfanpule/django-form-surveys) for customizable survey forms
- **Google OAuth 2.0** for authentication
- **HTML/CSS** for frontend templates
- **SQLite3** (local development database, not included for privacy)

---

## 🗂️ Project Structure

- `cvsu_mh/` - Main Django project (admin settings, configuration)
- `accounts/` - Custom user accounts and authentication logic
- `survey/` - Survey app for well-being questionnaires
- `users/` - User data and profile management
- `static/` - Static assets such as images
- `templates/` - HTML templates for rendering views
- `staticfiles/` - Collected static files (from Django and third-party apps)

> **Note:** The database file (`db.sqlite3`) is not included in the repository for privacy reasons.

---

## 🔐 Authentication

- Only university students/faculty (via Google account) can log in and participate.
- Utilizes `django-allauth` for easy integration with Google OAuth.
- After login, users are redirected to the survey page.

---

## 💡 Development Journey

Learning and implementing Django was both challenging and rewarding. From figuring out secure authentication (Google OAuth) to integrating third-party Django apps for surveys, this project was a hands-on experience in modern web development. AI tools and documentation were invaluable for troubleshooting and understanding new concepts.

---

## 🏁 Outcomes

- **Good Outcome:** Secure login, minimal CSS, working survey for selected users.
- **Better Outcome:** Improved CSS, analytics dashboard handling large data (20k+ records).
- **Best Outcome:** Always-live deployment, instant feedback/advice, chat support, rich data analysis, user profiles, school event feeds.

The current submission achieves the "good outcome" milestone. Future enhancements can aim for the "better" and "best" outcomes.

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Aj-z/cvsu_mh.git
   cd cvsu_mh
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables (add your Django secret key and Google OAuth credentials).
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```

---

## 📚 References

- [Django Documentation](https://docs.djangoproject.com/)
- [django-form-surveys](https://github.com/irfanpule/django-form-surveys)
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/)

---

## 🙏 Acknowledgments

- CS50 Team 
- The open-source Django community
- AI and documentation resources for troubleshooting

---

*For questions or contributions, feel free to open an issue or pull request!*
