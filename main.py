from flask import Flask, render_template
import utils
path = 'candidates.json'

app = Flask(__name__)

@app.route('/')
def index():
    candidates = utils.load_candidates_from_json(path)
    return render_template('list.html', candidates=candidates)


if __name__ == '__main__':
    app.run(debug=True)


