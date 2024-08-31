Create a Python environment to install the dependencies: python -m venv myenv

You need the virtualenv package to create a virtual environment. You can install it using pip if it’s not already installed: pip install virtualenv

Activate the environment using the command: myenv\Scripts\activate

Add the .env file containing your API key in the format: GOOGLE_API_KEY='Your API key'

Install the necessary libraries mentioned in the requirements.txt using the command: pip install -r requirements.txt

Finally in the terminal run the app.py using the command: streamlit run app.py
