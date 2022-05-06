
# Подключаем модули Flask и модуль c нашими методами
from flask import Flask, render_template
import utils

# Создаем экземпляр класса Flask
app = Flask(__name__)

# Загружаем данные кандидатов из JSON
candidates_list = utils.load_candidates_from_json("candidates.JSON")


# Метод рендера главной страницы
@app.route("/")
def show_main_page():
    return render_template('list.html', candidates=candidates_list)


# Метод рендера персональной страницы кандиадата по его ID
@app.route("/candidates/<int:candidate_id>")
def show_candidate_page_by_id(candidate_id):
    return render_template('card.html', candidate=utils.get_candidate_by_id(candidates_list, candidate_id))


# Метод рендера страницы c
@app.route("/candidates/<candidate_name>")
def show_candidate_page_by_name(candidate_name):
    candidates, count = utils.get_candidate_by_name(candidates_list, candidate_name)
    return render_template('search_name.html', candidates=candidates, count=count)


#
@app.route("/skills/<candidate_skill>")
def show_candidate_page_by_skill(candidate_skill):
    candidates, count = utils.get_candidate_by_skill(candidates_list, candidate_skill)
    return render_template('search_skills.html', candidates=candidates, count=count, candidate_skill=candidate_skill)


# Запускаем приложение
app.run()