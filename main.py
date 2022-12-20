from flask import Flask, render_template, request
import utils
from jinja2 import Template
from utils import load_candidates_from_json, get_candidates_by_name
path = 'candidates.json'

app = Flask(__name__)


@app.route("/")
def index():
    candidates = load_candidates_from_json(path)
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:pk>')
def candidate_page(pk):
    candidate = utils.get_candidate(pk)
    return render_template('card.html', candidate=candidate)


@app.route('/search/<name>')
def find_name(name):
    candidates = get_candidates_by_name(name)
    return render_template('search.html', candidates=candidates, count_candidates=len(candidates))


@app.route("/skill/<skill_name>")
def skill_search(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name.lower())
    return render_template('skill.html', candidates=candidates, count_candidates=len(candidates))


if __name__ == '__main__':
    app.run(debug=True)


