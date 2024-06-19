# Todo-Backend

## Description

This project is a backend implementation of a todo application. It provides a RESTful API for managing todo items. The frontend is being built in react. You can try and build a frontend for this yourself. Just try not to overload the server and the database.

## Features

- Create, read, update, and delete todo items
- Mark todo items as completed
- Filter and sort todo items
- User authentication and authorization

## Technologies Used

- Django REST Framework (DRF)
- PostgreSQL

## Installation

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Set up the database connection in the configuration file.
4. Apply the database migrations using `python manage.py migrate`.
5. Start the server using `python manage.py runserver`.

## Try The endpoints?

**You can try the Api Endpoints Through :**

- [Swagger Ui](https://todo.gaurav.rocks/swagger-ui)
- [Redoc](https://todo.gaurav.rocks/redoc)
- [Normal OpenAPI Schema](https://todo.gaurav.rocks/schema)

## API Endpoints

| **Path**                   | **Method** | **Operation ID**                | **Request Body Schema** | **Security**                                      | **Response Codes** |
| -------------------------- | ---------- | ------------------------------- | ----------------------- | ------------------------------------------------- | ------------------ |
| `/accounts/register/`      | `POST`     | `accounts_register_create`      | `Register`              | `jwtAuth`, `cookieAuth`, `basicAuth`              | `201`              |
| `/accounts/token/`         | `POST`     | `accounts_token_create`         | `GetJWTToken`           | `jwtAuth`, `cookieAuth`, `basicAuth`              | `200`              |
| `/accounts/token/refresh/` | `POST`     | `accounts_token_refresh_create` | `TokenRefresh`          | None                                              | `200`              |
| `/accounts/user/`          | `GET`      | `accounts_user_retrieve`        | None                    | `jwtAuth`, `cookieAuth`, `basicAuth`              | `200`              |
| `/accounts/user/`          | `PUT`      | `accounts_user_update`          | `Account`               | `jwtAuth`, `cookieAuth`, `basicAuth`              | `200`              |
| `/accounts/user/`          | `PATCH`    | `accounts_user_partial_update`  | `PatchedAccount`        | `jwtAuth`, `cookieAuth`, `basicAuth`              | `200`              |
| `/schema/`                 | `GET`      | `schema_retrieve`               | None                    | `jwtAuth`, `cookieAuth`, `basicAuth`, `basicAuth` | `200`              |
| `/todo/`                   | `GET`      | `todo_list`                     | None                    | `jwtAuth`                                         | `200`              |
| `/todo/`                   | `POST`     | `todo_create`                   | `Todo`                  | `jwtAuth`                                         | `201`              |
| `/todo/{id}/`              | `GET`      | `todo_retrieve`                 | None                    | `jwtAuth`                                         | `200`              |
| `/todo/{id}/`              | `PUT`      | `todo_update`                   | `Todo`                  | `jwtAuth`                                         | `200`              |
| `/todo/{id}/`              | `PATCH`    | `todo_partial_update`           | `PatchedTodo`           | `jwtAuth`                                         | `200`              |
| `/todo/{id}/`              | `DELETE`   | `todo_destroy`                  | None                    | `jwtAuth`                                         | `204`              |
| `/todo/{id}/complete/`     | `POST`     | `todo_complete_create`          | `Todo`                  | `jwtAuth`                                         | `200`              |

## Components Schemas

| **Schema Name**  | **Type** | **Description**                                      |
| ---------------- | -------- | ---------------------------------------------------- |
| `Account`        | `object` | User account details including username, email, etc. |
| `GetJWTToken`    | `object` | Credentials for obtaining a JWT token.               |
| `PatchedAccount` | `object` | Partial update schema for user account.              |
| `Register`       | `object` | User registration schema.                            |
| `Todo`           | `object` | To-do item details.                                  |
| `TokenRefresh`   | `object` | Refresh token details.                               |

## Security Schemes

| **Scheme Name** | **Type** | **Scheme**  | **Description**                  |
| --------------- | -------- | ----------- | -------------------------------- |
| `basicAuth`     | `http`   | `basic`     | Basic authentication.            |
| `cookieAuth`    | `apiKey` | `sessionid` | Cookie-based authentication.     |
| `jwtAuth`       | `http`   | `bearer`    | JWT Bearer token authentication. |

## Contributing

Contributions are welcome! Submit a PR as Normal if you want to expand on this further.

## License

This project is licensed under the [MIT License](/LICENSE).
