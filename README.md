# Medicalchatbot
STEPS:
Clone the repository
Project repo: https://github.com/
STEP 01- Create a conda environment after opening the repository
conda create -n medicalchatbot python=3.8 -y | python -m venv env
conda activate medicalchatbot | .\env\Scripts\activate.bat
STEP 02- Install the requirements
pip install -r requirements.txt
After Creating Files use the following commands
git add .
git commit -m " folder structure added"
git push origin main

Create a .env file in the root directory and add your Pinecone credentials as follows:
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
Download the quantize model from the link provided in model folder & keep the model in the model directory:

# run the following command
python store_index.py
# Finally run the following command
python app.py

