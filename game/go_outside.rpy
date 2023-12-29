label go_oustide:

    scene bg house front

    show protagonist neutral at right

    "Thinking about the latest days, everything feels unreal"
    "Maybe taking a breath outside helps a little"

    p "What if I say I don´t have time for this?"
    p "I can do all the paperwork with my lawyer anyway"
    
    "Leaving this house behind is no trouble for you"
    "It´s sad to lose a realtive but this time you have to put yourself together and take a step foward"
    show protagonist opened eyes at center
    menu:
        "My best option is...:"
        "Walk away and leave everything to the lawyer":

            p "Yes, telling my family that my lawyer has everything might be the best option. They can negociate everything with her"
            

        "Call and tell your cousin you found the certificates":
            show protagonist closed eyes  at center 
            p "I should be more considerate about this. It´s a rough time for us"
            show protagonist neutral at center
            "After calling and telling about your day in the house they tell you:"
            "We were thinking about all the rent stuff and came to our mind"
            "Can you please give us your part of the house?"
            "That would made us a little bit happier in this storm"
            show protagonist opened eyes
            p "Of course If you buy it, that´s how it works right?"
            show protagonist neutral
            "Oh no dear! We are family, that doesn´t need to be that way"
            show protagonist smiles
            p "Sorry, I need to think about it"
            show protagonist opened eyes
            "You will be calmer in no time, but today in particular is a headache"

            "Let´s go home and think about it later"

            jump protagonist_home

        
        "...Do I really care about this?":

            p "No"
            
            show protagonist closed eyes

            p "I can´t remember a nice memory with him. With him alone"

            show protagonist opened eyes

            p "With my cousins or his wife maybe, but not with him"
            p "My condolences to my relatives, they were closer and it hurts"
            
            "Losing someone is the world falling apart and you go with it, you know it very well"

            p "Staying with them until the paperwork ends seems fine, in that time I can give a hand with everything left"
            p "After that I would like to leave, life is rough and moving foward it´s the best for me"

            "Is this the best option? You don´t really know"
            "You will find it out in the next years"
            