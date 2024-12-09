# TidyTasks
TidyTasks is a simple and functional Todo app built using Django. This is my first Django project, which I developed to learn the basics of web development with Django. The app allows users to create, update, and delete tasks, providing a clean interface for managing daily activities and keeping track of important to-dos.

![image](https://github.com/user-attachments/assets/6f997dc5-b735-4df8-bed6-faac0cd67628)
### Features
- **User Authentication**: Allows users to register, log in, and manage their personal tasks.
- **Task Management**: Users can create, update, and delete tasks easily.
- **Task Status**: Mark tasks as complete or pending.
- **Database Integration**: All tasks are stored in a database for persistence.

### Technologies Used
- **Backend**: Django (Python)
- **Database**: SQLite (used by default in Django)
- **Frontend**: HTML, CSS

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/brahma-borude/TidyTasks.git
   ```

2. Navigate to the project directory:
   ```bash
   cd TidyTasks
   ```

3. Set up a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows: `.\venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Run the server:
   ```bash
   python manage.py runserver
   ```

7. Visit the app at `http://127.0.0.1:8000/` in your browser.
