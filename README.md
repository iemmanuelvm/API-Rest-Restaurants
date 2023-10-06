## TEST BACK END DEVELOPER

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

5. Endpoints
   
   - `GET` Request to fetch restaurants:
     ```shell
     http://127.0.0.1:5000/restaurants
     ```

   - `POST` Request to add a new restaurant:
     ```shell
     http://127.0.0.1:5000/restaurants
     ```

   - `PUT` Request to update a restaurant:
     ```shell
     http://127.0.0.1:5000/restaurants/<restaurant_id>
     ```

   - `DELETE` Request to delete a restaurant:
     ```shell
     http://127.0.0.1:5000/restaurants/<restaurant_id>
     ```

   - `STATISTICS` Request to get a statistics:
     ```shell
     http://127.0.0.1:5000/restaurants/statistics?latitude=<your_latitude>&longitude=<your_longitude>&radius=<your_radius>
