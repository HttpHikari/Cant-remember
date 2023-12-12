define p = Character("protagonist", who_color="#494f9b")
define t = Character("taxidriver", who_color="#9b6349")

label start:

#play music "sunflower-slow-drag.ogg" fadeout 1
 
    scene bg taxi back
    with fade
    "You've been traveling in a taxi for 15 minutes and you still haven't reached your destination."

    show protagonist neutral at right

    p "I don't wanna think how much the trip is gonna be"

    show taxidriver at left

    t "It will be $150"
    p "Thank you, here is the total, check it to be sure"
    t "You are welcome" 

#stop music fadeout 1
 
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

    "Check phone":
        show phone:
            xalign 0.5
            yalign 0.5
        "I almost forgot to tell Olie I am already here"

label enter_house:

    scene bg house livingroom

    "At first glance when you enter you can see dust everywhere, but still tidy, still in those past days."

    show protagonist closed eyes at right
    show protagonist opened eyes at right
  
    "Since you have some time, take the opportunity to look around the place a little."

    show protagonist neutral at right

label livingroom:
    menu:
        "Let´s see:"
        "The centerpiece":

            p "I remember the days my aunt told me and my cousins to not touch this thing"
            p "now I look at this and it's just a glass bowl with shiny rocks, nothing interesting anymore"
            jump livingroom
        
        "The pictures on the wall":

            p "Lots of nice memories frozen, some of them I can't recognize, parts of the family I didn't get to know"
            jump livingroom

        "The showcase": 

            p "Cat shaped souvenirs from different cities around the world."
            p "There are in so many colors and styles."

            show protagonist smiles at right

            p "These in particular make you smile."

label room_choice:
    show protagonist opened eyes at right
    "After having some time to organize your thoughts"
    "you decide it's time to look around the documents you have to get."

    p "Well even if I didn´t know him very well, I have the hunch he was the kind of old man who kept money under the couch and jewelry in a cardbox"
    p "Old man stuff"

    menu:
        "Where should I go first?"
        "Bedroom":
            scene bg bedroom

            "The old curtains once white, now brown cause of the dust and humidity."
            "Those worn walls."

            show protagonist neutral at right

            p "That little blue room"
            p "Even after all these years, you are surprised how that nickname still sticks in your head."

            p "no need to investigate a lot here, I guess I know where to search"
            
            p "If you were someone closer to him, you might understand all the pictures and history this little place has to tell."
            show protagonist closed eyes at right
            p "But you aren't."
            show protagonist opened eyes at right
            "Let's look in the wardrobe."

            scene bg wardrobe
            label hoverable_wardrobe:
                call screen hoverable_wardrobe
            label hanging_clothes:
                "You go through hanger to hanger inspecting all the pockets of each cloth."
                "You find a small wallet, with only the essentials."

                p "Two expired credit cards, some cash and an ID"
                p "It seems to be the most recent one, this should work"
                p "Now, where is the Birth Certificate?"
                jump hoverable_wardrobe

            label shoeboxes:
                "There are shoe boxes piled at the bottom of the wardrobe."
                "Most of them have their right pair of shoes, others have pictures."

                p "Aaand it's here"
                p "Those were the essentials to start the legal procedure"

                "Nothing good comes from personal interest and wanting money between the family, but you are on the road now."

                p "Whatever gets me out of these conflicts, this isn't even beneficial for me"
                p "The costs of the lawyer is almost the same amount of my heirloom"

                "sighs"
                jump hoverable_wardrobe

            label drawer:
                "Lots of trinkets, nothing of interest here."
                jump hoverable_wardrobe

        "Kitchen":
            jump room_choice

        "Go outside":
            jump room_choice

            "Now i can go"















