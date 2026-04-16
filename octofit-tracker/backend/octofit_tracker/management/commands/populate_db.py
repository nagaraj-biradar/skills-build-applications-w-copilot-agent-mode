from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model
from djongo import models

from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Users (superheroes)
        users = [
            {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
            {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
        ]
        db.users.insert_many(users)
        db.users.create_index([("email", 1)], unique=True)

        # Teams
        teams = [
            {"name": "Marvel", "members": ["Iron Man", "Captain America", "Black Widow"]},
            {"name": "DC", "members": ["Superman", "Batman", "Wonder Woman"]},
        ]
        db.teams.insert_many(teams)

        # Activities
        activities = [
            {"user": "Superman", "activity": "Flight", "duration": 120},
            {"user": "Batman", "activity": "Martial Arts", "duration": 90},
            {"user": "Wonder Woman", "activity": "Lasso Training", "duration": 60},
            {"user": "Iron Man", "activity": "Suit Test", "duration": 80},
            {"user": "Captain America", "activity": "Shield Practice", "duration": 70},
            {"user": "Black Widow", "activity": "Espionage", "duration": 100},
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {"user": "Superman", "score": 1000},
            {"user": "Iron Man", "score": 950},
            {"user": "Batman", "score": 900},
            {"user": "Wonder Woman", "score": 850},
            {"user": "Captain America", "score": 800},
            {"user": "Black Widow", "score": 750},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {"user": "Superman", "workout": "Strength", "reps": 100},
            {"user": "Batman", "workout": "Endurance", "reps": 80},
            {"user": "Wonder Woman", "workout": "Agility", "reps": 90},
            {"user": "Iron Man", "workout": "Tech", "reps": 70},
            {"user": "Captain America", "workout": "Cardio", "reps": 85},
            {"user": "Black Widow", "workout": "Flexibility", "reps": 95},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
