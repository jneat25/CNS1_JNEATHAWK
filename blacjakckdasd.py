confirm21 = input("Welcome to 21 would you like to play? ")
chips = 1000
while (confirm21 == "yes" or confirm21 == "Yes"):
    import os
    os.system("cls")
    import random
    card1 = random.randint(1,11)
    card2 = random.randint(1,11)
    dealer1 = random.randint(1,11)
    dealer2 = random.randint(1,11)
    print ("you have",chips," chips")
    chipbet = int(input("How much would you like to bet? "))
    print ("you have a",card1,"and a",card2,"totaling to a",card1 + card2,"")
    print ("the dealer has a",dealer1,)
    choice21_1 = input ("Would you like to Hit, Double, Surrender, or Stand? ")
    if (choice21_1 == "Hit" or choice21_1 == "hit"):
        card3 = random.randint(1,11)
        print ("You drew a",card3,"totaling your hand to",card1 + card2 + card3,"")
        if (card1 + card2 + card3 > 21):
            print ("You busted! Game over.")
            print ("You lost",chipbet,"sucks to suck")
            chips = chips - chipbet
            confirm21 = input("Would you like to play again? ")
        else:
            choice21_2 = input("Would you like to Hit or Stand? ")
            if (choice21_2 == "Hit" or choice21_2 == "hit"):
                card4 = random.randint(1,11)
                print ("You drew a",card4,"totaling your hand to",card1 + card2 + card3 + card4,"")
                if (card1 + card2 + card3 + card4> 21):
                    print ("You busted! Game over.")
                    print ("You lost",chipbet,"sucks to suck")
                    chips = chips - chipbet
                    confirm21 = input("Would you like to play again? ")
                else:
                    choice21_3 = input("Would you like to Hit or Stand?")
                    if (choice21_3 == "Hit" or choice21_3 == "hit"):
                        card5 = random.randint(1,11)
                        print ("You drew a",card5,"totaling your hand to",card1 + card2 + card3 + card4 +card5,"")
                        if (card1 + card2 + card3 + card4 + card5 > 21):
                            print ("You busted! Gamer over.")
                            print ("You lost",chipbet,"sucks to suck")
                            chips = chips - chipbet
                            confirm21 = input("Would you like to play again? ")
                        else:
                            print("You ended with a",card1,"and",card2,"and",card3,"and",card4,"and",card5,"totaling to",card1 + card2 + card3 + card4 + card5,"")
                            print("The dealer has a",dealer1,"and a",dealer2,"totaling to",dealer1 + dealer2,"")
                            if (dealer1 + dealer2 < card1 + card2 + card3 + card4 + card5):
                                dealer4_3 = random.randint(1,11)
                                print ("The dealer delt a",dealer4_3,"totaling to",dealer1 + dealer2 + dealer4_3,"")
                                if (dealer1 + dealer2 + dealer4_3 < card1 + card2 + card3 + card4 + card5):
                                    dealer4_4 = random.randint(1,11)
                                    print ("The dealer delt a",dealer4_4,"totaling to",dealer1 + dealer2 + dealer4_3 + dealer4_4,"")
                                    if (dealer1 + dealer2 + dealer4_3 + dealer4_4 < card1 + card2 + card3 + card4 + card5):
                                        dealer4_5 = random.randint(1,11)
                                        print ("The dealer delt a",dealer4_5,"totaling to",dealer1 + dealer2 + dealer4_3 + dealer4_4 + dealer4_5,"")
                                        if (dealer1 + dealer2 + dealer4_3 + dealer4_4 + dealer4_5 < card1 + card2 + card3 + card4 + card5):
                                            print("The dealer cannot get anymore cards")
                                        else:
                                            if (dealer1 + dealer2 + dealer4_3 + dealer4_4 + dealer4_5> 21):
                                                print("The dealer busted! You win")
                                                print ("You win",chipbet,"good job!")
                                                chips = chips + chipbet
                                                confirm21 = input("Would you like to play again? ")
                                            else:
                                                if (dealer1 + dealer2 + dealer4_3 + dealer4_4 + dealer4_5 > card1 + card2 + card3 + card4 + card5):
                                                    print("The dealer wins!")
                                                    print ("You lost",chipbet,"sucks to suck")
                                                    chips = chips - chipbet
                                                    confirm21 = input("Would you like to play again? ")
                                                if (dealer1 + dealer2 + dealer4_3 + dealer4_4 + dealer4_5 < card1 + card2 + card3 + card4 + card5):
                                                    print("The player wins!")
                                                    print ("You win",chipbet,"good job!")
                                                    chips = chips + chipbet
                                                    confirm21 = input("Would you like to play again? ")
                                                if (dealer1 + dealer2 + dealer4_3 + dealer4_4 + dealer4_5 == card1 + card2 + card3 + card4 + card5):
                                                    print("The dealer and player tied, the bet is pushed")
                                                    confirm21 = input("Would you like to play again? ")
                                    else:   
                                        if(dealer1 + dealer2 + dealer4_3 + dealer4_4 > 21):
                                            print("The dealer busted! You win")
                                            print ("You win",chipbet,"good job!")
                                            chips = chips + chipbet
                                            confirm21 = input("Would you like to play again? ")
                                        else:
                                            if (dealer1 + dealer2 + dealer4_3 + dealer4_4 > card1 + card2 + card3 + card4 + card5):
                                                print("The dealer wins!")
                                                print ("You lost",chipbet,"sucks to suck")
                                                chips = chips - chipbet
                                                confirm21 = input("Would you like to play again? ")
                                            if (dealer1 + dealer2 + dealer4_3 + dealer4_4 < card1 + card2 + card3 + card4 + card5):
                                                print("The player wins!")
                                                print ("You win",chipbet,"good job!")
                                                chips = chips + chipbet
                                                confirm21 = input("Would you like to play again? ")
                                            if (dealer1 + dealer2 + dealer4_3 + dealer4_4 == card1 + card2 + card3 + card4 + card5):
                                                print("The dealer and player tied, the bet is pushed")
                                                confirm21 = input("Would you like to play again? ")
                                else:                
                                    if (dealer1 + dealer2 + dealer4_3 > 21):
                                        print("The dealer busted! You win")
                                        print ("You win",chipbet,"good job!")
                                        chips = chips + chipbet
                                        confirm21 = input("Would you like to play again? ")
                                    else:
                                        if (dealer1 + dealer2 + dealer4_3 > card1 + card2 + card3 + card4 + card5):
                                            print("The dealer wins!")
                                            confirm21 = input("Would you like to play again? ")
                                            print ("You lose",chipbet,"sucks to suck")
                                            chips = chips - chipbet     
                                        if (dealer1 + dealer2 + dealer4_3 < card1 + card2 + card3 + card4 + card5):
                                            print("The player wins!")
                                            print ("You win",chipbet,"good job!")
                                            chips = chips + chipbet
                                            confirm21 = input("Would you like to play again? ")
                                        if (dealer1 + dealer2 + dealer4_3 == card1 + card2 + card3 + card4 + card5):
                                            print("The dealer and player tied, the bet is pushed")
                                            confirm21 = input("Would you like to play again? ")
                            else:
                                if(dealer1 + dealer2 > card1 + card2 + card3 + card4 + card5):
                                    print("The dealer wins!")
                                    print ("You lost",chipbet,"sucks to suck")
                                    chips = chips - chipbet
                                    confirm21 = input("Would you like to play again? ")
                                if(dealer1 + dealer2 < card1 + card2 + card3 + card4 + card5):
                                    print("The player wins!")
                                    print ("You win",chipbet,"good job!")
                                    chips = chips + chipbet
                                    confirm21 = input("Would you like to play again? ")
                                if (dealer1 + dealer2 == card1 + card2 + card3 + card4 + card5):
                                    print("The dealer and player tied, the bet is pushed")
                                    confirm21 = input("Would you like to play again? ")
                    if (choice21_3 == "Stand" or choice21_3 == "stand"):
                        print ("You stood with a",card1,"and",card2,"and",card3 ,"and",card4,"totaling to",card1 + card2 + card3 + card4,"")
                        print ("The dealer has a",dealer1,"and a",dealer2,"totaling to",dealer1 + dealer2,"")
                        if (dealer1 + dealer2 < card1 + card2 + card3 + card4):
                            dealer3_3 = random.randint(1,11)
                            print ("The dealer delt a",dealer3_3,"totaling to",dealer1 + dealer2 + dealer3_3,"")
                            if (dealer1 + dealer2 + dealer3_3 < card1 + card2 + card3 + card4):
                                dealer3_4 = random.randint(1,11)
                                print ("The dealer delt a",dealer3_4,"totaling to",dealer1 + dealer2 + dealer3_3 + dealer3_4,"")
                                if (dealer1 + dealer2 + dealer3_3 + dealer3_4 < card1 + card2 + card3 + card4):
                                    dealer3_5 = random.randint(1,11)
                                    print ("The dealer delt a",dealer3_5,"totaling to",dealer1 + dealer2 + dealer3_3 + dealer3_4 + dealer3_5,"")
                                    if (dealer1 + dealer2 + dealer3_3 + dealer3_4 + dealer3_5 < card1 + card2 + card3 + card4):
                                        print("The dealer cannot get anymore cards")
                                    else:
                                        if (dealer1 + dealer2 + dealer3_3 + dealer3_4 + dealer3_5> 21):
                                            print("The dealer busted! You win")
                                            print ("You win",chipbet,"good job!")
                                            chips = chips + chipbet
                                            confirm21 = input("Would you like to play again? ")
                                        else:
                                            if (dealer1 + dealer2 + dealer3_3 + dealer3_4 + dealer3_5 > card1 + card2 + card3 + card4):
                                                print("The dealer wins!")
                                                print ("You lost",chipbet,"sucks to suck")
                                                chips = chips - chipbet
                                                confirm21 = input("Would you like to play again? ")
                                            if (dealer1 + dealer2 + dealer3_3 + dealer3_4 + dealer3_5 < card1 + card2 + card3 + card4):
                                                print("The player wins!")
                                                print ("You win",chipbet,"good job!")
                                                chips = chips + chipbet
                                                confirm21 = input("Would you like to play again? ")
                                            if (dealer1 + dealer2 + dealer3_3 + dealer3_4 + dealer3_5 == card1 + card2 + card3 + card4):
                                                print("The dealer and player tied, the bet is pushed")
                                                confirm21 = input("Would you like to play again ?")
                                else:   
                                    if(dealer1 + dealer2 + dealer3_3 + dealer3_4 > 21):
                                        print("The dealer busted! You win")
                                        print ("You win",chipbet,"good job!")
                                        chips = chips + chipbet
                                        confirm21 = input("Would you like to play again? ")
                                    else:
                                        if (dealer1 + dealer2 + dealer3_3 + dealer3_4 > card1 + card2 + card3 + card4):
                                            print("The dealer wins!")
                                            print ("You lost",chipbet,"sucks to suck")
                                            chips = chips - chipbet
                                            confirm21 = input("Would you like to play again? ")
                                        if (dealer1 + dealer2 + dealer3_3 + dealer3_4 < card1 + card2 + card3 + card4):
                                            print("The player wins!")
                                            print ("You win",chipbet,"good job!")
                                            chips = chips + chipbet
                                            confirm21 = input("Would you like to play again? ")
                                        if (dealer1 + dealer2 + dealer3_3 + dealer3_4 == card1 + card2 + card3 + card4):
                                            print("The dealer and player tied, the bet is pushed")
                                            confirm21 = input("Would you like to play again? ")
                            else:                
                                if (dealer1 + dealer2 + dealer3_3 > 21):
                                    print("The dealer busted! You win")
                                    print ("You win",chipbet,"good job!")
                                    chips = chips + chipbet
                                    confirm21 = input("Would you like to play again? ")
                                else:
                                    if (dealer1 + dealer2 + dealer3_3 > card1 + card2 + card3 + card4):
                                        print("The dealer wins!")
                                        print ("You lost",chipbet,"sucks to suck")
                                        chips = chips - chipbet
                                        confirm21 = input("Would you like to play again? ")
                                    if (dealer1 + dealer2 + dealer3_3 < card1 + card2 + card3 + card4):
                                        print("The player wins!")
                                        print ("You win",chipbet,"good job!")
                                        chips = chips + chipbet
                                        confirm21 = input("Would you like to play again? ")
                                    if (dealer1 + dealer2 + dealer3_3 == card1 + card2 + card3 + card4):
                                        print("The dealer and player tied, the bet is pushed")
                                        confirm21 = input("Would you like to play again? ")
                        else:
                            if(dealer1 + dealer2 > card1 + card2 + card3 + card4):
                                print("The dealer wins!")
                                print ("You lost",chipbet,"sucks to suck")
                                chips = chips - chipbet
                                confirm21 = input("Would you like to play again? ")
                            if(dealer1 + dealer2 < card1 + card2 + card3 + card4):
                                print("The player wins!")
                                print ("You win",chipbet,"good job!")
                                chips = chips + chipbet
                                confirm21 = input("Would you like to play again? ")
                            if (dealer1 + dealer2 == card1 + card2 + card3 + card4):
                                print("The dealer and player tied, the bet is pushed")
                                confirm21 = input("Would you like to play again? ")
            if (choice21_2 == "Stand" or choice21_2 == "stand"):
                print ("You stood with a",card1,"and",card2,"and",card3,"totaling to",card1 + card2 + card3,"")
                print ("The dealer has a",dealer1,"and a",dealer2,"totaling to",dealer1 + dealer2,"")
                if (dealer1 + dealer2 < card1 + card2 + card3):
                    dealer2_3 = random.randint(1,11)
                    print ("The dealer delt a",dealer2_3,"totaling to",dealer1 + dealer2 + dealer2_3,"")
                    if (dealer1 + dealer2 + dealer2_3 < card1 + card2 + card3):
                        dealer2_4 = random.randint(1,11)
                        print ("The dealer delt a",dealer2_4,"totaling to",dealer1 + dealer2 + dealer2_3 + dealer2_4,"")
                        if (dealer1 + dealer2 + dealer2_3 + dealer2_4 < card1 + card2 + card3):
                            dealer2_5 = random.randint(1,11)
                            print ("The dealer delt a",dealer2_5,"totaling to",dealer1 + dealer2 + dealer2_3 + dealer2_4 + dealer2_5,"")
                            if (dealer1 + dealer2 + dealer2_3 + dealer2_4 + dealer2_5 < card1 + card2 + card3):
                                print("The dealer cannot get anymore cards")
                            else:
                                if (dealer1 + dealer2 + dealer2_3 + dealer2_4 + dealer2_5> 21):
                                 print("The dealer busted! You win")
                                 print ("You win",chipbet,"good job!")
                                 chips = chips - chipbet
                                 confirm21 = input("Would you like to play again? ")
                                else:
                                    if (dealer1 + dealer2 + dealer2_3 + dealer2_4 + dealer2_5 > card1 + card2 + card3):
                                        print("The dealer wins!")
                                        print ("You lose",chipbet,"sucks to suck")
                                        chips = chips - chipbet
                                        confirm21 = input("Would you like to play again? ")
                                    if (dealer1 + dealer2 + dealer2_3 + dealer2_4 + dealer2_5 < card1 + card2 + card3):
                                        print("The player wins!")
                                        print ("You win",chipbet,"good job!")
                                        chips = chips + chipbet
                                        confirm21 = input("Would you like to play again? ")
                                    if (dealer1 + dealer2 + dealer2_3 + dealer2_4 + dealer2_5 == card1 + card2 + card3):
                                        print("The dealer and player tied, the bet is pushed")
                                        confirm21 = input("Would you like to play again? ")
                        else:   
                            if(dealer1 + dealer2 + dealer2_3 + dealer2_4 > 21):
                                print("The dealer busted! You win")
                                print ("You win",chipbet,"good job!")
                                chips = chips + chipbet
                                confirm21 = input("Would you like to play again? ")
                            else:
                                if (dealer1 + dealer2 + dealer2_3 + dealer2_4 > card1 + card2 + card3):
                                    print("The dealer wins!")
                                    print ("You lose",chipbet,"sucks to suck")
                                    chips = chips - chipbet
                                    confirm21 = input("Would you like to play again? ")
                                if (dealer1 + dealer2 + dealer2_3 + dealer2_4 < card1 + card2 + card3):
                                    print("The player wins!")
                                    print ("You win",chipbet,"good job!")
                                    chips = chips + chipbet
                                    confirm21 = input("Would you like to play again? ")
                                if (dealer1 + dealer2 + dealer2_3 + dealer2_4 == card1 + card2 + card3):
                                    print("The dealer and player tied, the bet is pushed")
                                    confirm21 = input("Would you like to play again? ")
                    else:                
                        if (dealer1 + dealer2 + dealer2_3 > 21):
                            print("The dealer busted! You win")
                            print ("You win",chipbet,"good job!")
                            chips = chips + chipbet
                            confirm21 = input("Would you like to play again? ")
                        else:
                            if (dealer1 + dealer2 + dealer2_3 > card1 + card2 + card3):
                                print("The dealer wins!")
                                print ("You lose",chipbet,"sucks to suck")
                                chips = chips - chipbet
                                confirm21 = input("Would you like to play again? ")
                            if (dealer1 + dealer2 + dealer2_3 < card1 + card2 + card3):
                                print("The player wins!")
                                print ("You win",chipbet,"good job!")
                                chips = chips + chipbet
                                confirm21 = input("Would you like to play again? ")
                            if (dealer1 + dealer2 + dealer2_3 == card1 + card2 + card3):
                                print("The dealer and player tied, the bet is pushed")
                                confirm21 = input("Would you like to play again? ")
                else:
                    if(dealer1 + dealer2 > card1 + card2 + card3):
                        print("The dealer wins!")
                        print ("You lose",chipbet,"sucks to suck")
                        chips = chips - chipbet
                        confirm21 = input("Would you like to play again? ")
                    if(dealer1 + dealer2 < card1 + card2 + card3):
                        print("The player wins!")
                        print ("You win",chipbet,"good job!")
                        chips = chips + chipbet
                        confirm21 = input("Would you like to play again? ")
                    if (dealer1 + dealer2 == card1 + card2 + card3):
                        print("The dealer and player tied, the bet is pushed")
                        confirm21 = input("Would you like to play again? ")
    if (choice21_1 == "Stand" or choice21_1 == "stand"):
        print ("You stood with a",card1,"and a",card2,"totaling to",card1 + card2,"")
        print ("The dealer has a",dealer1,"and a",dealer2,"totaling to",dealer1 + dealer2,"")
        if (dealer1 + dealer2 < card1 + card2):
             dealer1_3 = random.randint(1,11)
             print ("The dealer delt a",dealer1_3,"totaling to",dealer1 + dealer2 + dealer1_3,"")
             if (dealer1 + dealer2 + dealer1_3 < card1 + card2):
                dealer1_4 = random.randint(1,11)
                print ("The dealer delt a",dealer1_4,"totaling to",dealer1 + dealer2 + dealer1_3 + dealer1_4,"")
                if (dealer1 + dealer2 + dealer1_3 + dealer1_4 < card1 + card2):
                 dealer1_5 = random.randint(1,11)
                 print ("The dealer delt a",dealer1_5,"totaling to",dealer1 + dealer2 + dealer1_3 + dealer1_4 + dealer1_5,"")
                 if (dealer1 + dealer2 + dealer1_3 + dealer1_4 + dealer1_5 < card1 + card2):
                     print("The dealer cannot get anymore cards")
                 else:
                     if (dealer1 + dealer2 + dealer1_3 + dealer1_4 + dealer1_5> 21):
                        print("The dealer busted! You win")
                        print ("You win",chipbet,"good job!")
                        chips = chips + chipbet
                        confirm21 = input("Would you like to play again? ")
                     else:
                        if (dealer1 + dealer2 + dealer1_3 + dealer1_4 + dealer1_5 > card1 + card2):
                            print("The dealer wins!")
                            print ("You lose",chipbet,"sucks to suck")
                            chips = chips - chipbet
                            confirm21 = input("Would you like to play again? ")
                        if (dealer1 + dealer2 + dealer1_3 + dealer1_4 + dealer1_5 < card1 + card2):
                            print("The player wins!")
                            print ("You win",chipbet,"goodjob!")
                            chips = chips + chipbet
                            confirm21 = input("Would you like to play again? ")
                        if (dealer1 + dealer2 + dealer1_3 + dealer1_4 + dealer1_5 == card1 + card2):
                            print("The dealer and player tied, the bet is pushed")
                            confirm21 = input("Would you like to play again? ")

                else:
                    if(dealer1 + dealer2 + dealer1_3 + dealer1_4 > 21):
                        print("The dealer busted! You win")
                        print ("You win",chipbet,"good job!")
                        chips = chips + chipbet
                        confirm21 = input("Would you like to play again? ")
                    else:
                        if (dealer1 + dealer2 + dealer1_3 + dealer1_4 > card1 + card2):
                            print("The dealer wins!")
                            print ("You lose",chipbet,"sucks to suck")
                            chips = chips - chipbet
                            confirm21 = input("Would you like to play again? ")
                        if (dealer1 + dealer2 + dealer1_3 + dealer1_4 < card1 + card2):
                            print("The player wins!")
                            print ("You win",chipbet,"good job!")
                            chips = chips + chipbet
                            confirm21 = input("Would you like to play again? ")
                        if (dealer1 + dealer2 + dealer1_3 + dealer1_4 == card1 + card2):
                            print("The dealer and player tied, the bet is pushed")
                            confirm21 = input("Would you like to play again? ")
             else:                
                if (dealer1 + dealer2 + dealer1_3 > 21):
                    print("The dealer busted! You win")
                    print ("You win",chipbet,"good job!")
                    chips = chips + chipbet
                    confirm21 = input("Would you like to play again? ")
                else:
                    if (dealer1 + dealer2 + dealer1_3 > card1 + card2):
                        print("The dealer wins!")
                        print ("You lose",chipbet,"sucks to suck")
                        chips = chips - chipbet
                        confirm21 = input("Would you like to play again? ")
                    if (dealer1 + dealer2 + dealer1_3 < card1 + card2):
                        print("The player wins!")
                        print ("You win",chipbet,"good job!")
                        chips = chips + chipbet
                        confirm21 = input("Would you like to play again? ")
                    if (dealer1 + dealer2 + dealer1_3 == card1 + card2):
                        print("The dealer and player tied, the bet is pushed")
                        confirm21 = input("Would you like to play again? ")

        else:
            if(dealer1 + dealer2 > card1 + card2):
                print("The dealer wins!")
                print ("You lose",chipbet,"sucks to suck")
                chips = chips - chipbet
                confirm21 = input("Would you like to play again? ")
            if(dealer1 + dealer2 < card1 + card2):
                print("The player wins!")
                print ("You win",chipbet,"good job!")
                chips = chips + chipbet
                confirm21 = input("Would you like to play again? ")
            if (dealer1 + dealer2 == card1 + card2):
                print("The dealer and player tied, the bet is pushed")
                confirm21 = input("Would you like to play again? ")
    if (choice21_1  == "Surrender" or choice21_1 == "surrender"):
        print ("You surrendered and forfeited half of your bet")
        chips = chips - (chipbet/2)
        confirm21 = input("Would you like to play again? ")
    if (choice21_1 == "Double" or choice21_1 == "double"):
        print("You just doubled your bet")
        dcard3 = random.randint(1,11)
        print ("You drew a",dcard3,"totaling your hand to",card1 + card2 + dcard3,"")
        if (card1 + card2 + dcard3 > 21):
            print ("You busted! Game over.")
            print ("You lost",chipbet * 2,"sucks to suck")
            chips = chips - (chipbet *2)
            confirm21 = input("Would you like to play again? ")
        if (dealer1 + dealer2 < card1 + card2 + dcard3):
             dealerd_3 = random.randint(1,11)
             print ("The dealer delt a",dealerd_3,"totaling to",dealer1 + dealer2 + dealerd_3,"")
             if (dealer1 + dealer2 + dealerd_3 < card1 + card2 + dcard3):
                dealerd_4 = random.randint(1,11)
                print ("The dealer delt a",dealerd_4,"totaling to",dealer1 + dealer2 + dealerd_3 + dealerd_4,"")
                if (dealer1 + dealer2 + dealerd_3 + dealerd_4 < card1 + card2 + dcard3):
                 dealerd_5 = random.randint(1,11)
                 print ("The dealer delt a",dealerd_5,"totaling to",dealer1 + dealer2 + dealerd_3 + dealerd_4 + dealerd_5,"")
                 if (dealer1 + dealer2 + dealerd_3 + dealerd_4 + dealerd_5 < card1 + card2 + dcard3):
                     print("The dealer cannot get anymore cards")
                 else:
                     if (dealer1 + dealer2 + dealerd_3 + dealerd_4 + dealerd_5> 21):
                        print("The dealer busted! You win")
                        print ("You win",chipbet * 2,"good job!")
                        chips = chips + (chipbet * 2)
                        confirm21 = input("Would you like to play again? ")
                     else:
                        if (dealer1 + dealer2 + dealerd_3 + dealerd_4 + dealerd_5 > card1 + card2 +dcard3):
                            print("The dealer wins!")
                            print ("You lose",chipbet * 2,"sucks to suck")
                            chips = chips - (chipbet * 2)
                            confirm21 = input("Would you like to play again? ")
                        if (dealer1 + dealer2 + dealerd_3 + dealerd_4 + dealerd_5 < card1 + card2 + dcard3):
                            print("The player wins!")
                            print ("You win",chipbet * 2,"goodjob!")
                            chips = chips + (chipbet * 2)
                            confirm21 = input("Would you like to play again? ")
                        if (dealer1 + dealer2 + dealerd_3 + dealerd_4 + dealerd_5 == card1 + card2 + dcard3):
                            print("The dealer and player tied, the bet is pushed")
                            confirm21 = input("Would you like to play again? ")

                else:
                    if(dealer1 + dealer2 + dealerd_3 + dealerd_4 > 21):
                        print("The dealer busted! You win")
                        print ("You win",chipbet * 2,"good job!")
                        chips = chips + (chipbet * 2)
                        confirm21 = input("Would you like to play again? ")
                    else:
                        if (dealer1 + dealer2 + dealerd_3 + dealerd_4 > card1 + card2 + dcard3):
                            print("The dealer wins!")
                            print ("You lose",chipbet * 2,"sucks to suck")
                            chips = chips - (chipbet * 2)
                            confirm21 = input("Would you like to play again? ")
                        if (dealer1 + dealer2 + dealerd_3 + dealerd_4 < card1 + card2 + dcard3):
                            print("The player wins!")
                            print ("You win",chipbet * 2,"good job!")
                            chips = chips + chipbet * 2
                            confirm21 = input("Would you like to play again? ")
                        if (dealer1 + dealer2 + dealerd_3 + dealerd_4 == card1 + card2 + dcard3):
                            print("The dealer and player tied, the bet is pushed")
                            confirm21 = input("Would you like to play again? ")
             else:                
                if (dealer1 + dealer2 + dealerd_3 > 21):
                    print("The dealer busted! You win")
                    print ("You win",chipbet * 2,"good job!")
                    chips = chips + (chipbet * 2)
                    confirm21 = input("Would you like to play again? ")
                else:
                    if (dealer1 + dealer2 + dealerd_3 > card1 + card2 + dcard3):
                        print("The dealer wins!")
                        print ("You lose",chipbet * 2,"sucks to suck")
                        chips = chips - chipbet * 2
                        confirm21 = input("Would you like to play again? ")
                    if (dealer1 + dealer2 + dealerd_3 < card1 + card2 + dcard3):
                        print("The player wins!")
                        print ("You win",chipbet * 2,"good job!")
                        chips = chips + (chipbet * 2)
                        confirm21 = input("Would you like to play again? ")
                    if (dealer1 + dealer2 + dealerd_3 == card1 + card2 + dcard3):
                        print("The dealer and player tied, the bet is pushed")
                        confirm21 = input("Would you like to play again? ")

        else:
            if(dealer1 + dealer2 > card1 + card2 + dcard3):
                print("The dealer wins!")
                print ("You lose",chipbet * 2,"sucks to suck")
                chips = chips - (chipbet * 2)
                confirm21 = input("Would you like to play again? ")
            if(dealer1 + dealer2 < card1 + card2 + dcard3):
                print("The player wins!")
                print ("You win",chipbet * 2,"good job!")
                chips = chips + (chipbet * 2)
                confirm21 = input("Would you like to play again? ")
            if (dealer1 + dealer2 == card1 + card2):
                print("The dealer and player tied, the bet is pushed")
                confirm21 = input("Would you like to play again? ")          
else:
    print("thank you for playing")