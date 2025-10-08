import pgzrun
import random

game_time = 0
box_size = 32
border_height = 16
border_width = 16
planet = []
WIDTH = box_size * border_width
HEIGHT = box_size * border_height

mod = "menu" 

inventory = Actor("inventory", pos = (303,463))
bin = Actor("bin", pos = (495, 397))
computer = Actor("computer")
generator_green = Actor("generatorgreen")
rock_texture_grid = Actor("rocktexturebuildred")
rock_texture_grid_red = Actor("rocktexturebuildred")
menu = Actor("screen")
research = Actor("researchfon")
energy_icon = Actor("energy", pos = (115, 170))
heat_icon = Actor("heatlevel", pos = (115, 240))
start = Actor("start", pos = (256, 300))
radar_icon = Actor("radaricon", pos = (300, 300))
back_arrow = Actor("back", pos = (390, 170))
generator_green_research = Actor("generatorgreen", pos = (50, 256))
generator_blue_research = Actor("generatorblue", pos = (450, 256))
solar_panel_research = Actor("solarpanel", pos = (200, 256))
wrench_research = Actor("wrench", pos = (200, 306))
circut_green_research = Actor("circutgreen", pos = (200, 356))
energy_box_green_research = Actor("energyboxgreen", pos = (200, 206))
battery_green_research = Actor("batterygreen", pos = (200, 156))
radar_choice = Actor("radar", pos = (300, 206))
fire_Wall_choice = Actor("radar", pos = (345, 206))
faster_green_choice = Actor("radar", pos = (325, 306))
build_structure = Actor("radar", pos = (-100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000))

asteroids = []


research_list = [Actor("batterygreencompleted", pos = (200, 156)), 
                 Actor("energyboxgreencompleted", pos = (200, 206)), 
                 Actor("solarpanelcompleted", pos = (200, 256)), 
                 Actor("wiresresearchcompleted", pos = (200, 306)), 
                 Actor("circutgreencompleted", pos = (200, 356))]


asteroid_crash_time = -1
inventory_x = 120
inventory_y = 440
move_inventory_list = []
placed_objects = []
all_wires = []
wires_point_1 = -1
wires_point_2 = -1

research_cell = ["researchdownload1", "researchdownload2", "researchdownload1", "researchdownload2"]

computer.left = 0
computer.top = (border_height - 3) * box_size
generator_green.left = 7 * 32
generator_green.top = 7 * 32

heat_waves = random.randint(20, 70)
heat_random = random.randint(-150, 150)
asteroid = random.randint(2, 10)
virus = random.randint(30, 120)

#research_time_reduce = 0 ---- circut
max_heat = 1000
heat = 100
max_energy = 500
energy = 50
min_energy = 0
research_faster = 0
radar_unlocked = True
max_radar = 20
radar = 0
wires_2_cords = -1
research_cell_gone = True
build_menu = False
generator_blue = False
draw_wire_line = False
allow_wires_build = False


def research_window():
    screen.draw.filled_rect(Rect((170, 156), (5, 200)), (0,0,0))
    screen.draw.filled_rect(Rect((225, 156), (5, 200)), (0,0,0))
    screen.draw.filled_rect(Rect((270, 206), (5, 100)), (0,0,0))
    screen.draw.filled_rect(Rect((370, 206), (5, 105)), (0,0,0))
    screen.draw.filled_rect(Rect((50, 256), (150, 5)), (0,0,0))
    screen.draw.filled_rect(Rect((170, 156), (60, 5)), (0,0,0))
    screen.draw.filled_rect(Rect((170, 206), (60, 5)), (0,0,0))
    screen.draw.filled_rect(Rect((170, 256), (100, 5)), (0,0,0))
    screen.draw.filled_rect(Rect((170, 306), (60, 5)), (0,0,0))
    screen.draw.filled_rect(Rect((170, 356), (60, 5)), (0,0,0))
    screen.draw.filled_rect(Rect((270, 206), (100, 5)), (0,0,0))
    screen.draw.filled_rect(Rect((270, 306), (100, 5)), (0,0,0))
    screen.draw.filled_rect(Rect((370, 256), (50, 5)), (0,0,0))

    generator_green_research.draw()
    generator_blue_research.draw()
    solar_panel_research.draw()
    wrench_research.draw()
    circut_green_research.draw()
    energy_box_green_research.draw()
    battery_green_research.draw()
    radar_choice.draw()
    fire_Wall_choice.draw()
    faster_green_choice.draw()

    for i in range(len(research_list)):
        if research_true[i] == True:    
            research_list[i].draw()


