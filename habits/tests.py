from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="test user",
            password="12345",
        )
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            place="зал",
            time="4:20:00",
            action="йога",
            reward="качать пресс",
            owner=self.user,
            duration='30',
            is_public=True
        )

    def test_get_habits(self):
        url = reverse("habits:habit_list")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), response.json(),
                         {
                             "count": 1,
                             "next": None,
                             "previous": None,
                             "results": [
                                 {
                                     "id": self.habit.id,
                                     "place": self.habit.place,
                                     "time": self.habit.time,
                                     "action": self.habit.action,
                                     "is_pleasnt": self.habit.is_pleasnt,
                                     "period": self.habit.period,
                                     "reward": self.habit.reward,
                                     "duration": self.habit.duration,
                                     "is_public": self.habit.is_public,
                                     "owner": self.habit.owner_id,
                                     "linked": self.habit.linked
                                 }
                             ]
                         }
                         )

    def test_get_public_habits(self):
        url = reverse("habits:public_habit_list")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_habits(self):
        url = reverse("habits:habit_create")
        data = {
            "place": "дом",
            "time": "18:00:00",
            "action": "учиться",
            "reward": "учиться ",
            "is_public": True,
            "owner": self.habit.owner_id,
            "duration": '30'
        }

        response = self.client.post(url, data=data)
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Habit.objects.all().count(), 2)

    def test_update_habits(self):
        url = reverse("habits:habit_update", args=[self.habit.id])
        data = {
            "place": "дом",
            "time": "18:00:00",
            "action": "учиться",
            "reward": "учится больше",
            "is_public": True,
            "owner": self.habit.owner_id,
            "duration": '30'
        }

        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habits(self):
        url = reverse("habits:habit_delete", args=[self.habit.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_duration_validator(self):
        url = reverse("habits:habit_create")
        data = {
            "place": "дом",
            "time": "18:00:00",
            "action": "закрыть таску",
            "reward": "зп",
            "is_public": True,
            "owner": self.habit.owner_id,
            "duration": 121
        }

        response = self.client.post(url, data=data)

        self.assertEquals(response.status_code,
                          status.HTTP_400_BAD_REQUEST)

    def test_period_validator(self):
        url = reverse("habits:habit_create")
        data = {
            "place": "дом",
            "time": "18:00:00",
            "action": "закрыть таску",
            "reward": "зп",
            "is_public": True,
            "owner": self.habit.owner_id,
            "period": 8,
            "duration": 12
        }

        response = self.client.post(url, data=data)

        self.assertEquals(response.status_code,
                          status.HTTP_400_BAD_REQUEST)

    def test_is_pleasant_validator(self):
        url = reverse("habits:habit_create")
        data = {
            "place": "дом",
            "time": "18:00:00",
            "action": "закрыть таску",
            "reward": "зп",
            "is_pleasnt": True,
            "is_public": True,
            "owner": self.habit.owner_id,
            "duration": 12
        }

        response = self.client.post(url, data=data)

        self.assertEquals(response.status_code,
                          status.HTTP_400_BAD_REQUEST)
