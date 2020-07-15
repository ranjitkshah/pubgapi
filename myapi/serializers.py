from rest_framework import serializers

from .models import *

class ARSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AR
        fields = ('name', 'ammo','mag','ext_mag','fire_rate','damage','bullet_speed','rload','shot_range','scoped_spread','dps')


class smgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = smg
        fields = ('name', 'ammo','mag','ext_mag','fire_rate','damage','bullet_speed','rload','shot_range','scoped_spread','dps')

class lmgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = lmg
        fields = ('name', 'ammo','mag','ext_mag','fire_rate','damage','bullet_speed','rload','shot_range','scoped_spread','dps')

class dmrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = dmr
        fields = ('name', 'ammo','mag','ext_mag','fire_rate','damage','bullet_speed','rload','shot_range','scoped_spread','dps')

class shotgunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = shotgun
        fields = ('name', 'ammo','mag','ext_mag','fire_rate','damage','bullet_speed','rload','shot_range','scoped_spread','dps')

class pistolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pistol
        fields = ('name', 'ammo','mag','ext_mag','fire_rate','damage','bullet_speed','rload','shot_range','scoped_spread','dps')

class otherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = other
        fields = ('name', 'ammo','mag','ext_mag','fire_rate','damage','bullet_speed','rload','shot_range','scoped_spread','dps')

class sniperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = sniper
        fields = ('name', 'ammo','mag','ext_mag','fire_rate','damage','bullet_speed','rload','shot_range','scoped_spread','dps')

class gripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = grip
        fields = ('name','DRP','H_recoil','V_recoil','sway','kick_animation','dec_adsSpeed')


class healthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = health
        fields = ('name', 'action_time','health_gained','boost_bar','duration')

# class gunSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = gun
#         fields = ('name','type', 'ammo','mag','ext_mag','fire_rate','damage','bullet_speed','rload','shot_range','scoped_spread','dps')

# # class GuntypeSerializer(serializers.HyperlinkedModelSerializer):
# #     class Meta:
# #         model = Guntype
# #         fields = ('type')






