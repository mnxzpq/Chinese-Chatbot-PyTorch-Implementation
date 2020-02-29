import fire
from sanic import Sanic
from sanic_api.urls.url import nlp_blueprint
from sanic_api.models.api import robot


def main(**kwargs):
    robot.init_torch(**kwargs)
    app = Sanic("AI REST SERVER")
    app.blueprint(nlp_blueprint)
    app.run(host="0.0.0.0", port=10001)


if __name__ == '__main__':
    fire.Fire(main)
