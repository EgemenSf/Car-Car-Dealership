# CarCar

Carcar is an application that was created to track an automobile company's inventory, vehicle service, and vehicle sales.

Team:

* Steven Ericksen - Automobile Sales Microservice
* Egemen SARI - Automobile Service Microservice

## Getting Started
​
**Make sure you have Git, Docker, and Node.js 18.2 or above**

1. Fork and clone this repository onto your local computer:
git clone https://gitlab.com/ege4822138/project-beta

2. Build and run the this project using Docker with these commands:
```

docker volume create beta-data
docker-compose build
docker-compose up
```
- After building and running these Docker commands, check all of your Docker containers are running

- Open the application in your browser:
http://localhost:3000/

## Design

CarCar is comprised of three microservices that interact with eachother.

- **Inventory**
    - Automobiles
    - Manufacturers
    - Vehicle models
- **Services**
    - Technician
    - Appointment
    - AutomobileVO
- **Sales**
    - Customer
    - Salespeople
    - Sale
    - AutomobileVO

![Img] (/images/diagram.png)


## Accessing Endpoints to Send and View Data: Access Through Insomnia & Your Browser

### Manufacturers:

| Action | Method | URL
| ----------- | ----------- | ----------- |
| List manufacturers | GET | http://localhost:8100/api/manufacturers/
| Create a manufacturer | POST | http://localhost:8100/api/manufacturers/ |
| Get a specific manufacturer | GET | http://localhost:8100/api/manufacturers/id/
| Update a specific manufacturer | PUT | http://localhost:8100/api/manufacturers/id/
| Delete a specific manufacturer | DELETE | http://localhost:8100/api/manufacturers/id/

JSON body to send data:
​
Create and Update a manufacturer (SEND THIS JSON BODY):
- You cannot create manufacturers with the same name. Name property is unique.

```
{
  "name": "Ford"
}
```


The return value of creating, viewing, updating a single manufacturer:
```
{
	"href": "/api/manufacturers/1/",
	"id": 1,
	"name": "Ford"
}
```

Getting a list of manufacturers return value:
```
{
  "manufacturers": [
    {
      "href": "/api/manufacturers/2/",
      "id": 2,
      "name": "Chevrolet"
    }
  ]
}
```

### Automobiles:
- The **'vin'** that is a unique value at the end of the detail urls represents the VIN for the specific automobile you want to access. This is not an integer ID. This is a string value so you can use numbers and/or letters.
​
| Action | Method | URL
| ----------- | ----------- | ----------- |
| List automobiles | GET | http://localhost:8100/api/automobiles/
| Create an automobile | POST | http://localhost:8100/api/automobiles/
| Get a specific automobile | GET | http://localhost:8100/api/automobiles/vin/
| Update a specific automobile | PUT | http://localhost:8100/api/automobiles/vin/
| Delete a specific automobile | DELETE | http://localhost:8100/api/automobiles/vin/


Create an automobile (SEND THIS JSON BODY):
- You cannot make two automobiles with the same vin. Vin is unique property.
```
{
  "color": "blue",
  "year": 2020,
  "vin": "1C3CC5FB2AN120236",
  "model_id": 2
}
```

Return Value of Creating an Automobile:
```
{
	"href": "/api/automobiles/1C3CC5FB2AN120236/",
	"id": 2,
	"color": "blue",
	"year": 2020,
	"vin": "1C3CC5FB2AN120236",
	"model": {
		"href": "/api/models/1/",
		"id": 1,
		"name": "Corvette",
		"picture_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWR-OIKro73LuOX_FXfcoiou6ny5qOy7J4xwgla2mODwuk7zhckzKhS7nnRVBEgDWyKLs&usqp=CAU",
		"manufacturer": {
			"href": "/api/manufacturers/2/",
			"id": 2,
			"name": "Chevrolet"
		}
	}
}
```

To access the details of a specific automobile, you can query by its VIN:
example url: http://localhost:8100/api/automobiles/1C3CC5FB2AN120236/
​
Return Value:
```
{
  "href": "/api/automobiles/1C3CC5FB2AN120236/",
  "id": 2,
  "color": "blue",
  "year": 2020,
  "vin": "1C3CC5FB2AN120236",
  "model": {
    "href": "/api/models/1/",
    "id": 1,
    "name": "Corvette",
    "picture_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWR-OIKro73LuOX_FXfcoiou6ny5qOy7J4xwgla2mODwuk7zhckzKhS7nnRVBEgDWyKLs&usqp=CAU",
    "manufacturer": {
      "href": "/api/manufacturers/2/",
      "id": 2,
      "name": "Chevrolet"
    }
  }
}
```

You can update the color and/or year of an automobile (SEND THIS JSON BODY):
```
{
  "color": "red",
  "year": 2012
}
```

