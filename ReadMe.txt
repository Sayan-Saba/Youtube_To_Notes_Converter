create a python environment inside the directory containing the above both files (app.py and requirements.txt) using vscode terminal command: virtualenv venv
You need the virtualenv package to create a virtual environment. You can install it using pip if it’s not already installed: pip install virtualenv
acitvate the environment using the command: venv\Scripts\activate
add the .env file containing your api key in the format : GOOGLE_API_KEY='Your API key'
install the necessary lbrarires mentioned in the requirements.txt using the command: pip install -r requirements.txt
now run the code
finally in the terminal run the app.py using the command: streamlit run app.py
