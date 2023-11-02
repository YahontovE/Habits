from rest_framework import serializers

from habits.models import Habit
from habits.validators import DurationValidator, RelatedHabitAndRewardValidator, IsPleasantValidator, PeriodValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

        validators = [
            DurationValidator(field='duration'),
            RelatedHabitAndRewardValidator(field1='linked', field2='reward'),
            IsPleasantValidator(field1='is_pleasnt', field2='linked', field3='reward'),
            PeriodValidator(field='period')
        ]
