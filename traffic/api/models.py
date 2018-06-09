from __future__ import unicode_literals

from django.db import models
from api.internal_models.route import Route


class City:
    def __init__(self, time, population, routes):
        self.time = time
        self.population = population
        self.routes = []
        for r in routes:
            self.routes.append(Route(r))
