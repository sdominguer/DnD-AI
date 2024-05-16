import numpy as np
import matplotlib.pyplot as plt
import random
from .models import *

class Habitacion:
    def __init__(self, x, y, w, h, room_type):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.room_type = room_type
        self.treasure = False
        self.boss = False
        self.spawn = False
        self.portal = False

def crear_habitacion(mapa, min_size, max_size, room_type):
    h = random.randint(min_size, max_size)
    w = random.randint(min_size, max_size)
    x = random.randint(1, mapa.shape[1] - w - 1)
    y = random.randint(1, mapa.shape[0] - h - 1)

    # Asegurar que la habitación no se superponga con otras
    if np.any(mapa[y:y+h, x:x+w] != ''):
        return None

    return Habitacion(x, y, w, h, room_type)

def designar_habitaciones_especiales(rooms):
    # Seleccionar habitación para spawn de jugadores
    habitacion_spawn = random.choice(rooms)
    habitacion_spawn.spawn = True
    
    # Seleccionar tres rooms para jefes
    habitaciones_boss = 0
    while habitaciones_boss < 3:
        h = random.choice(rooms)
        if not h.spawn:
            h.boss = True
            habitaciones_boss += 1
    
    # Seleccionar rooms para tesoros
    for h in rooms:
        if random.random() < 0.20:  # 20% de probabilidad de tener tesoro (cofre)
            h.treasure = True

    # Seleccionar rooms para portales
    habitaciones_portal = 0
    while habitaciones_portal < int(len(rooms)*0.015): # el 2% de las rooms tienen portal
        h = random.choice(rooms)
        if not h.spawn and not h.boss:
            h.portal = True
            habitaciones_portal += 1



