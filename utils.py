import json


def load_candidates_from_json(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
        return data




def get_candidate(candidate_id):
    for candidate in load_candidates_from_json("candidates.json"):
        if candidate_id == candidate['id']:
            return candidate


def get_candidates_by_name(candidate_name):
    data = []
    for candidate in load_candidates_from_json("candidates.json"):
        if candidate_name. lower() == candidate['name'].lower():
            data.append(candidate)
    return data


def get_candidates_by_skill(skill_name):
    data = []
    for candidate in load_candidates_from_json():
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            data.append(candidate)
    return data

