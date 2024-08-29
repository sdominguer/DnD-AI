from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Weapon)
<<<<<<< HEAD
admin.site.register(Character)
admin.site.register(Monster)
admin.site.register(Treasure)
admin.site.register(History)
admin.site.register(Tile)
admin.site.register(Campaign)
=======
#admin.site.register(Character)
#admin.site.register(Monster)
admin.site.register(Treasure)
admin.site.register(History)
admin.site.register(Tile)
admin.site.register(Campaign)

@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_boss', 'is_key', 'name', 'monster_race', 'monster_class', 'weapon')
    search_fields = ('campaign__id', 'id', 'name', 'monster_race', 'monster_class', 'x', 'y', 'weapon__id', 'weapon__name')
    list_filter = ('is_boss', 'is_key', 'campaign__id', 'monster_race', 'monster_class')

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_playable', 'name', 'character_race', 'character_class', 'weapon')
    search_fields = ('campaign__id', 'id', 'name', 'character_race', 'character_class', 'x', 'y', 'weapon__id', 'weapon__name')
    list_filter = ('campaign__id', 'character_race', 'character_class', 'is_playable')
>>>>>>> 6b7a768c3d598e5168f830ce4ec720a35e4c9f23
