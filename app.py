from flask import Flask, request
import movieCrawling
import json
import movieCrawling


app = Flask(__name__)
@app.route("/genre", methods=['GET','POST'])
def genre():
    genre = request.form["genre"]
    mv = movieCrawling.MovieCrawling()
    
    return json.dumps(mv.save_Image(genre))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5050", debug=True)
