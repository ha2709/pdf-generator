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
   git clone https://github.com/your-username/flask-redis-pdf-generator.git
