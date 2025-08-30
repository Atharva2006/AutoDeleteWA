# AutoDeleteWA

A Python script that automates the process of deleting WhatsApp messages using Playwright. This code helps in removing your own messages after some seconds for privacy freaks.

## Features

- Automates the deletion of WhatsApp messages.
- Built using Python and Playwright for browser automation.
- Simple script-based solution – no extra tools or complex setup required.

## Requirements

- Python 3.8 or later
- Patchright for asynchronous Playwright integration

## Installation

1.Clone the repository:

    git clone https://github.com/yourusername/AutoDeleteWA.git
    cd AutoDeleteWA

2.Create a virtual environment (optional but recommended):

    python3 -m venv venv
- on Linux,use

    source venv/bin/activate

- On Windows, use
         
    venv\Scripts\activate 

3.install patchright and chromium via

    pip install patchright
    patchright install chrome

## Usage

Run the script:
- In the terminal, execute the Python script:

    python auto_delete_wa.py


Modify conditions:
- You can edit the script to specify when and which messages to delete (e.g., by sender, content, or message time).

## License

- This code is licensed under the MIT License – see the LICENSE file for details.

    

  
   
