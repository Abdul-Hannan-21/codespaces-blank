from flask import Flask, render_template
import requests
import json
import random  # Import the random module

app = Flask(__name__)

def get_meme():
    url = "https://api.imgflip.com/get_memes"
    try:
        response = requests.get(url).json()
        memes = response["data"]["memes"]
        
        # Select a random meme from the list
        selected_meme = random.choice(memes) if memes else None

        if selected_meme:
            meme_url = selected_meme["url"]
            meme_name = selected_meme["name"]
            return meme_url, meme_name
        else:
            return None, None

    except (json.decoder.JSONDecodeError, KeyError) as e:
        print(f"Error retrieving meme: {e}")
        return None, None

@app.route('/')
def index():
    meme_url, meme_name = get_meme()
    
    if meme_url is not None and meme_name is not None:
        return render_template('meme_index.html', meme_url=meme_url, meme_name=meme_name)
    else:
        return "Error retrieving meme. Please try again later."

if __name__ == "__main__":
    app.run(debug=True, port=50003)
