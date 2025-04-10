# FIT5120TA19

System Components
User
The end-user(parents) interacts with the system via a web-based interface. Users can search historical drowning statistics and retrieve real-time beach condition updates.

User Interface (Frontend)
The front-end component of the WaterWiseFamily website where users access system features and submit requests. It forwards inputs to the backend for processing and displays the returned results.

Backend Service (Flask)
The core logic layer is built using Flask, a lightweight Python web framework. It manages communication between the UI, the database, the AI model, and external APIs. Flask processes user requests, coordinates data retrieval or analysis, and returns structured responses to the frontend.

Google Cloud PostgreSQL Database
Stores and manages structured public datasets, such as historical drowning statistics. It supports backend queries by providing accurate, relevant data for analysis and insight generation.

External Wrangled Data Sources
Pre-processed public datasets are imported into the PostgreSQL database. These sources enrich the system's analytical capabilities and enhance the accuracy of its safety on beach insights.

External API Connections
External APIs provide real-time environmental data, including beach conditions, tides, and weather updates. The Flask backend sends requests to these APIs and relays the information to the UI, enabling informed user decisions.

AI Model
An optional module that analyzes and predicts rip current levels or water safety risks based on user-uploaded photos. It processes image inputs and returns intelligent insights to support decision-making.

GitHub
Hosts the source code repository, enabling version control, continuous development, and streamlined deployment. Supports collaborative coding and ensures system reliability and maintainability.

Deployment Service (Netlify)
The frontend is hosted on Netlify, a modern cloud-based deployment platform. Netlify enables continuous integration and deployment from the GitHub repository, automatically building and publishing frontend updates with minimal effort.

Project Structure Overview
vue-project/
│── backend/  <-- All backend-related code files which was created manually.
│   ├── app.py  <-- Main Flask file to define API routes.
│   ├── database.py  <-- To handle the remote PostgreSQL connection.
│   ├── .env  <-- Store DB credentials securely.
│   ├── requirements.txt  <-- Required dependencies and libraries for deployment
│── dist/  <-- The final production build output of your Vue project. It is automatically generated when you run npm run build. This folder contains optimized, minified HTML, CSS, JS, and static assets ready to be deployed to a web server. You should not edit files in dist/, and it's typically excluded from version control (.gitignore).
│── node_modules  <-- Stores all the packages (dependencies) your project needs to run
│── public  <-- Stores the index.html file (the main HTML entry point) and static assets like images, icons, or fonts. Files placed here are copied directly into the final build without processing and are accessible via absolute URLs (e.g., /logo.png).
│── src/  <-- The main folder where you write your Vue application logic, styles, and components.
│   ├── assets  <-- Stores static files that need to be processed by the build system, like images and logos.
│   ├── components  <-- Contains the main Vue components and function codes.
│   ├── router  <-- Holds the Vue Router configuration, typically in a file like index.js. It defines all the app's routes (pages or views).
│── App.vue <-- The root component where the main layout and structure of your app are defined. 
│── main.js  <-- The entry point, where the Vue app is initialized and the root component (App.vue) is mounted to the DOM. This is also where global configurations like Vue Router are registered.
****
Frontend page is now html file. 
Open the Homepage.html to start the project!
