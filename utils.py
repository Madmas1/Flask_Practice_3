# Модуль с основными функциями

# Подключаем модуль по обработке JSON
import json


#Основные методы

def load_candidates_from_json(filename):
    """Метод получения всего списка кандидатов в формате словаря"""
    with open(filename, 'r', encoding='utf-8') as candidates:
        candidates_list = json.load(candidates)
    return candidates_list


def get_candidate_by_id(candidate_list, candidate_id):
    """Метод получения информация о кандидате по его ID"""
    for candidate in candidate_list:
        if candidate_id == candidate['id']:
            candidate_data = {
                "name": candidate["name"],
                "position": candidate["position"],
                "picture": candidate["picture"],
                "skills": candidate["skills"]
            }
    return candidate_data


def get_candidate_by_name(candidate_list, candidate_name):
    """Метод получения информация о кандидатах по имени"""
    count = 0
    candidates = []
    for candidate in candidate_list:
        if candidate_name.lower() in candidate["name"].lower():
            candidate_data = {
                'id': candidate['id'],
                'name': candidate['name']
            }
            count += 1
            candidates.append(candidate_data)
    return candidates, count


def get_candidate_by_skill(candidate_list, candidate_skill):
    """Метод для поиска кандидатов по скиллу"""
    count = 0
    candidates = []
    for candidate in candidate_list:
        if candidate_skill.lower() in candidate["skills"].lower():
            candidate_data = {
                'id': candidate['id'],
                'name': candidate['name']
            }
            count += 1
            candidates.append(candidate_data)
    return candidates, count