research_time = [4, 4, 4, 4, 4, 4, 4, 4]

build_energy_amount = [50, 50, 10, 10, 10, 100]

research_names = ["batterygreen", "energyboxgreen", "solarpanel", "wrench", "circutgreen", "radar", "firewall", "greenfast"]
research_objects = [battery_green_research, energy_box_green_research, solar_panel_research, wrench_research, circut_green_research, radar_choice, fire_Wall_choice, faster_green_choice]
research_true = [False, False, False, False, False, False, False, False]
research_level = "green"
research_status = False
research_number = -1
research_timer_amount = 0

def game_time_manager():
    global game_time, asteroid_crash_time

    if game_time == asteroid_crash_time:
        asteroid = Actor("asteroid")
        asteroid.landing_spot = (random.randint(1, 15)*32, random.randint(1, 12)*32)
        asteroid.left = asteroid.landing_spot[0] -500
        asteroid.top = asteroid.landing_spot[1] -500
        animate(asteroid, "linear", 1, x = asteroid.landing_spot[0], y = asteroid.landing_spot[1])
        asteroids.append(asteroid)
        asteroid_crash_time = game_time + random.randint(1, 2)
    game_time += 1

clock.schedule_interval(game_time_manager, 1)
asteroid_crash_time = random.randint(1, 2)


def create_map():
    for i in range(border_height):
        row = []
        for j in range(border_width):
            row.append("rocktexture")
        planet.append(row)

create_map()
print(planet)

def heat_time():
    global heat
    heat += 50

clock.schedule_interval(heat_time, 120)

def draw_map():
    for i in range(border_height):
        for j in range(border_width):
            box = Actor(planet[i][j])
            box.left = i * box_size
            box.top = j * box_size
            box.draw()

