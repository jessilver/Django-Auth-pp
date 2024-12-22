# Django Auth App Project

Welcome to my Django Auth App project. This project is an Auth App that I can use in others projects

### Used Database: 

[Postgres](https://github.com/jessilver/Docker-DataBases/tree/main/Postgres)

## Features

- User registration
- User login
- Password reset
- Email verification

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/jessilver/Django-Auth-pp.git
    ```
2. Create venv:

    ```sh
    cd Django-Auth-pp
    ```
    ```sh
    py -m venv venv
    ```
3. Install dependencies: 

    ```sh
    cd venv/Scripts
    ```
    ```sh
    activate
    ```
    ```sh
    cd ../..
    ```
    ```sh
    pip install -r requirements.tx
    ```
4. Setup `settings.py`
5. Run migrations:

    ```sh
    py manage.py makemigrations
    ```
    ```sh
    py manage.py migrate
    ```
6. Start the development server:

    ```sh
    py manage.py runserver
    ```

## Usage

[Working - Coming Soon]

## Contributing

Feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License.