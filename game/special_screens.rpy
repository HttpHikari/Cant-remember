#necesitas un call screen hoverable_image para activar esto
screen hoverable_image:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.28
        idle "unhovered cat.jpg"
        hover "hover cat.jpg"
        action [Hide("displayTextScreen"),Jump("livingroom")]

        hovered Show("displayTextScreen", displayText = "Hovered!")
        unhovered Hide("displayTextScreen")

screen displayTextScreen:
    default displayText = ""
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            text displayText



screen multiple_hoverable_image:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.28
        idle "unhovered cat.jpg"
        hover "hover cat.jpg"
        action [Hide("displayTextScreen"),Jump("livingroom")]

        hovered Show("displayTextScreen", displayText = "Hovered!")
        unhovered Hide("displayTextScreen")
    imagebutton:
        xanchor 1.5
        yanchor 0.5
        xpos 0.5
        ypos 0.28
        idle "unhovered cat.jpg"
        hover "hover cat.jpg"
        action [Hide("displayTextScreen"),Jump("livingroom")]

        hovered Show("displayTextScreen", displayText = "Hovered!")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xanchor -0.5
        yanchor -0.75
        xpos 0.5
        ypos 0.28
        idle "unhovered cat.jpg"
        hover "hover cat.jpg"
        action [Hide("displayTextScreen"),Jump("livingroom")]

        hovered Show("displayTextScreen", displayText = "Hovered!")
        unhovered Hide("displayTextScreen")


screen hoverable_wardrobe:
    imagebutton:
        xanchor 0
        yanchor 0
        xpos 1000
        ypos 470
        idle "cloth unhover.png"
        hover "cloth hovered.png"
        action [Hide("displayTextScreen"),Jump("hanging_clothes")]

        hovered Show("displayTextScreen", displayText = "Check hanging clothes")
        unhovered Hide("displayTextScreen")
    
    imagebutton:
        xanchor 1
        yanchor 0.5
        xpos 0.5
        ypos 0.28
        idle "shoebox_unhover"
        hover "shoebox_hovered"
        action [Hide("displayTextScreen"),Jump("shoeboxes")]

        hovered Show("displayTextScreen", displayText = "Check shoe boxes")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 1320
        ypos 750
        idle "drawer unhover.png"
        hover "drawer hovered.png"
        action [Hide("displayTextScreen"),Jump("drawer")]

        hovered Show("displayTextScreen", displayText = "Check drawers")
        unhovered Hide("displayTextScreen")
