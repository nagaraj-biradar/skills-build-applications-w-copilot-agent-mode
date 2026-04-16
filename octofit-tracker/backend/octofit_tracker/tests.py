from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, 'Marvel')

    def test_team_creation(self):
        team = Team.objects.create(name='Avengers', members=['Iron Man', 'Thor'])
        self.assertEqual(team.name, 'Avengers')
        self.assertIn('Iron Man', team.members)

    def test_activity_creation(self):
        activity = Activity.objects.create(user='Test', activity='Run', duration=30)
        self.assertEqual(activity.activity, 'Run')
        self.assertEqual(activity.duration, 30)

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user='Test', score=100)
        self.assertEqual(lb.score, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(user='Test', workout='Pushups', reps=50)
        self.assertEqual(workout.workout, 'Pushups')
        self.assertEqual(workout.reps, 50)
