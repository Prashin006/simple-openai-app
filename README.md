### Simple Chatbot Using OpenAI

- This repository contains code written in Python to work with OpenAI's API and creating a chatbot with various models like 'gpt-4o', 'gpt-3.5-turbo' etc. which runs on the terminal/command line.
- `image.py` file also shows how to generate images using the 'dall-e-3' model. We can also use the 'dall-e-2' model, but 'dall-e-3' model is the latest one at the time of experimenting with this API.
- To follow along with the code, make sure to:

1. Clone the repository to your local machine using `git clone https://github.com/Prashin006/simple-openai-app.git` command

2. Create a virtual environment (recommended) using the built-in `venv` module (requires Python 3.3.0 or above) by using the command `python -m venv {name_of_virtual_env}`

3. Activate the virtual environment using `{name_of_virtual_env}\Scripts\activate.bat` for Windows and `source {name_of_virtual_env}/bin/activate` for Linux/MacOS.

4. I have created the Virtual Environment using `Anaconda` (a Python distribution, specifically designed for scientific computing, data science, and machine learning applications) using the `conda create {name_of_virtual_env}` and activating it using `conda activate {name_of_virtual_env}`

5. Install the required modules/libraries from the `requirements.txt` file by running `pip install -r requirements.txt` on the terminal/command line.

6. Create a file named `.env` for storing the OpenAI API key (which you need to have an OpenAI account and create an API key) [OpenAI] (https://platform.openai.com) and paste the key as `OPENAI_API_KEY={your_openai_api_key}`.

7. Another way of setting up the API key is to create an environment variable on your system and save the API key as an environment variable.

8. Now you can execute all of the code from this repository!

9. To deactivate the virtual environment, run `deactivate` (for venv) on command line or `conda deactivate` (for anaconda).

**NOTE: To make sure you are able to understand the code, try running and experimenting with the code by yourself**

If you are facing issues using `pip` try using `pip3` instead. Same goes for `python`, try `python3`.
