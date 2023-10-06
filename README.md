## TEST BACK END DEVELOPER

This is a project that implements a REST API with CRUD operations for the 'restaurants' table, along with basic statistical data retrieval capabilities.

### Documentation

To run the application from the container, follow these steps:

1. Build the Docker image:
   ```shell
   docker build -t api-restaurants .

2. Run a container:
    ```shell
    docker run -p 5000:5000 api-restaurants

### To call the endpoints.
3. Execute the **seed-data** of the endpoint and/or
   ```shell
   http://127.0.0.1:5000/restaurants/seed-data

4. (OPTIONAL) The endpoint **delete** all the restaurants as appropriate.
   ```shell
    http://127.0.0.1:5000/restaurants

5. Endpoints Dev and Prod

   - `GET` Documentation:
     ```shell
     http://127.0.0.1:5000/swagger-ui
     ```
     ```shell
     https://test-back-end-developer.onrender.com/swagger-ui
     ```
   
   - `GET` Request to fetch restaurants:
     ```shell
     http://127.0.0.1:5000/restaurants
     ```
     ```shell
     https://test-back-end-developer.onrender.com/restaurants
     ```

   - `POST` Request to add a new restaurant:
     ```shell
     http://127.0.0.1:5000/restaurants
     ```
     ```shell
     https://test-back-end-developer.onrender.com/restaurants
     ```

   - `PUT` Request to update a restaurant:
     ```shell
     http://127.0.0.1:5000/restaurants/<restaurant_id>
     ```
     ```shell
     https://test-back-end-developer.onrender.com/<restaurant_id>
     ```

   - `DELETE` Request to delete a restaurant:
     ```shell
     http://127.0.0.1:5000/restaurants/<restaurant_id>
     ```
      ```shell
     https://test-back-end-developer.onrender.com/<restaurant_id>
     ```

   - `STATISTICS` Request to get a statistics:
     ```shell
     http://127.0.0.1:5000/restaurants/statistics?latitude=<your_latitude>&longitude=<your_longitude>&radius=<your_radius>
     ```
     ```shell
     https://test-back-end-developer.onrender.com/restaurants/statistics?latitude=<your_latitude>&longitude=<your_longitude>&radius=<your_radius>
     ```