def draw_energy():
    global energy, max_energy

    cost = max_energy // 20
    energy_icon.draw()
    for i in range(20):
        emptycell = Actor("emptycell", pos = (115 + 31 + 11 * i, 170))
        emptycell.draw()
    for i in range(int(energy) // cost):
        cell = Actor("cell", pos = (115 + 31 + 11 * i, 170))
        cell.draw()

def draw_heat():
    global max_heat, heat_waves, heat_random, heat
    cost = max_heat // 20
    heat_icon.draw()
    for i in range(20):
        emptycell = Actor("emptycell", pos = (115 + 31 + 11 * i, 240))
        emptycell.draw()
    heat_temp = min(heat + heat_random, max_heat)
    for i in range(int(heat_temp) // cost):
        cell = Actor("cell", pos = (115 + 31 + 11 * i, 240))
        cell.draw()

def draw_radar():
    global radar, radar_unlocked, radar_icon

    if radar_unlocked == True:
        cost = max_radar // 20
        radar_icon.draw()
        for i in range(20):
            emptycell = Actor("emptycell", pos = (115 + 31 + 11 * i, 240))
            emptycell.draw()
        for i in range(int(heat) // cost):
            cell = Actor("cell", pos = (115 + 31 + 11 * i, 240))
            cell.draw()

def draw_research_process():
    global research_timer_amount, research_number

    if research_time[research_number] - research_faster <= 0:
        cost = 1
    else:
        cost =  (research_time[research_number] - research_faster) // 4
    research_count = research_timer_amount // cost
    if research_count > 4:
        research_count = 4
    for i in range(research_count):
        cell = Actor(research_cell[i], pos = (research_objects[research_number].x - 12 + i * 8, research_objects[research_number].y))
        cell.draw()

def draw():
    global mod, research_status

    if mod == "game":
        draw_map()
        bin.draw()
        inventory.draw()
        computer.draw()
        generator_green.draw()
        for i in range(len(move_inventory_list)):
            move_inventory_list[i].draw()
        for i in range(len(placed_objects)):
            placed_objects[i].draw()
        if build_menu == True:
            rock_texture_grid.draw()
            build_structure.draw()
        show_text_tile()
        for i in range(len(all_wires)):
            all_wires[i].draw()
                
        if draw_wire_line == True:
            try:
                dx = wires_2_cords[0] - wires_point_1[0]
                dy = wires_2_cords[1] - wires_point_1[1]
                x2 = -1
                y2 = -1
                if dx > 0:
                    if dy > 0:
                        if abs(dx) >= abs(dy):
                            x2 = wires_point_1[0] + 32
                            y2 = wires_point_1[1]
                        else:
                            x2 = wires_point_1[0]
                            y2 = wires_point_1[1] + 32
                    else:
                        if abs(dx) >= abs(dy):
                            x2 = wires_point_1[0] + 32
                            y2 = wires_point_1[1]
                        else:
                            x2 = wires_point_1[0]
                            y2 = wires_point_1[1] - 32    
                else:
                    if dy > 0:
                        if abs(dx) >= abs(dy):
                            x2 = wires_point_1[0] - 32
                            y2 = wires_point_1[1]
                        else:
                            x2 = wires_point_1[0]
                            y2 = wires_point_1[1] + 32
                    else:
                        if abs(dx) >= abs(dy):
                            x2 = wires_point_1[0] - 32
                            y2 = wires_point_1[1]
                        else:
                            x2 = wires_point_1[0]
                            y2 = wires_point_1[1] - 32 
                            
                screen.draw.line(wires_point_1, (x2,y2), (225,0,0))
                screen.draw.line((wires_point_1[0]-1,wires_point_1[1]-1), (x2-1, y2-1), (225,0,0))
                screen.draw.line((wires_point_1[0]-1,wires_point_1[1]+1), (x2, y2+1), (225,0,0))
            except:
                print("hihi")
        for i in range(len(asteroids)):
            asteroids[i].draw()

    elif mod == "menu":
        menu.draw()
        start.draw()

    elif mod == "screen":
        menu.draw()
        draw_energy()
        draw_heat()
        #draw_radar()
        back_arrow.draw()

    elif mod == "research":
        research.draw()
        back_arrow.draw()
        research_window()
        if research_status == True:
            draw_research_process()

def research_prosses():
    global research_number, research_status, research_timer_amount, research_cell_gone,inventory_x,inventory_y
    
    if research_cell_gone == False:
        research_status = False
        research_cell_gone = True
    print(research_timer_amount)
    if research_status == True:
        research_timer_amount += 1 
        if research_timer_amount == research_time[research_number] - research_faster or (research_faster >= research_time[research_number] and research_timer_amount == 4):
            research_cell_gone = False
            research_true[research_number] = True
            research_object = Actor(research_names[research_number],(inventory_x,inventory_y))
            research_object.energy = build_energy_amount[research_number]
            move_inventory_list.append(research_object)
            inventory_x += 40
            if research_object.image == "wrench":
                new_object = Actor("wrenchdelete", (inventory_x,inventory_y))
                new_object.energy = 0
                move_inventory_list.append(new_object)
                inventory_x += 40


clock.schedule_interval(research_prosses, 1)

def research_update(button, pos):
    global research_number, research_status, research_timer_amount

    if battery_green_research.collidepoint(pos) and research_true[0] == False:  
        if research_number != 0:
            research_timer_amount = 0
        research_number = 0
        research_status = True
       
    elif energy_box_green_research.collidepoint(pos) and research_true[1] == False:
        if research_number != 1:
            research_timer_amount = 0
        research_number = 1
        research_status = True
    
    elif solar_panel_research.collidepoint(pos) and research_true[2] == False:
        if research_number != 2:
            research_timer_amount = 0
        research_number = 2
        research_status = True
    
    elif wrench_research.collidepoint(pos) and research_true[3] == False:
        if research_number != 3:
            research_timer_amount = 0
        research_number = 3
        research_status = True

    elif circut_green_research.collidepoint(pos) and research_true[4] == False:
        if research_number != 4:
            research_timer_amount = 0
        research_number = 4
        research_status = True

    elif radar_choice.collidepoint(pos) and research_true[5] == False:
        research_choice_check = research_true[0] and research_true[1] and research_true[2] and research_true[3] and research_true[4] and not research_true[7]
        if research_choice_check:  
            if research_number != 5:
                research_timer_amount = 0
            research_number = 5
            research_status = True

    elif fire_Wall_choice.collidepoint(pos) and research_true[6] == False:
        research_choice_check = research_true[5]
        if research_choice_check:
            if research_number != 6:
                research_timer_amount = 0
            research_number = 6
            research_status = True

    elif faster_green_choice.collidepoint(pos) and research_true[7] == False:
        research_choice_check = research_true[0] and research_true[1] and research_true[2] and research_true[3] and research_true[4] and not research_true[5]
        if research_choice_check:
            if research_number != 7:
                research_timer_amount = 0
            research_number = 7
            research_status = True

def show_text_tile():
    for i in range(len(placed_objects)):
        if placed_objects[i].image == "batterygreen":
            screen.draw.text(str(placed_objects[i].energy), (placed_objects[i].x - 9, placed_objects[i].y - 6), color = "#FFFFFF", fontsize = 16)

def heat_increase():
    global heat
    heat += 10

def energy_decrease():
    global energy

    if energy <= min_energy:
        energy -= 0
    else:
        energy -= 5

def energy_increase():
    global energy

    if energy >= max_energy:
        energy += 0

    else:
        energy += 10

def check_chips():
    global placed_objects

    for i in range(len(placed_objects)):
        if placed_objects[i].image == "circutGreen":
            pass

def on_mouse_down(button, pos):
    global mod, build_menu, move_inventory_list, energy, max_energy, research_faster, wires_point_1, wires_point_2, draw_wire_line, wires_2_cords, allow_wires_build

    if mod == "screen" and back_arrow.collidepoint(pos):
        mod = "game"

    if mod == "research" and back_arrow.collidepoint(pos):
        mod = "game"

    if mod == "research":
        research_update(button, pos)

    if mod == "game" and bin.collidepoint(pos) and build_menu == False:
        print("hehe")

    if mod == "menu" and start.collidepoint(pos):
        mod = "game"

    elif mod == "game" and computer.collidepoint(pos) and not build_menu == True:
        mod = "screen"

    elif mod == "game" and generator_green.collidepoint(pos) and not build_menu == True:
        mod = "research"

    elif mod == "game":
        if mod == "game" and build_menu == True:
            if build_structure.energy <= energy:
                if (build_structure.image == "wrench" or build_structure.image == "wrenchdelete") and allow_wires_build == True:

                    if wires_point_1 == -1:
                        wires_point_1 = rock_texture_grid.pos

                    elif wires_point_2 == -1:
                        wires_point_2 = rock_texture_grid.pos
                        draw_wire_line = False

                        dx = pos[0] - wires_point_1[0]
                        dy = pos[1] - wires_point_1[1]
                        if dx > 0:
                            if dy > 0:
                                if abs(dx) >= abs(dy) and check_wires((wires_point_1[0]+32, wires_point_1[1])):
                                    new_line = Actor('wiresgreenhor',(wires_point_1[0]+16, wires_point_1[1])) 
                                elif check_wires((wires_point_1[0], wires_point_1[1]+32)):
                                    new_line = Actor('wiresgreenver',(wires_point_1[0], wires_point_1[1]+16))
                            else:
                                if abs(dx) >= abs(dy) and check_wires((wires_point_1[0]+32, wires_point_1[1])):
                                   new_line = Actor('wiresgreenhor',(wires_point_1[0]+16, wires_point_1[1]))
                                elif check_wires((wires_point_1[0], wires_point_1[1]-32)):
                                    new_line = Actor('wiresgreenver',(wires_point_1[0], wires_point_1[1]-16))
                        else:
                            if dy > 0:
                                if abs(dx) >= abs(dy) and check_wires((wires_point_1[0]-32, wires_point_1[1])):
                                    new_line = Actor('wiresgreenhor',(wires_point_1[0]-16, wires_point_1[1]))
                                elif check_wires((wires_point_1[0], wires_point_1[1]+32)):
                                    new_line = Actor('wiresgreenver',(wires_point_1[0], wires_point_1[1]+16))
                            else:
                                if abs(dx) >= abs(dy) and check_wires((wires_point_1[0]-32, wires_point_1[1])):
                                    new_line = Actor('wiresgreenhor',(wires_point_1[0]-16, wires_point_1[1]))
                                elif check_wires((wires_point_1[0], wires_point_1[1]-32)):
                                    new_line = Actor('wiresgreenver',(wires_point_1[0], wires_point_1[1]-16))
                        try:
                            if build_structure.image == "wrench":
                                temp = True
                                for i in range(len(all_wires)):
                                    if new_line.pos == all_wires[i].pos:
                                        temp = False
                                        break
                                if temp == True and build_structure.energy <= energy:
                                    all_wires.append(new_line)
                                    energy -= build_structure.energy
                            else:
                                for i in range(len(all_wires)):
                                    if new_line.pos == all_wires[i].pos:
                                        all_wires.pop(i)
                                        break
                        except:
                            pass

                        # if wires_point_1[0] > wires_point_2[0]:
                        #     all_wires.append(Actor('wiresgreenhor',(wires_point_1[0]-16, wires_point_1[1])))
                        # elif wires_point_1[0] < wires_point_2[0]:
                        #     all_wires.append(Actor('wiresgreenhor',(wires_point_1[0]+16, wires_point_1[1])))

                        # elif wires_point_1[1] > wires_point_2[1]:
                        #     all_wires.append(Actor('wiresgreenver',(wires_point_1[0], wires_point_1[1]-16)))
                        # elif wires_point_1[1] < wires_point_2[1]:
                        #     all_wires.append(Actor('wiresgreenver',(wires_point_1[0], wires_point_1[1]+16)))

                        wires_point_1 = -1
                        wires_point_2 = -1

                elif rock_texture_grid.image == "rocktexturebuild":
                    placed_objects.append(Actor(build_structure.image,rock_texture_grid.pos))
                    build_menu = False
                    energy -= build_structure.energy

                    if build_structure.image == "batterygreen":
                        placed_objects[-1].energy = 100
                        clock.schedule_interval(heat_increase, 10)

                    if build_structure.image == "energyboxgreen":
                        max_energy += 100
                        clock.schedule_interval(heat_increase, 30)

                    if build_structure.image == "solarpanel":
                        clock.schedule_interval(energy_increase, 2)
                        clock.schedule_interval(heat_increase, 15)

                    if build_structure.image == "circutgreen":
                        research_faster += 4
                        clock.schedule_interval(heat_increase, 4)
                        clock.schedule_interval(energy_decrease, 10)

            else:
                build_menu = False
        if bin.collidepoint(pos):
            build_menu = False
            draw_wire_line = False

        for i in range(len(move_inventory_list)):
            if move_inventory_list[i].collidepoint(pos):
                build_menu = True
                wires_point_1 = -1
                wires_point_2 = -1
                rock_texture_grid.image = "rocktexturebuildred"
                build_structure.image = move_inventory_list[i].image
                build_structure.energy = move_inventory_list[i].energy

def on_mouse_move(pos):
    global build_menu, box_size, wires_point_1, wires_point_2, draw_wire_line, wires_2_cords, allow_wires_build

    allow_wires_build = True
    if wires_point_1 != -1 and wires_point_2 == -1 and build_menu == True and allow_wires_build == True:
        #screen.draw.filled_rect(Rect(wires_point_1, pos), (0,0,0))
        draw_wire_line = True
        wires_2_cords = pos
    else:
        draw_wire_line = False
        wires_2_cords = -1

    if build_menu == True:
        build_structure.pos = pos
        rock_texture_grid.top = box_size * (pos[1] // box_size)
        rock_texture_grid.left = box_size * (pos[0] // box_size)
        for i in range (len(placed_objects)):
            if placed_objects[i].pos == rock_texture_grid.pos:
                rock_texture_grid.image = rock_texture_grid_red.image
                break
        else:
            rock_texture_grid.image = "rocktexturebuild"
            build_menu = True
        if rock_texture_grid.y > HEIGHT - 3 * box_size:
            rock_texture_grid.image = rock_texture_grid_red.image
            allow_wires_build = False
        if generator_green.collidepoint(pos):
            rock_texture_grid.image = "rocktexturebuildred"
            allow_wires_build = False
        if bin.collidepoint(pos):
            rock_texture_grid.image = "rocktexturebuildred"
            allow_wires_build = False

def check_wires(point):
    if point[1] > HEIGHT - 3 * box_size:
        return False
    if generator_green.collidepoint(point):
        return False
    if bin.collidepoint(point):
        return False
    return True




pgzrun.go()


# TO DO!

# add asteroids/virus
# change images
# make the bin move with ur mouse on click
# WRENCH - instead of wires there is 2 wrench 1 deletes wires other creates wires
# no green cirst add circut only at blue level
#