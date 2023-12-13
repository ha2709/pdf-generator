# Flask Redis PDF Generator

This is a simple Flask application that demonstrates generating PDFs, storing links in a Redis queue, and associating each link with a UUID. The generated PDF links are then emitted to the front end in real-time using Flask-SocketIO.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Asynchronous PDF generation using RQ.
- Real-time status check and download functionality.
- Simple API for submitting PDF generation requests.

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


**In terminal run :**

curl --location 'localhost:5000/generate_pdf' \
--header 'Content-Type: application/json' \
--data '{
    "pdf_data":"1234",
    "user_id":"abcd"
}'


## Usage: 

1. **Submit PDF Generation Request:**

Use the `/generate_pdf` endpoint to submit a PDF generation request. The endpoint expects a JSON payload with the pdf_data parameter.

Example:

`curl -X POST -H "Content-Type: application/json" -d '{"pdf_data": "PDF Data"}' http://127.0.0.1:5000/generate_pdf`
 
The response will include a pdf_uuid that can be used to check the status and download the generated PDF.

2. **Check PDF Status:**

Use the /pdf-link/<pdf_uuid> endpoint to check the status of the generated PDF. The status will be either "pending" or "success."

Example:

`curl http://127.0.0.1:5000/pdf-link/PDF_UUID`

3. **Download PDF:**

Use the /download-pdf/<pdf_uuid> endpoint to download the generated PDF once the status is "success."

Example:

`curl -OJ http://127.0.0.1:5000/download-pdf/PDF_UUID`

# Endpoints

- /generate_pdf (POST): Submit a PDF generation request.
- /pdf-link/<pdf_uuid> (GET): Check the status of the generated PDF.
- /download-pdf/<pdf_uuid> (GET): Download the generated PDF.

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
