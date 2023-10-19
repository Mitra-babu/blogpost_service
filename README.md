<p style="text-align: center;">Blog Post service code</p>
Welcome to the Blog post service code. This file content set up guide and overall overview of service code.

**Tech Stack**
+ Python 3.8+
+ PostgreSQL

**Set up guide**
 + Create an virtual environment/ conda environment.
    ```console
    conda create -n myenv python=3.8
    ```
 + Activate the environemnt
    ```console
    conda actiavte myenv
    ```
 + Clone the repo in your project location
    ```console
   git clone https://github.com/TMGA-WAY/blogpost_service.git
    ```
 + Open the project in Pycharm or any other IDE.
 + Go to root location of project and execute the command below
    ```console
   pip install -r requirements.txt
    ```
 + Start the server
    ```console
   uvicorn main:app --reload
    ```