def distancia(h1, h2):
    # Calcular la distancia entre el centro de dos rooms
    centro_h1 = (h1.x + h1.w // 2, h1.y + h1.h // 2)
    centro_h2 = (h2.x + h2.w // 2, h2.y + h2.h // 2)
    return np.sqrt((centro_h1[0] - centro_h2[0]) ** 2 + (centro_h1[1] - centro_h2[1]) ** 2)

def conectar_habitaciones(mapa, habitacion1, habitacion2, tipo_pasillo, campaign_id):
    puntos1 = (random.randint(habitacion1.x, habitacion1.x + habitacion1.w - 1),
               random.randint(habitacion1.y, habitacion1.y + habitacion1.h - 1))
    puntos2 = (random.randint(habitacion2.x, habitacion2.x + habitacion2.w - 1),
               random.randint(habitacion2.y, habitacion2.y + habitacion2.h - 1))

    # Crear un pasillo horizontal o vertical
    ancho_pasillo = random.randint(1, 2)
    if random.random() < 0.5:  # horizontal primero, luego vertical
        for x in range(min(puntos1[0], puntos2[0]), max(puntos1[0], puntos2[0]) + 1):
            for offset in range(ancho_pasillo):
                if 0 <= puntos1[1] + offset < mapa.shape[0]:
                    #mapa[puntos1[1] + offset, x] = tipo_pasillo
                    Tile.objects.update_or_create(campaign_id=campaign_id, x=x, y=puntos1[1] + offset, defaults={'tile_type': tipo_pasillo})
        for y in range(min(puntos1[1], puntos2[1]), max(puntos1[1], puntos2[1]) + 1):
            for offset in range(ancho_pasillo):
                if 0 <= puntos2[0] + offset < mapa.shape[1]:
                    #mapa[y, puntos2[0] + offset] = tipo_pasillo
                    Tile.objects.update_or_create(campaign_id=campaign_id, x=puntos2[0] + offset, y=y, defaults={'tile_type': tipo_pasillo})
    else:  # vertical primero, luego horizontal
        for y in range(min(puntos1[1], puntos2[1]), max(puntos1[1], puntos2[1]) + 1):
            for offset in range(ancho_pasillo):
                if 0 <= puntos1[0] + offset < mapa.shape[1]:
                    #mapa[y, puntos1[0] + offset] = tipo_pasillo
                    Tile.objects.update_or_create(campaign_id=campaign_id, x=puntos1[0] + offset, y=y, defaults={'tile_type': tipo_pasillo})
        for x in range(min(puntos1[0], puntos2[0]), max(puntos1[0], puntos2[0]) + 1):
            for offset in range(ancho_pasillo):
                if 0 <= puntos2[1] + offset < mapa.shape[0]:
                    #mapa[puntos2[1] + offset, x] = tipo_pasillo
                    Tile.objects.update_or_create(campaign_id=campaign_id, x=x, y=puntos2[1] + offset, defaults={'tile_type': tipo_pasillo})


def generate_object(campaign_id, room, object_type, entity=None):
    tries = 30
    while tries > 0:
        x = random.randint(room.x, room.x + room.w - 1)
        y = random.randint(room.y, room.y + room.h - 1)

        if object_type == 'treasure':
            existent_treasure = Treasure.objects.filter(campaign_id=campaign_id, x=x, y=y)
            
            if not existent_treasure:
                Treasure.objects.create(campaign_id=campaign_id, treasure_type='Chest', x=x, y=y)
                break
            else:
                tries -= 1

        elif object_type == 'portal':
            existent_treasure = Treasure.objects.filter(campaign_id=campaign_id, x=x, y=y)
            if not existent_treasure:
                Treasure.objects.create(campaign_id=campaign_id, treasure_type='Portal', x=x, y=y)
                break
            else:
                tries -= 1

        if object_type == 'player':
            existent_player = Character.objects.filter(campaign_id=campaign_id, x=x, y=y)
            existent_treasure = Treasure.objects.filter(campaign_id=campaign_id, x=x, y=y)
            
            if not existent_player and not existent_treasure:
                entity.x = x
                entity.y = y
                entity.save()
                break
            else:
                tries -= 1

        if object_type == 'monster':
            existent_player = Character.objects.filter(campaign_id=campaign_id, x=x, y=y)
            existent_treasure = Treasure.objects.filter(campaign_id=campaign_id, x=x, y=y)
            existent_monster = Monster.objects.filter(campaign_id=campaign_id, x=x, y=y)
            
            if not existent_player and not existent_treasure and not existent_monster:
                entity.x = x
                entity.y = y
                entity.save()
                break
            else:
                tries -= 1

        elif object_type == 'boss':
            entity.x = x
            entity.y = y
            entity.save()
            break
    if tries == 0:
        return False
    return True
    

def generate_mapa_dungeon(campaign: Campaign) -> bool:
    #campaign = Campaign.objects.get(id=campaign_id)
    #print(campaign)
    campaign_id = campaign.id
    dimx = campaign.size_x
    dimy = campaign.size_y

    if dimx * dimy > 500000:
        print('Mapa demasiado grande')
        return False
    
    mapa = np.full((dimy, dimx), '', dtype=object)

    total_tiles = dimx * dimy   # 200
    num_habitaciones = total_tiles // 200  # 1 habitación por cada 200 tiles

    room_types = ['path', 'dungeon', 'grass', 'dirt']
    boss_types = ['boss', 'psycho', 'hell', 'god']
    path_types = ['dirt', 'path', 'dungeon']

    rooms = []
    while len(rooms) < num_habitaciones:
        room_type = random.choice(room_types)
        new_room = crear_habitacion(mapa, 4, 10, room_type)
        if new_room:
            if rooms:
                # Conectar con la habitación más cercana
                habitacion_cercana = min(rooms, key=lambda h: distancia(h, new_room))

                # Quizás sería mejor ponerlo a lo último
                conectar_habitaciones(mapa, habitacion_cercana, new_room, random.choice(path_types), campaign_id)
            rooms.append(new_room)
            mapa[new_room.y:new_room.y + new_room.h, new_room.x:new_room.x + new_room.w] = new_room.room_type

    # Designar rooms para spawn de jugadores, jefes y tesoros
    designar_habitaciones_especiales(rooms)

    boss_counter = 0
    key_bosses = Monster.objects.filter(campaign_id=campaign_id, is_boss=True, is_key=True)
    if key_bosses.count() < 3:
        key_bosses = generate_key_bosses(campaign_id, 3)

    for room in rooms:

        tile_type = room.room_type

        if room.spawn:
            tile_type = 'spawn'
            generate_object(campaign_id, room, 'portal')
            for player in Character.objects.filter(campaign_id=campaign_id):
                generate_object(campaign_id, room, 'player', player)

        elif room.boss:
            tile_type = random.choice(boss_types)
            try:
                generate_object(campaign_id, room, 'boss', key_bosses[boss_counter])
                boss_counter += 1
            except:
                pass

        elif room.portal:
            tile_type = 'portal'
            generate_object(campaign_id, room, 'portal')

        elif room.treasure:
            generate_object(campaign_id, room, 'treasure')
            # 15% de probabilidad de tener dos tesoros
            # 2% de probabilidad de tener tres tesoros
            how_much = random.random()
            if how_much < 0.02:
                generate_object(campaign_id, room, 'treasure')
                generate_object(campaign_id, room, 'treasure')
            if how_much < 0.15:
                generate_object(campaign_id, room, 'treasure')

        for x in range(room.x, room.x + room.w):
            for y in range(room.y, room.y + room.h):
                Tile.objects.update_or_create(campaign_id=campaign_id, x=x, y=y, defaults={'tile_type': tile_type})

                '''
                spawn = random.random()

                if spawn < 0.05 and not room.spawn:
                    pass
                '''

                


    
    non_boss_rooms = [room for room in rooms if not room.boss]
    non_spawn_rooms = [room for room in rooms if not room.spawn]

    for NPC in Character.objects.filter(campaign_id=campaign_id, is_playable=False):
        generate_object(campaign_id, random.choice(non_boss_rooms), 'player', NPC)
    
    '''
    for monster in Monster.objects.filter(campaign_id=campaign_id, is_key=False, is_boss=False):
        generate_object(campaign_id, random.choice(non_spawn_rooms), 'monster', monster)
    
    for monster in Monster.objects.filter(campaign_id=campaign_id, is_key=True, is_boss=False):
        generate_object(campaign_id, random.choice(non_spawn_rooms), 'monster', monster)

    for monster in Monster.objects.filter(campaign_id=campaign_id, is_key=False, is_boss=True):
        generate_object(campaign_id, random.choice(non_spawn_rooms), 'monster', monster)
    '''
    

    return True

# Ejemplo de uso
# no más de 500.000 tiles
# generate_mapa_dungeon(3)

# -----------------------------------------------------------------------------------------------------------

def generate_unique_weapon():
    from DnD_AI.default import UNIQUE_WEAPONS_NAMES, UNIQUE_WEAPONS_STATS

    weapon_name = random.choice(list(UNIQUE_WEAPONS_NAMES))
    weapon_stats = UNIQUE_WEAPONS_STATS[weapon_name]

    unique_weapon = Weapon.objects.create(
        is_template=False,
        name=weapon_name,
        is_ranged=weapon_stats['is_ranged'],
        weapon_type=weapon_stats['weapon_type'],  
        damage_type=weapon_stats['damage_type'],  
        physical_description=weapon_stats['physical_description'],
        image=weapon_stats['image'],
        damage=weapon_stats['damage'],
        range=weapon_stats['range'],
        range_level_points=0,
        durability=100,
    )
    unique_weapon.save()

    return unique_weapon




def generate_key_bosses(campaign_id, n:int = 3):
    from DnD_AI.functions_AI import campaign_interpreter, image_generator_DallE, image_generator_StabDiff
    from DnD_AI.default import COOL_NAMES, DEFAULT_RACES, DEFAULT_CLASSES, COOL_BOSSES_WITH_ICON

    FILTERED_CLASSES = [player_class for player_class in DEFAULT_CLASSES if player_class not in DEFAULT_RACES]
    
    attributes_dict, API_KEY_GEMINI = campaign_interpreter(campaign_id, n)

    unique_weapons = [generate_unique_weapon() for _ in range(n)]

    key_bosses = []

    for i in range(n):

        no_api_name, no_api_boss_race, no_api_boss_class, no_api_physical_description = None, None, None, None
        if not API_KEY_GEMINI:
            no_api_name = random.choice(COOL_NAMES)
            no_api_boss_race = random.choice(DEFAULT_RACES)
            no_api_boss_class = random.choice(FILTERED_CLASSES)
            no_api_physical_description = no_api_boss_race+' '+no_api_boss_class

        key_boss = Monster.objects.create(
            name=no_api_name if not API_KEY_GEMINI else attributes_dict['name'][i],
            is_key=True,
            is_boss=True,
            monster_race=no_api_boss_race if not API_KEY_GEMINI else  attributes_dict['race'][i],
            monster_class=no_api_boss_class if not API_KEY_GEMINI else attributes_dict['class'][i],
            physical_description=no_api_physical_description if not API_KEY_GEMINI else  attributes_dict['physical_description'][i],
            weapon=unique_weapons[i],
            campaign_id=campaign_id,
            max_health=random.randint(4,6)*100,
            strength=random.randint(10,15),
            intelligence=random.randint(10,15),
            recursiveness=random.randint(10,15),
            dexterity=random.randint(10,15),
            physical_resistance=random.randint(10,15), 
            magical_resistance=random.randint(10,15),
            constitution=random.randint(10,15),
            exp_drop=1000,
            x=random.randint(0,10),
            y=random.randint(0,10),
        )

        boss_personality = random.choice(['making a smug face', 'laughing...', 'looking at you with a serious face', 'smiling', 'intimidating'])

        image_description = f"{key_boss.name}{key_boss.monster_race} {key_boss.monster_class} holding a {key_boss.weapon.weapon_type}, {key_boss.physical_description} is {boss_personality}"
        try:
            image_dir_DallE = image_generator_DallE(image_description).replace('media/', '')
            key_boss.icon = image_dir_DallE
        except:
            try:
                image_dir_StabDiff = image_generator_StabDiff(image_description).replace('media/', '')
                key_boss.icon = image_dir_StabDiff
            except:
                name = random.choice(COOL_BOSSES_WITH_ICON)
                icon_path = name.replace(' ', '-').lower()+'.png'
                icon = f"entity/icons/boss_icons/{icon_path}.png"

                key_boss.name = name
                key_boss.icon = icon

        key_boss.save()

        key_bosses.append(key_boss)

    return key_bosses


# -----------------------------------------------------------------------------------------------------------

'''
# Visualización del mapa en matplotlib
    # Rellenar las rooms y los pasillos en el mapa
    for room in rooms:
        if room.spawn:
            mapa[room.y:room.y + room.h, room.x:room.x + room.w] = 'spawn'
        elif room.boss:
            mapa[room.y:room.y + room.h, room.x:room.x + room.w] = 'boss'
        elif room.treasure:
            mapa[room.y:room.y + room.h, room.x:room.x + room.w] = 'treasure'
        elif room.portal:
            mapa[room.y:room.y + room.h, room.x:room.x + room.w] = 'portal'
        else:
            mapa[room.y:room.y + room.h, room.x:room.x + room.w] = room.room_type

    # Convertir nombres a colores RGB
    
    color_map = {'': [0, 0, 0], 'path': [210, 180, 140], 'dungeon': [128, 128, 128], 'boss': [255, 0, 0], 'god': [255, 255, 0], 'psycho': [75, 0, 130], 'hell': [11, 111, 11], 'grass': [0, 128, 0], 'dirt': [139, 69, 19], 'Spawn': [255, 255, 224], 'Boss': [255, 0, 0], 'Treasure': [255, 223, 0]}
    
    color_map = {
        '':         [0, 0, 0], 
        'path':     [210, 180, 140], 
        'dungeon':  [128, 128, 128],
        'god':      [255, 255, 255], 
        'psycho':   [255, 255, 255],
        'hell':     [255, 255, 255],
        'grass':    [255, 255, 255],
        'dirt':     [255, 255, 255],
        
        'spawn':    [0, 0, 255],
        'boss':     [255, 0, 0],
        'treasure': [0, 255, 0],
        'portal':   [255, 100, 255],
        }
    
    mapa_colorido = np.array([[color_map[cell] for cell in row] for row in mapa])

    # Visualización
    plt.figure(figsize=(10, 10))
    plt.imshow(mapa_colorido, interpolation='nearest')
    plt.title("Mapa de Mazmorra Procedural con Juego Integrado")
    plt.xticks([])
    plt.yticks([])
    plt.show()
'''