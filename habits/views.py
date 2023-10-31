from rest_framework import generics


class HabitCreateAPIView(generics.CreateAPIView):
    pass


class HabitListAPIView(generics.ListAPIView):
    pass


class HabitUpdateAPIView(generics.UpdateAPIView):
    pass


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    pass


class HabitDestroyAPIView(generics.DestroyAPIView):
    pass