Getting a list of Automobile Return Value:
```
{
  "autos": [
    {
      "href": "/api/automobiles/1C3CC5FB2AN120174/",
      "id": 2,
      "color": "red",
      "year": 2012,
      "vin": "1C3CC5FB2AN120236",
      "model": {
        "href": "/api/models/1/",
        "id": 1,
        "name": "Corvette",
        "picture_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWR-OIKro73LuOX_FXfcoiou6ny5qOy7J4xwgla2mODwuk7zhckzKhS7nnRVBEgDWyKLs&usqp=CAU",
        "manufacturer": {
          "href": "/api/manufacturers/2/",
          "id": 2,
          "name": "Chevrolet"
        }
      }
    }
  ]
}
```


## Vehicle Models:

In Insomnia you can load these to interact with the vehicle models.


List Vehicle Models | GET | http://localhost:8100/api/models/
 - Will list data as follows:
 {
	"models": [
		{
			"href": "/api/models/1/",
			"id": 1,
			"name": "Sebring",
			"picture_url": "your image url here",
			"manufacturer": {
				"href": "/api/manufacturers/1/",
				"id": 1,
				"name": "Chrysler"
			}
		}
    ]
 }

Create a vehicle model | POST | http://localhost:8100/api/models/
 - To create a model you'll send this JSON body:
 {
  "name": "Sebring",
  "picture_url": "your image url here",
  "manufacturer_id": 1
 }

Get a specific vehicle model | GET | http://localhost:8100/api/models/id/
 - Will list data as follows:
 {
	"href": "/api/models/1/",
	"id": 1,
	"name": "Sebring",
	"picture_url": "your image url here",
	"manufacturer": {
		"href": "/api/manufacturers/1/",
		"id": 1,
		"name": "Chrysler"
	}
 }

Update a specific vechile model | PUT | http://localhost:8100/api/models/id/
 - Updating a model takes upto two pieces, name and picture_url and is put in a JSON body like below:
 {
  "name": "Sebring",
  "picture_url": "your image url here"
 }

Delete a specific vehicle model | DELETE | http://localhost:8100/api/models/id/
 - Make sure you've selected the correct vehicle model to delete and it's gone.

## Service microservice

On the backend, the service microservice has 3 models: Technician, Appointment, and AutomobileVO. An Appointment model containing technician field. The technician field should be a foreign key. Your vin field should be of type CharField. (It should not be a AutomobileVO foreign key.)
​
The AutomobileVO is a value object that gets data about the automobiles in the inventory using a poller. The service poller automotically polls the inventory microservice for data, so the service microservice is constantly getting the updated data.
​
The reason for integration between these two microservices is that when recording a new service, you'll need to see which custumer is being VIP by checking their VIN number of car and that information lives inside of the inventory microservice.

## Accessing Endpoints to Send and View Data - Access through Insomnia:

### Technician:


| Action | Method | URL
| ----------- | ----------- | ----------- |
| List technicians | GET | http://localhost:8080/api/technicians/
| Create a technician | POST | http://localhost:8080/api/technicians/
| Show a specific technician | GET | http://localhost:8080/api/technicians/id/

To create a Technician (SEND THIS JSON BODY):
```
{
	"first_name": "Harve",
	"last_name": "Cums",
	"employee_id": "HarCums"
}
```

Return Value of Creating a Technician:
```
{
	"href": "/api/technicians/1/",
	"id": 1,
	"first_name": "Harve",
	"last_name": "Cums",
	"employee_id": "HarCums"
}
```

Return value of Listing all Technicians:
```
{
	"technicians": [
		{
			"href": "/api/technicians/1/",
			"id": 1,
			"first_name": "Harve",
			"last_name": "Cums",
			"employee_id": "HarCums"
		},
		{
			"href": "/api/technicians/2/",
			"id": 2,
			"first_name": "Terry",
			"last_name": "Simon",
			"employee_id": "TerrySimon"
		}
	]
}
```

### Appointment:

- The **'id'** that is a unique value at the end of the detail urls represents the ID for the specific appointment you want to access.

| Action | Method | URL
| ----------- | ----------- | ----------- |
| List appointments | GET | http://localhost:8080/api/appointments/
| Create an appointment | POST | http://localhost:8080/api/appointments/
| Update the STATUS of a specific appointment AS FINISHED | PUT | http://localhost:8080/api/appointments/id/finish/
| Update the STATUS of a specific automobile AS CANCELED| PUT | http://localhost:8080/api/appointments/id/cancel/
| Delete a specific appointment | DELETE | http://localhost:8080/api/appointments/id/


To create a Appointment (SEND THIS JSON BODY):

```
{
	"date_time": "2024-01-24 15:30:00",
	"reason": "Paint",
	"status": "created",
	"vin": "1C3CC5FB2AN120236",
	"customer": "Handy Somen",
	"technician": 1
}
```

