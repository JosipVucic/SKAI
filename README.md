# SKAI

This is a repository reserved for task solutions for the SKAI_LABS job application.  

## Tasks
All tasks can be accessed from the homepage as well as the navigation bar.  

### Task 1 
The task involved drawing a polygon on a map and displaying it to the user in a interactive fashion with drag and zoom capabilities.  
  
#### Map Logic
- Location: `task1/static/task1/js/map.js`

#### HTML Template
- Location: `task1/templates/task1/home.html`
  
### Task 2 
The task involved setting up an API endpoint for detecting unauthorized sales.  
  
Input example:  
```bash
{
  "productListings": [{"productID": "123", "authorizedSellerID": "A1"}],
  "salesTransactions": [{"productID": "123", "sellerID": "B2"}]
}
```
Output example:  
```bash
{
  "unauthorizedSales": [
    {"productID": "123", "unauthorizedSellerID": ["B2"]}
  ]
}
```
  
#### API Logic
- Location: `task2/views.py`

#### HTML Template
- Location: `task2/templates/task2/home.html`
  
### Task 3 
The task involved setting up an API endpoint that determines the maximum number of interviews that can be scheduled without overlap.  
  
Input example:
```bash
{
  "start_times": [10, 20, 30, 40, 50, 60],
  "end_times": [15, 25, 35, 45, 55, 65]
}
```
Output example:
```bash
{
  "max_interviews : 6
}
```
  
#### API Logic
- Location: `task3/views.py`

#### HTML Template
- Location: `task3/templates/task3/home.html`

## Running with Docker
To run the project with Docker, navigate to the 'SKAI' folder (the folder containing the Dockerfile) and execute the following commands:
```bash
docker build -t skai .
docker run -d --name skai-container -p 8000:8000 skai
```
The app should now be running, and you can access it at http://localhost:8000 in your web browser.

## Running with Django
Before running the app install dependencies using pip:  
```bash
pip install -r requirements.txt
```
To run the app using Django, navigate to the 'config' folder (the folder containing manage.py) and execute the following command:
```bash
python manage.py runserver
```
Make sure you have all the required dependencies listed in requirements.txt installed in your environment, otherwise, the app may not work properly.
