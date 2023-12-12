# Flask Redis PDF Generator

This is a simple Flask application that demonstrates generating PDFs, storing links in a Redis queue, and associating each link with a UUID. The generated PDF links are then emitted to the front end in real-time using Flask-SocketIO.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- PDF generation using Flask and Redis.
- Real-time updates to the front end using Flask-SocketIO.
- UUID association with each generated PDF link.
- Store and retrieve PDF links from a Redis queue.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ha2709/pdf-generator.git

2. **Navigate to the Project Directory:**

`cd pdf-generator`

3. **Create a Virtual Environment:**

`python -m venv venv`
 
4. **Activate the Virtual Environment:**

`source venv/bin/activate`

5. **Install Dependencies:**

``

6. **Run the Application:**

The application will be accessible at http://127.0.0.1:5000/.

## Usage: 

 **In terminal run :**

curl --location 'localhost:5000/generate_pdf' \
--header 'Content-Type: application/json' \
--data '{
    "pdf_data":"1234",
    "user_id":"abcd"
}'

 
# Running in Production

To run the application in production:

`gunicorn -w 4 -b 0.0.0.0:5000 app:app`

## Background Task Execution

To start executing enqueued function calls in the background, start a worker from project’s directory:

`rq worker --with-scheduler`

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. 