Return Value of Creating a Appointment:
```
{

    "href": "/api/appointments/1/",
	"id": 1,
	"vin": "1C3CC5FB2AN120236",
	"status": "created",
	"reason": "Paint",
	"technician": {
		"href": "/api/technicians/1/",
	    "id": 1,
	    "first_name": "Harve",
	    "last_name": "Cums",
	    "employee_id": "HarCums"
	}

}
```

Return value of Listing all Appointments:
```
{
	"appointments": [
		{
			"href": "/api/appointments/2/",
			"id": 2,
			"vin": "1C3CC5FB2AN120176",
			"status": "canceled",
			"date_time": "2023-12-10T10:30:00+00:00",
			"technician": {
				"href": "/api/technicians/2/",
				"id": 2,
				"first_name": "Tommy",
				"last_name": "Hazar",
				"employee_id": "229574"
			},
			"customer": "Deny Ma",
			"reason": "Oil Change"
		},
		{
			"href": "/api/appointments/6/",
			"id": 6,
			"vin": "1C3CC5FB2AN120236",
			"status": "finished",
			"date_time": "2024-01-24T15:30:00+00:00",
			"technician": {
				"href": "/api/technicians/12/",
				"id": 12,
				"first_name": "Laris",
				"last_name": "Nikol",
				"employee_id": "LarisNikol"
			},
			"customer": "Handy Somen",
			"reason": "Paint"
		}
	]
}
```

Return Value of Canceled a Appointment:
```
{

	"href": "/api/appointments/6/",
	"id": 6,
	"vin": "1C3CC5FB2AN120236",
	"status": "canceled",
	"reason": "Paint",
	"technician": {
		"href": "/api/technicians/12/",
		"id": 12,
		"first_name": "Laris",
		"last_name": "Nikol",
		"employee_id": "LarisNikol"
	}
}
```

Return Value of Finished a Appointment:
```
{

	"href": "/api/appointments/6/",
	"id": 6,
	"vin": "1C3CC5FB2AN120236",
	"status": "finished",
	"reason": "Paint",
	"technician": {
		"href": "/api/technicians/12/",
		"id": 12,
		"first_name": "Laris",
		"last_name": "Nikol",
		"employee_id": "LarisNikol"
	}
}
```



## Sales microservice

This microservice has four models, AutomobileVO, Salesperson, Customer, and Sale. The Sale model has ForeignKeys connecting it to the other three models.
    AutomobileVO: a value object that gets data from the Automobile model in the Inventory microservice. It gets this data from a poller. This function happens automatically and provides updated data to the Sale model. The purpose for this interaction is so the user that is recording a sale pulls the vehicle from the inventory that isn't sold.

### Customers:

List a customer | GET | http://localhost:8090/api/customers/
 - Will display data as follows:
 {
	"customers": [
		{
			"first_name": "Joe",
			"last_name": "Customer",
			"address": "123 Main St\nDenver CO 80010",
			"phone_number": "123-456-7890",
			"id": 3
		}
    ]
 }

Create a customer | POST | http://localhost:8090/api/customers/
 - Creating a customer needs JSON body sent like below:
 {
    "first_name": "John",
    "last_name": "Doe",
    "address": "123 Main St",
    "phone_number": "123-456-7890"
 }

Show a specific customer | GET | http://localhost:8090/api/customers/id/
 - Specific customer data is returned as follows:
 {
    "first_name": "Joe",
    "last_name": "Customer",
    "address": "123 Main St\nDenver CO 80010",
    "phone_number": "123-456-7890",
    "id": 3
 }

### Salespeople:

List salespeople | GET | http://localhost:8090/api/salespeople/
 - Will display data as follows:
 {
	"salespeople": [
		{
			"first_name": "Bob",
			"last_name": "Evans",
			"employee_id": "BE1",
			"id": 9
		}
    ]
 }

Salesperson details | GET | http://localhost:8090/api/salespeople/id/
 - Will display data as follows:
 {
	"first_name": "Bob",
	"last_name": "Evans",
	"employee_id": "BE1",
	"id": 9
 }

Create a salesperson | POST | http://localhost:8090/api/salespeople/
 - Takes data in a JSON body as follows:
 {
    "first_name": "John",
    "last_name": "Wayne",
    "employee_id": "001"
 }

Delete a salesperson | DELETE | http://localhost:8090/api/salespeople/id/
 - Will delete the specific salesperson

### Sales

List sales | GET | http://localhost:8090/api/sales/
 - will return data as follows:
 {
	"sales": [
		{
			"automobile": {
				"vin": "1C3CC5FB2AN120174",
				"sold": false,
				"id": 5
			},
			"salesperson": {
				"first_name": "Bob",
				"last_name": "Evans",
				"employee_id": "BE1",
				"id": 9
			},
			"customer": {
				"first_name": "Joe",
				"last_name": "Customer",
				"address": "123 Main St\nDenver CO 80010",
				"phone_number": "123-456-7890",
				"id": 3
			},
			"price": 5000.0
		}
    ]
 }

Create a new sale | POST | http://localhost:8090/api/sales/
 - Requires the following in JSON body:
