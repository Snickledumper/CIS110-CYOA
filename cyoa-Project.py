
print('Welcome to this choose-your-own adventure application. Throughout the game you will be asked questions. \nPlease type in your answers and hit the ENTER key.')
print('Before we get started, we should give you some information about this game. You will be playing as an Ork in the Warhammer 40k universe. \nOrks, if you\'re unfamiliar, are green humanoid creatures.\nIn this universe, they are master mechanics, not because of their intelligence, \nbut for their odd ability to make things work and exist from the power of belief. \nYou are part of a speed cult, a tribe of Orks that live and breath speed and mayhem. \nRacing and violence isn\'t a hobby for you, it\'s a way of life.')
#create variables that will be used within the adventure
pName = input('What is your Ork name? ')
tName = input('What is the name of your tribe? ')
tColor = input('What is your tribe\'s color? ')
rName = input('What is the name of your rival within the tribe? ')
loot = input('What is the loot you will be racing for? ')
print('-' * 20)
#Begin writing the adventure

print(f'Welcome {pName}. You are an Ork of the {tName} Tribe, driver of a Kustom Boosta-Blastah. The Boosta-Blastah is a SpeedWagon, a heavily modified vehicle made specifically for heavy combat in the badlands.\nYou find yourself on an arid wasteland of a planet named Jy\'rah. An old planet that used to be inhabited by spacefaring humans but they have left long ago by your estimate.\nYour tribe have taken up refuge in an abandoned jet hanger which now houses many vehicles consisting primarily of spikes, bones and guns.\nOutside this hanger has a lot of tents and makeshift cabins that make up the settlement that you all call home.')
print(f'You heard talks among your tribe that there is a fresh wreck of a capital ship off in the badland and a race among the tribes coming.\nUsually, combat in the badlands are chaotic and spontaneous, however you know when a rare wreck shows up that the megabosses of the tribes all organize a race to claim that loot.')
print(f'As you wake from your nap, you begin walking over to your SpeedWagon as you catch the crowd of Orks gathering at the center of the camp. As you join them, you see your Megaboss tower over the rest.\nThe Megaboss is a giant figure compared to the Orks. Where your fellow brothers are about 4 to 5 feet tall, the Megaboss stands at a 10ft tall.')
print(f'The Megaboss begins to bellow to the crowd\n"All youz Orkz are goin to listen up. I \'ave met wiv de ovva bosses and we agree dat we\'ze all race for it. We all agree on a single Speedwagon and free bikas.\nFirst one to show me a finished wagon will represent us in da big race."')
print(f'After the tribe meeting, everyone disperses quickly to go back to their jobs and get ready for the big race.\nYou begin working on your SpeedWagon, confident that you will be selected as you\'re almost complete with the repairs since the last successful raid.\nHowever, as you\'re doing the last inspection you notice that your main drive belt is cracked and has a small incision on it.')
print(f'You remember that {rName} is behind on their repairs, but did manage to get a new belt. The belt that was rightfully yours before he swiped it from under your nose.\nMaybe it\'s time to reclaim your property.')

Dec1 = input('Do you want to go to their garage and reclaim your brand new belt? y or n: ' )
while Dec1.lower() not in["y" , "n"]:
    Dec1 = input('Choice invalid, please input y or n: ')

if Dec1.lower() == 'y':
    print(f'You head over to {rName}\'s garage. You see their half-completed SpeedWagon on a makeshift car lift, wheels laid haphazardly around the ground and bits of scrap metal and random bones litter the place.\nYou notice that {rName} isn\'t any where closeby so you approach the vehicle and see that the drive belt isn\'t installed correctly and you\'re able to snatch it easily.\nJust after you put the belt into your pouch and begin to leave, {rName} catches sight of you and yells \'Oi mate! Who do ya think youz iz, waltzing around me garage eh? Maybe I should knock some sense into ya!\'.\n{rName} begins to approach you, brows furrowed and fists clenched, they get up in your face and yells \'Youz betta get out of me garage and dun\'t let me catch youz snoopin\' around here!\'.\nYou stand your ground and return his stare with a steely gaze. His posture and pride falters and he looks at the ground then back to you. \'Just git wit it, I gotz tingz to do.\'\nYou return to your garage with a new drive belt that was meant for your SpeedWagon, and make the swap easily.')
else:
   print(f'You decided that stealing may either be too risky or too much trouble. Though Megabosses usually don\'t care about the going-ons of the tribe members, the big race is much too important to the tribe. You may lose your SpeedWagon altogether and your place among the Megaboss\'s chosen drivers.')

   print(f'After you go over your SpeedWagon, you are confident in it\'s state and begin to close up shop.')