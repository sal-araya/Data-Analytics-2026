/*
a) The actor table includes information about actors such actor_id, first_name, last_name, and last_update.
b) The film table includes information about movies such film_id, title, description, release_year, rental_rate, and other details about each film. 
c) The table that contains both actor_id and film_id is the film_actor table.
d) The rental table includes information about rentals such as rental_id, rental_date, inventory_id, customer_id, return_date, and staff_id. This information can be hard to read because it contains may IDs instead of descriptive names.
e) The inventory table includes information about copies of films, such as inventory_id, film_id, and store_id. It shows which films are available at each store.
f) To understand the name of all films rented on a specific date, you need rental, inventory, and film tables. The rental table shows when a film was rented, the inventory table connects rentals to specific films, and the film table contains the film names. These tables are related through inventory_id and film_id.
*/

SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;