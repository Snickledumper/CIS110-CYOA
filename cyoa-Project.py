
print('Welcome to this choose-your-own adventure application. Throughout the game you will be asked questions. \nPlease type in your answers and hit the ENTER key.')
print()
print('Before we get started, we should give you some information about this game. You will be playing as an Ork in the Warhammer 40k universe. \nOrks, if you\'re unfamiliar, are green humanoid creatures.\nIn this universe, they are master mechanics, not because of their intelligence, \nbut for their odd ability to make things work and exist from the power of belief. \nYou are part of a speed cult, a tribe of Orks that live and breath speed and mayhem. \nRacing and violence isn\'t a hobby for you, it\'s a way of life.')
#create variables that will be used within the adventure

playAgain = 'y'
while playAgain.lower() == 'y':
    print()


    pName = input('What is your Ork name? ')
    tName = input('What is the name of your tribe? ')
    tColor = input('What is your tribe\'s color? ')
    rName = input('What is the name of your rival within the tribe? ')
    loot = input('What is the physical treasure you will be racing for? ')
    print('-' * 20)
    #Begin writing the adventure

    print(f'Welcome {pName}. You are an Ork of the {tName} Tribe, driver of a Kustom Boosta-Blastah. The Boosta-Blastah is a SpeedWagon, a heavily modified vehicle made specifically for heavy combat in the badlands.\nYou find yourself on an arid wasteland of a planet named Jy\'rah. An old planet that used to be inhabited by spacefaring humans but they have left long ago by your estimate.\nYour tribe have taken up refuge in an abandoned jet hanger which now houses many vehicles consisting primarily of spikes, bones and guns.\nOutside this hanger has a lot of tents and makeshift cabins that make up the settlement that you all call home.')
    print()
    print(f'You heard talks among your tribe that there is a fresh wreck of a capital ship off in the badland and a race among the tribes coming.\nUsually, combat in the badlands are chaotic and spontaneous, however you know when a rare wreck shows up that the megabosses of the tribes all organize a race to claim that loot.')
    print()
    print(f'As you wake from your nap, you begin walking over to your SpeedWagon as you catch the crowd of Orks gathering at the center of the camp. As you join them, you see your Megaboss tower over the rest.\nThe Megaboss is a giant figure compared to the Orks. Where your fellow brothers are about 4 to 5 feet tall, the Megaboss stands at a 10ft tall.')
    print()
    print(f'The Megaboss begins to bellow to the crowd\n"All youz Orkz are goin to listen up. I \'ave met wiv de ovva bosses and we agree dat we\'ze all race for it. We all agree on a single Speedwagon and free bikas.\nFirst one to show me a finished wagon will represent us in da big race."')
    print()
    print(f'After the tribe meeting, everyone disperses quickly to go back to their jobs and get ready for the big race.\nYou begin working on your SpeedWagon, confident that you will be selected as you\'re almost complete with the repairs since the last successful raid.\nHowever, as you\'re doing the last inspection you notice that your main drive belt is cracked and has a small incision on it.')
    print()
    print(f'You remember that {rName} is behind on their repairs, but did manage to get a new belt. The belt that was rightfully yours before he swiped it from under your nose.\nMaybe it\'s time to reclaim your property.')
    print('-' * 50)
 #first decision
    Dec1 = input('Do you want to go to their garage and reclaim your brand new belt? y or n: ' )
    while Dec1.lower() not in["y" , "n"]:
        Dec1 = input('Choice invalid, please input y or n: ')

    if Dec1.lower() == 'y':
        print()
        print(f'You head over to {rName}\'s garage. You see their half-completed SpeedWagon on a makeshift car lift, wheels laid haphazardly around the ground and bits of scrap metal and random bones litter the place.\nYou notice that {rName} isn\'t any where closeby so you approach the vehicle and see that the drive belt isn\'t installed correctly and you\'re able to snatch it easily.\nJust after you put the belt into your pouch and begin to leave, {rName} catches sight of you and yells \'Oi mate! Who do ya think youz iz, waltzing around me garage eh? Maybe I should knock some sense into ya!\'.\n{rName} begins to approach you, brows furrowed and fists clenched, they get up in your face and yells \'Youz betta get out of me garage and dun\'t let me catch youz snoopin\' around here!\'.\nYou stand your ground and return their stare with a steely gaze. Their confidence falters and they looks at the ground then back to you. \'Just git on wit it, I gotz tingz to do.\'\nYou return to your garage with a new drive belt that was meant for your SpeedWagon, and make the swap easily.')
    else:
       print(f'You decided that stealing may either be too risky or too much trouble. Though Megabosses usually don\'t care about the going-ons of the tribe members, the big race is much too important to the tribe. You may lose your SpeedWagon altogether and your place among the Megaboss\'s chosen drivers.')
    print()
    print(f'After taking some time doing your final inspection and putting away your tools, you begin closing up shop and securing the gate when the smell of stew and meat begin to fill your nostrils.\nThe murmurings of voices becoming a roar of laughter and cheers, the drums begin pounding and the guns are firing into the sky. Seems to you that the tribe is having a party in true {tName} fashion.\nYou join in the festivities after locking up, grabbing a large bowl of stew and watch as the others jump around to the drum beat and drink their fill of grog that was stolen from another tribe weeks ago.\nThe Megaboss is making his rounds, speaking to each of the drivers and eventually he reaches you.\n"I\'ve seen ya work on dat SpeedWagon fo weekz. Me tinks youz make a good rep. Youz gonna be da driver fo tomorrow\'s race. Dun\'t lose."')
    print()
    print(f'In the following day, you line up at the starting line in the middle of the wasteland before dawn, surrounded by 3 other tribes of Orks of varying colors. All those racing began to line up and they all start their engines, ensuring their weapons are loaded and there are plenty of ammo in their reserves.\nEvery SpeedWagon is made up up a driver, a co-driver, and a gunner. each biker has one rider. All the Orks are strapping metal scraps on straps onto themselves to armor themselves, putting on goggles and gloves, and throwing insults at one another to gain a psychological edge. As soon as the sun peeks over the horizon, a flare is shot to the sky, signaling the start of the race.')
    print()
    print('The engines roar as well as the Orks, the wagons and bikes speeding off with a large dust trail behind them. The combat is fierce with bullets flying every which way and explosions going off haphazardly within this congested mass of Ork and metal, bikers and wagons are blown to smithereens as everyone speeds across the wasteland.\nAs the race goes on, there are only 2 tribes left, racing towards the slowly approaching finish line that is the fresh wreckage of glorious loot.\nThe surviving tribe has their Wagon and 2 bikes left while your group are left with yourself, and one biker.\nAll seems bleak as the enemy has a larger force, but Orks fight harder and better when their backs are to the wall.')
    print('-' * 50)
 #second decision
    Dec2 = input('Do you puff out your chest and let out a Waaagh?! y or n: ')
    while Dec2.lower() not in['y' , 'n']:
        Dec2 = input('Choice Invalid, please input y or n: ')
    
    if Dec2.lower() == 'y':
        print()
        print(f'You puff out your chest let out a primal roar "Waaaaaaagh!" The surviving Ork lets out a roar. That sound is the glorious sound of combat. What all orks live for and die for.\nYour co-driver puts a mouthful of rich gasoline into his mouth and climbs to the hood and spits it into the bug catcher, forcing additional fuel into the motor increasing the power.')
    if Dec2.lower() == 'n':
        print()
        print(f'You cannot muster up the roar, your enemies bearing down, smashing into the sides of your SpeedWagon shooting out the tires.\nA tire pops and the SpeedWagon veers sharply to the side, sideswiping a fellow biker and taking them out. The wagon begins to shake violently as the front digs into the sand.')
 #Outcome 1 if answers to both decisions are y
    if Dec1.lower() == 'y' and Dec2.lower() == 'y':
        print()
        print(f'With their engine roaring and the Waaaagh screaming in their hearts, the Orks began to tear down the wasteland, zealously firing all their weaponry and explosives at the enemy.\n{pName} emerges from the wreckage and fires alive, pistons firing on all cylinders, and tears down the wasteland, reaching the wreckage.\nThey find the goldmine. {loot} is found within the wreckage and you fire a flare, lighting up the sky in {tName}\'s {tColor} hue. You find the favor of the Megaboss and are promoted to the higher circle as the Megaboss\'s right hand.')
 #Outcome 2 if answer to Decision 1 is y but 2 is n
    if Dec1.lower() == 'y' and Dec2.lower() == 'n':
        print()
        print(f'You and your surviving biker fight hard as you can, but whether your rage wasn\'t hot enough or your Speedwagon wasn\'t running as hard, your vehicles begin to fail and your wagon begins to swing into a slide, almost tipping over into a roll but you come to a dead stop. You didn\'t win, but worse yet, you didn\'t die. You\'re alive with the realization that you failed your megaboss and your tribe. Being demoted into a laboring peon is the best case scenario, but you lost the great race. You just might be exiled from the tribes and subjected to a lonely path of the wasteland.')
 #Outcome 2 if answers to Decision 1 is n but 2 is y
    if Dec1.lower() == 'n' and Dec2.lower() == 'y':
        print()
        print(f'You and your surviving biker fight hard as you can, but whether your rage wasn\'t hot enough or your Speedwagon wasn\'t running as hard, your vehicles begin to fail and your wagon begins to swing into a slide, almost tipping over into a roll but you come to a dead stop. You didn\'t win, but worse yet, you didn\'t die. You\'re alive with the realization that you failed your megaboss and your tribe. Being demoted into a laboring peon is the best case scenario, but you lost the great race. You just might be exiled from the tribes and subjected to a lonely path of the wasteland.')
 #Outcome 3 if both answers are n   
    if Dec1.lower() == 'n' and Dec2.lower() == 'n':
        print()
        print(f'The tires pop and the belt snaps, the wagon shakes violently and begins to start tumbling while the enemy begins to rocket away. The Speedwagon begins rolling hard, catching their fellow bikers in the mix and taking them out.\nThe fuel begins to leak out of the still-running motor and engulfs the wagon in flame. It comes to an abrupt stop when slamming into a rock, sending random chucks of molten metal through the sky.')
    print()
 #make a loop to ask if the user wants to play again
    playAgain = input(f'Would you like to play again? y or n: ')
    while playAgain.lower() not in [ 'y' , 'n']:
        playAgain = input(f'Invalid choice, please input y or n: ')