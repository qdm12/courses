# Real time Big Data Analytics: Homework 4

## Twitter API
1. Create a [**Twitter**](https://twitter.com/) account first and log in to it.
2. Add a valid phone number to your account at [https://twitter.com/settings/add_phone](https://twitter.com/settings/add_phone).
2. Head to [https://apps.twitter.com/](https://apps.twitter.com/).
3. Click on **Create New App** at the center of the screen.
4. Fill out the form and click on **Create your Twitter application**.
5. Click on the **Keys and Access Tokens** tab.
6. Click on **Create my access token** at the bottom of the page.
7. Finally copy all the following values in the code (Python or Java):
    - Set **apiKey** equal to your *Consumer Key (API Key)*
    - Set **apiSecret** equal to your *Consumer Secret (API Secret)*
    - Set **accessToken** equal to your *Access Token*
    - Set **accessTokenSecret** equal to your *Access Token Secret*

## Python
1. Go to the *python* directory and install the required packages with:
   
   ```bash
   pip install -r requirements.txt
   ```
   
   or, for python 3:
   
   ```bash
   pip3 install -r requirements.txt
   ```
   
2. Add your credentials to the code as explained above.

3. Simply run the program, either in STREAM mode or in API search mode (see variable `mode`)

   ```bash
   python homework4.py
   ```