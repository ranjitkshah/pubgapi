from django.db import models

# Create your models here.

class AR(models.Model):
    name = models.CharField(max_length=60)
    ammo = models.FloatField()
    mag  = models.FloatField()
    ext_mag = models.FloatField()
    fire_rate = models.FloatField()
    damage  = models.FloatField()  
    bullet_speed = models.FloatField()
    rload = models.FloatField()
    shot_range  = models.FloatField()
    scoped_spread = models.FloatField()
    dps = models.FloatField()
    

    def __str__(self):
        return self.name

class smg(models.Model):
    name = models.CharField(max_length=60)
    ammo = models.FloatField()
    mag  = models.FloatField()
    ext_mag = models.FloatField()
    fire_rate = models.FloatField()
    damage  = models.FloatField()  
    bullet_speed = models.FloatField()
    rload = models.FloatField()
    shot_range  = models.FloatField()
    scoped_spread = models.FloatField()
    dps = models.FloatField()
    

    def __str__(self):
        return self.name

class sniper(models.Model):
    name = models.CharField(max_length=60)
    ammo = models.FloatField()
    mag  = models.FloatField()
    ext_mag = models.FloatField()
    fire_rate = models.FloatField()
    damage  = models.FloatField()  
    bullet_speed = models.FloatField()
    rload = models.FloatField()
    shot_range  = models.FloatField()
    scoped_spread = models.FloatField()
    dps = models.FloatField()
    

    def __str__(self):
        return self.name

class dmr(models.Model):
    name = models.CharField(max_length=60)
    ammo = models.FloatField()
    mag  = models.FloatField()
    ext_mag = models.FloatField()
    fire_rate = models.FloatField()
    damage  = models.FloatField()  
    bullet_speed = models.FloatField()
    rload = models.FloatField()
    shot_range  = models.FloatField()
    scoped_spread = models.FloatField()
    dps = models.FloatField()
    

    def __str__(self):
        return self.name

class lmg(models.Model):
    name = models.CharField(max_length=60)
    ammo = models.FloatField()
    mag  = models.FloatField()
    ext_mag = models.FloatField()
    fire_rate = models.FloatField()
    damage  = models.FloatField()  
    bullet_speed = models.FloatField()
    rload = models.FloatField()
    shot_range  = models.FloatField()
    scoped_spread = models.FloatField()
    dps = models.FloatField()
    

    def __str__(self):
        return self.name

class shotgun(models.Model):
    name = models.CharField(max_length=60)
    ammo = models.FloatField()
    mag  = models.FloatField()
    ext_mag = models.FloatField()
    fire_rate = models.FloatField()
    damage  = models.FloatField()  
    bullet_speed = models.FloatField()
    rload = models.FloatField()
    shot_range  = models.FloatField()
    scoped_spread = models.FloatField()
    dps = models.FloatField()
    

    def __str__(self):
        return self.name

class pistol(models.Model):
    name = models.CharField(max_length=60)
    ammo = models.FloatField()
    mag  = models.FloatField()
    ext_mag = models.FloatField()
    fire_rate = models.FloatField()
    damage  = models.FloatField()  
    bullet_speed = models.FloatField()
    rload = models.FloatField()
    shot_range  = models.FloatField()
    scoped_spread = models.FloatField()
    dps = models.FloatField()
    

    def __str__(self):
        return self.name


class other(models.Model):
    name = models.CharField(max_length=60)
    ammo = models.CharField(max_length=60)
    mag  = models.FloatField()
    ext_mag = models.FloatField()
    fire_rate = models.FloatField()
    damage  = models.FloatField()  
    bullet_speed = models.FloatField()
    rload = models.FloatField()
    shot_range  = models.FloatField()
    scoped_spread = models.FloatField()
    dps = models.FloatField()
    

    def __str__(self):
        return self.name


class grip(models.Model):
    name = models.CharField(max_length=60)
    DRP  = models.FloatField()
    H_recoil = models.FloatField()
    V_recoil = models.CharField(max_length=60)
    sway  = models.FloatField()  
    kick_animation = models.FloatField()
    dec_adsSpeed = models.FloatField()

    def __str__(self):
        return self.name


class health(models.Model):
    name = models.CharField(max_length=60)
    health_gained  = models.FloatField()  
    action_time = models.CharField(max_length=60)
    boost_bar = models.CharField(max_length=20)
    duration = models.FloatField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    email=models.EmailField(max_length=50)
    message=models.TextField(max_length=500)

    def __str__(self):
        return self.email