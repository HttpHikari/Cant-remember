﻿define p = Character("protagonist", who_color="#494f9b")
define t = Character("taxidriver", who_color="#9b6349")

define true_points = 0
define void_points = 0
define neutral_points = 0

label start:

    play music "Past sadness.ogg" volume 0.5 fadeout 1
 
    scene bg taxi back
    with fade
    "You've been traveling in a taxi for 15 minutes and you still haven't reached your destination."

    show protagonist neutral at right

    p "I don't wanna think how much the trip is gonna be"

    show taxidriver at left

    t "It will be $4300"
    p "Thank you, here is the total, check it to be sure"
    t "It´s ok, you´re welcome" 
 
    hide taxidriver
label house_outside:

    "When you get out of the car, the weight of the memories falls on you."
    "You didn't think the passage of time would be like this"
    
    scene bg house front
    show protagonist neutral at right

    p "Well, I need to be sure I have everything on hand"

    show protagonist opened eyes at right
menu:
    "What should i do?"
    "Check keys":
        show keys:
            xalign 0.5
            yalign 0.5
        "Yes, I have both of my keys and the “sweet home” keys"
        jump enter_house

    "Check phone":
        show phone:
            xalign 0.5
            yalign 0.5
        "I almost forgot to tell Olie I am already here"
        jump enter_house

label livingroom:
    menu:
        "Let´s see:"
        "The centerpiece":
            show protagonist opened eyes at center
            p "I remember the days my aunt told me and my cousins to not touch this thing"
            p "now I look at this and it's just a glass bowl with shiny rocks, nothing interesting anymore"
            jump livingroom
        
        "The pictures on the wall":
            show protagonist opened eyes at center
            p "Lots of nice memories frozen, some of them I can't recognize, parts of the family I didn't get to know"
            jump livingroom

        "The showcase": 

            show cat 1:
                xalign 0.5
                yalign 0.5
            p "Cat shaped souvenirs from different cities around the world."
            show cat 2:
                xalign 0.5
                yalign 0.5
            p "There are in so many colors and styles."
            show cat 3:
                xalign 0.5
                yalign 0.5

            show protagonist smiles at right

            p "These in particular make you smile."

label room_choice:

    scene bg house livingroom
    stop music fadeout 1
    show protagonist opened eyes at right
    "After having some time to organize your thoughts"
    "you decide it's time to look around the documents you have to get."

    p "Well even if I didn´t know him very well, I have the hunch he was the kind of old man who kept money under the couch and jewelry in a cardbox"
    p "Old man stuff"

    menu:
        "Where should I go?"
        "Bedroom":
            jump enter_bedroom

            label drawer:
                "Lots of trinkets, nothing of interest here."
                jump hoverable_wardrobe

        "Kitchen":
            jump enter_kitchen

        "Go outside":
            jump go_oustide















