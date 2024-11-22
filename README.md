# Simple Checkout System (AGRICHAIN Assignment)

## How To Run
  
  - clone this repository

    ```bash
    $ git clone https://github.com/moinologics/checkout-system
    $ cd checkout-system
    ```

  - Non Docker Method

    - Requirements
      - python v3 should be installed on your machine
    
    - install the required packages (only required when using external packages)
      ```bash
      $ python -m pip install -r requirements.txt
      ```

    - Run Checkout System
      ```bash
      $ python checkout.py
      ```
    
    - Run Unit Tests
      ```bash
      $ python test_checkout.py
      ```

  - Docker Method

    - Requirements
      - Docker should be installed on your system
    
    - Build Docker Image
      ```bash
      $ docker build -t agrichain .
      ```
    
    - Run Checkout System
      ```bash
      $ docker run --rm -it agrichain
      ```
    
    - Run Unit Tests
      ```bash
      $ docker run --rm agrichain test_checkout.py
      ```