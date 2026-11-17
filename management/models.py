from django.db import models

# Create your models here.

class Facultyteam(models.Model):
    SPORT_TYPE_OPTIONS = [
        ("Football","Football"),
         ("Netball","Netball") ,
         ("Volleyball","Volleyball"),
         ("Basketball","Basketball"),
         ("Athletics","Athletics"),
    ]

    name = models.CharField(max_length=100)
    sport_type = models.CharField(max_length= 15, choices=SPORT_TYPE_OPTIONS)
    team_manager = models.CharField(max_length= 100)
    number_of_registered_players = models.PositiveBigIntegerField()


class Student(models.Model):
    GENDER_OPTIONS = [
        ("F", "Female"),
        ("M", "Male")
    ]

    PLAYER_ROLE = [
       ( "Goalkeeper", "Goalkeeper"), 
       ("Striker", "Striker"), 
        ("Setter","Setter"),
        ( "Center", "Center")
    ]
    regno = models.CharField(max_length=15 , unique=true)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=2 , choices=GENDER_OPTIONS)
    facuty = models.CharField(max_length=100)
    sport_type = models.CharField(max_length=50)
    player_role = models.CharField(max_length=50 , choices=PLAYER_ROLE)
    team = models.ForeignKey(Facultyteam, on_delete=models.CASCADE)


class Venue(models.Model):
    VENUE_TYPE_OPYIONS = [
       ( "football_pitch", "football_pitch"), 
       ("indoor_court","indoor_court"),
       ("netball_court","netball_court"),
       ("track_field","track_field")
    ]
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=100, choices=VENUE_TYPE_OPYIONS)
    capacity = models.PositiveIntegerField()


class Match(models.Model):
    MATCH_DAY = [
       ( "Monday", "Monday") ,
       ("Tuesday","Tuesday"),
       ("Wednesday","Wednesday"),
       ("Thursday","Thursday")
    ]
    match_day =models.CharField(max_length=100, choices=MATCH_DAY)
    value = models.ForeignKey(Venue, on_delete=models.CASCADE)






    
