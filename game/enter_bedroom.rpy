label enter_bedroom:

    scene bg bedroom

    "The old curtains once white, now brown cause of the dust and humidity."
    "Those worn walls."

    show protagonist neutral at right

    p "That little blue room"
    p "Even after all these years, you are surprised how that nickname still sticks in your head."

    p "No need to investigate a lot here, I guess I know where to search"
            
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
        p "I should check the kitchen..."

        jump enter_kitchen
    
    label drawer:
        "Lots of trinkets, nothing of interest here."
        jump hoverable_wardrobe

        "*sighs*"

        