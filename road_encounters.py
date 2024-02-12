import random

class Road_side():

  def encounter_list(self):

    roadside_encounters = {
    1:'You come across a hexagonal hay wagon pulled by three cows with the sound of a bard playing inside. If you approach, you are offered a ride.',
    10:'You see three men in animal masks, juggling fruit.',
    100:'A small black kitten is sitting by the side of the road. It hisses right before a witch appears and attacks.',
    11:'You come across a blacksmith, who claims that he will pay you to watch him while he runs errands.',
    12:'You come across a man who invites you to play a game. If you win, you get a prize. If you lose, you owe him a favor.',
    13:'You come across a group of people arguing about a hill giant.',
    14:'You see a group of large men standing around a pit.',
    15:'You see four men dressed in black, riding horses.',
    16:'You see a wagon being pulled by a giant snail. A wizard tips his hat as he passes.',
    17:'You come across a group of young men parading down the road dressed in costumes.',
    18:'You see a group of women walking down the road. They are singing a song about a famous battle.',
    19:'You see a group of people painting a wagon at a crossroads.',
    2:'A man in beggar\'s clothing asks for your help. He claims to have been cursed by the local Duke because he witnessed the Duke murdering his wife.',
    20:'You see a man and a woman standing next to a wagon, arguing. If you tell them to make up, they will ask you to choose their punishment.',
    21:'Two men are arguing about a goat.',
    22:'As you walk along the road, you see a gleaming red gem. If you touch it, you will instantly turn into a gem that can talk for 2d20+20 days.',
    23:'Two men are arguing about the value of a bridge. If you offer to buy it, one of them will sell it to you for 10 silver pieces.He does not own the bridge. He is just hungry.',
    24:'You see a loaded cart that is trapped. If you touch it, it will explode. A group of 2d8 bandits will then attack.',
    25:'A cart is being pulled by a giant ox. The farmer riding in front says, “Hello! Goodbye!”',
    26:'As you approach a barn, someone comes out and invites you in for some cider. If you drink it, you will be poisoned.',
    27:'You come across a group of young men on their way to a feast. They will invite you to come along with them, but the feast is held in the basement of an insane cult leader who will force you to eat human flesh.',
    28:'You come across a wineskin on the side of the road. It never runs out of wine.',
    29:'You see a man carrying a large wooden box. He will offer to give it to you, but he wants you to answer three riddles. If you fail to answer, he will become enraged and attack.',
    3:'You come across a group of acrobats performing. If you join them and give them a show of your own skill, they will invite you to join their circus',
    30:'You see a cleric of a god you do not believe in. If you insult him, he will challenge you to a debate.',
    31:'You see a farmer who claims to have been cursed. As you watch him, he transforms into a unicorn and trots away.',
    32:'You see a man arguing with a boy. If you intervene, the man will thank you and the boy will attack you.',
    33:'You see a dead rabbit on the side of the road.',
    34:'You see a man carrying a board that has a long message written on it. It is a letter from a father to his son. If you stop to read it, he will steal something of yours that you will never get back.',
    35:'You see a sign that says, “Fork in the road. Go left.”',
    36:'A man dressed in black is standing in the distance. If you approach, he will ask you if he can buy your soul for 1,000 gold pieces.',
    37:'You see a stack of coffins. They are all empty.',
    38:'You see a barn painted on the side of the road. A board is nailed to the wall that says, “Welcome to Barnsville. Population 37 rats!”',
    39:'You see three old men carrying a heavy load down the road. If you help them, they will invite you over for dinner. They are three brothers.',
    4:'You come across a riverboat with a sign advertising passage to the next town.',
    40:'A bunch of men are standing in the road, arguing about a wooden barrel.',
    41:'You see a man carrying a bucket with a sign that says, “I am lost. Will you show me the way to the nearest tavern?” If you agree, he will follow you around for the rest of the day, slowing you down.',
    42:'You see a man in the distance, waving his arms.',
    43:'You see a group of prostitutes. They will ask you to help them carry their supply of cocoa leaves to the local brothel. If you help, they will then ditch you.',
    44:'You see a group of men praying at a crossroads. If you join them, they will ask you to pray to their god. If players do not, they will attack.',
    45:'You come across a man digging a hole. When you ask him what he is doing, he says that he is burying a vampire queen who was killed by a paladin. He’s actually burying his mother in law.',
    46:'A man is standing in the road with a sign that says, “I am lost.” If you try to give him directions, he will demand donations.',
    47:'You see a group of men arguing about what to do with a sheep.',
    48:'You see a group of horsemen. If you approach them, they will ask you to join them in a battle.',
    49:'You see men dragging a large wooden barrel. They are too drunk to explain what is in the barrel, but it is heavy and is not beer.',
    5:'You see a woman standing by a tree, holding a bundle. She asks you to hold it for a moment, and she runs off. When you open the bundle, you find a newborn baby.',
    50:'You see a group of men tossing a ball around. If you join in, it will quickly become very competitive.',
    51:'You see a group of farmers arguing about what crop to plant.',
    52:'You see a group of men carrying a dead man behind them.',
    53:'You see a group of young men singing songs.',
    54:'You see a man in the distance. He is very angry at someone named “Dave.” He will engage players in conversation, angry about Dave, until he is calmed/lied to, or he is given directions to find Dave.',
    55:'You see a group of men digging a hole. When you ask them what they are doing, they say that they are burying their friend, who has been gravely injured. They are actually burying a fallen member of their group.',
    56:'You see a man in the distance. He is walking with a limp. If you approach him, he will tell you that he has been attacked by a group of men, who stole his money and kicked him in the shin really hard. Really hard!',
    57:'You see a group of young men examining an old helmet, with various things growing out of it, including plants, fungi, and insects.',
    58:'A group of 2d4+2 men dressed in colorful clothing and masks are chasing a wild pig. They will challenge players to try and catch the pig, and if they succeed, they will be invited to a feast.',
    59:'You see a group of crying young boys and girls. “Our parents were taken away by an ogress! It was horrible!”',
    6:'You come across a troll passed out on the side of the road.',
    60:'You see a group of children near a dead campfire. They will ask the players to listen to their tale of woe. The children are offspring of the 2d8 bandits hiding nearby.',
    61:'You see a group of young men who are apparently fishermen. They do not have any fish, but they do have a fish shaped hat and fish shaped shoes. They claim to be from the future.',
    62:'You see a group of men fighting over a piece of food. They will attack the party if not fed.',
    63:'A small group of 2d4 young men are playing catch with a live chicken. The chicken is not enjoying the game.',
    64:'You see a group of merchants in colorful clothing, with all sorts of trinkets and baubles for sale. They are supposedly the only source of the items that they are selling.',
    65:'You see a group of men in the distance. They are in the middle of a game of chess. They will challenge the party to a game of chess for their lives. They take the game very seriously. The chess board and pieces are actually cursed.',
    66:'You see a group of rangers in full camouflage. They are embarrassed when you notice them.',
    67:'A group of 2d4+1 men in matching clothing are having an arm-wrestling competition on the side of the road. Betting is encouraged.',
    68:'Two elderly women are gossiping about a group of men involved in a nearby trial. The players are welcome to listen in.',
    69:'You see a group of young men. They are drunk, but are polite. If the players are also drunk, the men are belligerent.',
    7:'You come across a horse whose rider has fallen off. The horse will let you mount him if you can wake him up.',
    70:'An old beggar is lying on the side of the road.',
    71:'You see a group of men running away from something. It is unclear what they are running from. They do not stop.',
    72:'You see a group of men and women inspecting a dead body. They are very upset and will not allow the party to investigate the body.',
    73:'As you continue down the road, you hear a loud noise from ahead. It sounds like a wagon full of gears and scrap metal is careening down the road. A traveling gnome trinket offers to sell you his wares.',
    74:'You hear a loud squawking from above. A large vulture is circling the party.',
    75:'A man in a wagon is asking for protection to rest for the night. He has a large amount of gold in a chest.',
    76:'A group of men is in a wagon. They are insane and will not let you pass.',
    77:'Up ahead, you see a group of men in a wagon.',
    78:'There is a group of men at the side of the road arguing over some gold.',
    79:'A group of men are on horseback arguing with a merchant.',
    8:'You come across the burnt remains of a wagon.',
    80:'As you travel you hear a loud snorting sound. A large wild hog is rooting through the bushes nearby.',
    81:'A large wild boar is sleeping on the side of the road.',
    82:'A goblin is standing at the side of the road, at first glance he appears to be a small, human boy begging for food.',
    83:'An elven bard and a halfling spy have been captured by a group of slavers and are being taken to a nearby fortress.',
    84:'There is a small pond with a few ducks swimming in it.',
    85:'A large black pig is rooting through the bushes.',
    86:'A large black bear is standing at the side of the road. The bear looks healthy and well fed.',
    87:'A group of young children are playing a game of “Hide and Seek” in a nearby field.',
    88:'A group of children are running through the forest, laughing and playing tag.',
    89:'A group of children are playing a game of tag in a nearby meadow.',
    9:'You see a man in armor, waving his sword in the air, demanding that people move out of the way.',
    90:'A group of adults are having a discussion in a small clearing. You can not quite make out what they are discussing.',
    91:'A woman carrying a basket is walking down the road.',
    92:'A maiden is sitting on a rock at the side of the road looking sad.',
    93:'A small cottage is in the distance, smoke is billowing from the chimney.',
    94:'A small house is on the side of the road with a sign that reads “Cobblestone Inn”.',
    95:'A small dog is barking at you from behind a fence.',
    96:'A horse is grazing on the side of the road.',
    97:'A horse-drawn wagon is stalled in the road. A man is arguing with a farmer.',
    98:'A shepherd is herding a flock of sheep down the road.',
    99:'A small dragon is sitting on the side of the road playing with a pile of rocks.',

    }

    rand_encouter = random.randint(1,100)
    print(roadside_encounters[rand_encouter])
    return rand_encouter


#Road_side.encounter_list()   
