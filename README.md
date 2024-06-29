Grazioso Salvare Rescue Animal Dashboard
Overview
This project involves creating an interactive dashboard for Grazioso Salvare, an animal rescue organization. The dashboard connects to a MongoDB database to display and filter animal records based on specific rescue requirements. The project uses Dash, a Python framework for building analytical web applications.

Dashboard Functionality
The dashboard includes several interactive components:

Filtering Options: Users can filter animals based on specific rescue types such as Water Rescue, Mountain or Wilderness Rescue, and Disaster or Individual Tracking.
Interactive Data Table: Displays animal data from the MongoDB database and updates based on the selected filters.
Charts: Visual representations of the breed distribution of animals based on the current filter settings.
Map: Displays the location of the selected animal from the data table.
Tools and Technologies
Dash: For building the web application.
Plotly: For creating interactive charts.
Dash Leaflet: For displaying maps.
Pandas: For data manipulation and analysis.
MongoDB: Database to store animal records.
CRUD Python Module: Custom module for performing CRUD operations on MongoDB.
Project Structure
animal_shelter.py: Contains the CRUD operations for interacting with MongoDB.
app.py: Main application file that sets up the Dash layout and callbacks.
README.md: Documentation file.
Logo.png: Logo of Grazioso Salvare.
How to Run the Project
Ensure you have the necessary Python packages installed:

pip install dash dash-leaflet pandas plotly pymongo

Set up your MongoDB connection details in animal_shelter.py.
Run the Dash app:

python app.py

Open your web browser and navigate to http://127.0.0.1:8050/ to view the dashboard.
Reflection
Writing Maintainable, Readable, and Adaptable Code
Writing maintainable, readable, and adaptable code involves following best practices such as using meaningful variable names, modularizing code, and adding comments and documentation. In this project, the CRUD Python module from Project One facilitated a clean separation of database operations from the application logic. This modular approach made the code more maintainable and adaptable. In the future, this CRUD module can be reused for other projects requiring MongoDB operations, saving development time and ensuring consistency.

Approach to Problem-Solving
As a computer scientist, approaching problems involves breaking them down into manageable components, understanding the requirements, and using the right tools and technologies. For the Grazioso Salvare dashboard, the approach was to first understand the filtering and display requirements, then design the database schema, and finally implement the interactive components. Compared to previous assignments, this project required more integration between different technologies (Dash, MongoDB, Plotly). Future projects would benefit from this experience by applying similar integration strategies to meet client requirements effectively.

Role of Computer Scientists
Computer scientists solve complex problems by creating efficient algorithms, designing robust systems, and developing user-friendly applications. This project helps Grazioso Salvare streamline their rescue operations by providing an intuitive interface to access and filter animal data. Such tools are crucial for organizations to make informed decisions quickly and accurately, thereby improving their overall efficiency and effectiveness.
