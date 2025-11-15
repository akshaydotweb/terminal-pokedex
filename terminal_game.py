print("Welcome to the Pokemon Adventure!")
print("You are a brave Pokemon Trainer seeking the legendary pokemon 'Arceus'.")
print("Make choices wisely, or face the consequences. \n")

current_scene = "start"
pokedex = ""

while current_scene != "end":
	if current_scene == "start":
		print("You stand at the Twinleaf Town.")
		print("A path splits into two: one lead to The summit of Mount Coronet, the other to The Hall of origin")
		print("1. The summit of Mount Coronet")
		print("2. The Hall of Origin")
		choice = input("What do you choose? ")
		if choice == "1":
			current_scene = "MountCoronet"
		elif choice == "2":
			current_scene = "HallOfOrigin"
		else:
			print("invalid choice. Try again. \n")
	elif current_scene == "MountCoronet":
		print("You reached the summit of Mount Coronet.")
		print("You see 'Dialga' and a 'Azure Flute'")
		print("1. Capture Dialga")
		print("2. Wait for Azure Flute")
		choice = input("What do you choose? ")
		if choice == "1":
			current_scene = "SpearPillar"
		elif choice == "2":
			current_scene = "HallOfOrigin"
		else:
			print("invalid choice. Try again. \n")
		
	elif current_scene == "SpearPillar":
		print("You reached the Spear Pillar.")
		print("1. Play the Azure Flute") 
		print("2. Go back to Mount Coronet")
		choice = input("What do you choose?")
		if choice == "1":
			current_scene = "HallOfOrigin"
		elif choice == "2":
			current_scene = "MountCoronet"
		else:
			print("invalid choice. Try again. \n")

	elif current_scene == "HallOfOrigin":
		print("You reached the Hall of Origin")
		print("1. Capture 'Dialga'")
		print("2. Capture 'Aceus' ")
		choice = input("Which pokemon do you choose? ")
		if choice == "1":
			current_scene = "Dialga"
		elif choice == "2":
			current_scene = "Aceus"
		else:
			print("invalid choice. Try again. \n")

	elif current_scene == "Dialga":
		print("congratulations you captured 'Dialga'")
		print("                                          .::                                                       ")
		print("                                         !PB5       .^^.                                            ")
		print("                                        ?PPP:  .:. ^55B^                                            ")
		print("                                      :555P..~J5GY7P?P~                                             ")
		print("                                     ~PJY5^75YJ5G&Y!G~                                              ")
		print("                                    7G?YBY5J!75PB?~G~                                               ")
		print("                                  .Y57Y#PJ!!?5PP~~B~                                                ")
		print("                                 ^5Y!5#5!!?Y5P5:~G~            .77~.                                ")
		print("                                !PJ!5#GJ?555GY:~BY.^.         .PY!B^                                ")
		print("                              .JP?75#GY?P5PPJ^~BBG5PJ        .PJ.!B.                                ")
		print("                             :55?75&G5?55PP?:~BB!GJ7B!      .PJ.:Y5                                 ")
		print("                             :55?75&G5?55PP?:~BB!GJ7B!      .PJ.:Y5                                 ")
		print("                             !G?7?#B5J55PY7:!#G:.B?!YG.    .PJ::^G!          ^?JJ:                  ")
		print("                             ~G77PB5?555P7^:B5. :B?77G?   :PJ:::7B:       ^7YJ!7B!                  ")
		print("                            .J5?PPYJY555P7:7G.  ^B?77?B^ :P?::::55     :7YY7:^Y5:                   ")
		print("                        !5JJYP5GY?Y55P5P57:P7   ^B777!PPJG?::::~B?  .7YY7^::7P?                     ")
		print("                        :YG?JBPJ!YYPPYJJ~^JB7?~ ~B7777P?7P^:::!?!JYYY?~:::^55:                      ")
		print("                          ~GBPP7JJ?5Y!:.~55J~GY~YB?777P7?Y:::!Y^.~Y7:::::?G?                        ")
		print("                          .BG5PYJJ?!!G~.?P~.!P5P?JP777P75?::!5::?J^:::^~55^                         ")
		print("                          ?G55JJ??JP#P~^5Y!?5J?PY!PJ77P7G~:!Y^~J!::^~7!~G~   ..:^~!!777.            ")
		print("                          5P5#5PGGB5!~YP5GP#5~^55Y7P77P?P.!5^??::~77!^:^?G??JJ???!!!7JB~            ")
		print("                          .JG#GYYPGP~!BP55GB7~5PJGYJ57P5J!Y!?!^!77~^~777!^^::::^~7JJ?!:             ")
		print("                            7G!7?!GBG5B5PYYPPG#?:5PJYYJ?7775!7?!!!77!^::::^^!?JJ?!:.         .      ")
		print("                             ..BPY~GGBGP5PJJPB5~?BYJJYYY7^:~!~Y?77!!7????JJ?7^.         .:!JP5.     ")
		print("                               ?GY5!BGGGP5P7?5PPBGPPPPPPPPJ::~JG#PYJ7~^:.         ..^~?YPPPGG~      ")
		print("                               .GYJYJBPGP555?55555P5?J5555G?J5JPGGBGGGPP5YYJJJJYY5PGGGPJ?Y5?.       ")
		print("                                !B??B#GGGP55P5PPPY7?5P5555GPPP!?55PGGPGGGGGGGGGGGGPP555YY7:         ")
		print("                                 JG?!PYJ55PPPP5?~!5P555555555J!75555GP5555555555PPGGP57^            ")
		print("                                  !P7?~.!!^?YJ7?PPYYYY5555YY???!?5555GBGGGGGGGGP5J7^.               ")
		print("                                 :7GGJ::?:!5J?YG5YYYYYY5PYY5PP55J?YP55BG??7!~^:.                    ")
		print("                              ^?5GBB5Y?J~:^^^:^YP5YYJYYYPPGGGP5555YJ55PB!                           ")
		print("                           .75GBGGGPBPYYY~~!!7??YYP5?YYYGBPP5PBP5555JYPPB7                          ")
		print("                          !PGGGGGGGGPGPPPJ777?GGPP555?5YG5.. .!PBP555!J5PB?                         ")
		print("                         ~BYPGGGGGPGGGGGBB5JJJ5GGP55PJYPPB~     !BGPP?!YGGB?                        ")
		print("                         ?BYGGGPGGBGJYB55GPYYYYPBGP5PJ755GP.    .PBGBPYPBG?B^                       ")
		print("                        ^BBPBGGGGGP5!P5JY7PGGGGB?GG557!?P5#!    .P5JGGGGGP5#!                       ")
		print("                       .G5BBBPYJJ?YBGYYY7?GGPGG#:7#PP?!YP5B5:    ^YGPGGBGGY#P.                      ")
		print("                       JGY5#JP55PG#PYY?775GGGGBP.JGGG5J5GP~YJ     .GGJBGGGYP#!                      ")
		print("                     ~5P5Y5Y7GGGGPBGYJJJJY5P55Y^ 55JG5P5P5?G?      5#?GBYBPYB5                      ")
		print("                   .JG5YJ5J7?BGGGG#7             .5BJPGGPJPBJ     .GG7GPJB5JBG.                     ")
		print("                  .Y#PYY5?7?5BGBBB5:              !#!P5YG5JGG.    .B5?B5J#PYGP.                     ")
		print("                   .77JPYJJ??7!!~:.               ?B^PP!G57GB:     7?!!Y?~?J~.                      ")
		print("                                                  5Y.GP^B5!5#~                                      ")
		print("                                                  G?7#5^BP?5P:                                      ")
		print("                                                  ?J!JGJ!Y5!.                                       ")
		print("                                                                                                    ")
		print("                                                                                                    ")
		choice = input("To add this on you pokedex press 1: \n")
		if choice == "1":
			current_scene = "end"
			pokedex = "Dialga"
			print("You have completed your adventure by capturing Dialga!")
			print("Thank you for playing Pokemon Adventure!")
		else: 
			print("invalid choice try again")


	elif current_scene == "Aceus":
		print("congradulations you captured 'Aceus'")
		print("                                                       ..:::^^~~~^^^^:                              ")
		print("                                                  .::^^^^~!7?7!~^:....                              ")
		print("                                               ::::::~?YYJ7^.                                       ")
		print("                                             :^:...75PJ^.                                           ")
		print("                                            ^^...^5G?.                                              ")
		print("                                           ~^::.~PP^                                                ")
		print("                                          ~^:::~PG:                                                 ")
		print("                              :!        .!^:::^PB7                                                  ")
		print("                      !~      ~^^    ..^~::::~5GP.                                                  ")
		print("                      !!!    .~.!.::^^::..:~JPGB!                                                   ")
		print("                      !77!.::!^.~~:::..:~?5GGGGJ                                                    ")
		print("                      ?7!!:::!::^~..^!JPGGGGGG?                                                     ")
		print("                     :7^....~^:::!~JPGGGPPGG5!                                                      ")
		print("                    ~^...::^~.::.?GGGPPPGGP?.                                                       ")
		print("                   ~?:..:..^^~::.7GPPGGGP?:                                                         ")
		print("                  ^!!...:^!YBJ.:.?GGGP5Y^                                                           ")	
		print("                  !7!~7JPGPGG^::^5PYJ7?.                                                            ")
		print("                  :~~75GGPGY!^~7??7!!?^                                                             ")
		print("                      ^Y5YY?!7??7!!!!7.                                                             ")
		print("                      77~^:.:?7!!~^^:^!.                                                            ")
		print("                         .:~7~^^^::::.:^^:.                                                         ")
		print("                       !!7?7^..:^.::::...:^^. ?~                                                    ")
		print("                       ^??~.::::::::.:::^^^~^:YY:                                .:.                ")
		print("                        !:.:::::::::!~~^:.   ^YY?                ::.          :^~7?.                ")
		print("                       ~:..:::^::::~?.       ^YJY^ .:~!?JJ^      !!!!:     .^~~7?!                  ")
		print("                    .^77.:::~?~:::::^^^:.    ^YJYY7JYYYJ!.       :!^!J^ :^~~~!?!.                   ")
		print("                    .7?J~~7YP7::::::.:^~~    .YPYJJYY7^          .7^^!J~~^~7?!.                     ")
		print("                      JGY5GG7::::::~!^:.     !5GPY5?:             !!JJJ!!??~.                       ")
		print("                     7PPPGP?.:::::^J:      ~YP555YP.             ^5Y5J7??^                          ")
		print("                    ?P55P5Y::::::::^~    .JGPP5PPPP^           ^~~?7~!Y?               .:^^~~~!!!!~:")
		print("                   ?P555P57.::::::::^~:::7JJJJ~J55P7         ^!~^~~~~JY:           .:~!!!!!7JJ?!^:. ")
		print("                  7GP55P55~:~!~~~^^^:^^:::....::^~!7~^.    :!77??J7!!?Y:::......:^!777!!?5PJ~.      ")
		print("           .:::^^^7?777777~~!!~~^^^^^:::::::::::...:~77~.^!77??7^77!!JJ:::^^~!777777!!7PGJ:         ")
		print("           ~::::::.......~~^^^^^~~~~~~!~^::::::::....^7777?JY7~^^?7!!JJ~~~!!!!!!!!!!7YB5:           ")
		print("          .~..::::::::::::::^~!!7!!!~~^^:..^7!~~~~^^::^?7JY7!!777J!~!JY!77??????JJYPBG!             ")
		print("          :7:^~:::^^^^^^:~7^::::::::::::::::^^~!77!!!7!?7J777!77J!^^7Y55GGBBGBBBBB#BJ:              ")
		print("       .^^~J7~:~~~^::..^7?77!!!!!!!~~^^^::::::::^~7??7777J!7777?J^^!5BB#BBBBBBBGPY7:                ")
		print("    .:~~:^~!7~!~:.::.~YBBBGGPYJ?777777!!~^::::::::::^7J?Y?7777!J!^~JJ?JYJ^^^~~^:.                   ")
		print(" :^^^::..7:^!!:.::::JBBGGB###BP5YJ????777!!~^^:::::::~YYJ!7777?7^^?J!!!!^                           ")
		print(":!::.:::^J~::::::::77~:..:~7JY5P5PPPY777!777!!!~~~~!?YY?!777!7?^^!Y77?~.                            ")
		print(" ^7~^!^!J5?~::::::~^            .5PPP7^!77!!77777?JYYYJ!!!!!7?~^^?Y77:                              ")
		print("  .!JJ??Y5J^:::::.!J.           ^PPPP^^JPP555PPGGGGYJJY7!!!7J7!~7YJJ!                               ")
		print("    75YY5?7.::::..~PY~          !PPPP5PPPP5YY5BBBBBPJJYJ!7??!!!?J?777                               ")
		print("    .YY5?7~.:::..^YYYYJ!.       7GPPGPP?:.75YYPBBBBBYJJY??7!!7YJ7!!!?:  ..:^~.                      ")
		print("     .^?!7::::.:!YYYYYYYJ.     !PBG5GJ:    JYYYPBBBBG?7!7!!!?Y?!!77!77^!!!!77                       ")
		print("      ^~7~.:::~JG55YYYYYY7   ^YPGGPPP:     :YYYY5GBGPYYJ!!7JY7!77777!?J7!7?7.                       ")
		print("     :!~7:::^^..~YPP5YYYY5^:?PPPPPPPP:      ?YYYYY55?J5Y7JY!~77!777777777?7:                        ")
		print("     !~7~:^^.     :?PP5YYY5PP5?^.?P5P~      ~YYYYYJ!:!YJ?YPY..777777777777^                         ")
		print("    ~~~?~~:         ^YGP5Y5Y:.    75PY      .?YJ7~^!77~!!75^   !7!7!!77777                          ")
		print("   :~~!?~             !PPPPY       .~7:     :!7~!?Y555?:^!J.   .7!!!J7!!?^                          ")
		print("   !^!!.               :JGPG~               ^~^:JPYYYY5!^^J.    J7!7J!777                           ")
		print("   :^:                   !5P?                   J5Y5YYYY^~J.   .??!777777                           ")
		print("                          :J7                  ^55YYYYY5?^J.   !77777777?                           ")
		print("                                               JPGYYYY5Y7!?:  ^JJ7777777?                           ")
		print("                                              !PG5YY5Y7: :7: :J5J777777?^                           ")
		print("                                             :PGPYYY7:      .JYY77777?~.                            ")
		print("                                            .Y55Y5?:       :JJY?!7777:                              ")
		print("                                            7YJJJ~        :?7??!777^                                ")
		print("                                           7JJY?^        :7!!7~!7~.                                 ")
		print("                                          :YJYJ:        :?!!7~~^.                                   ")
		print("                                         :JJ?~         .77!!?~.                                     ")
		print("                                         .^:          :!7!7~.                                       ")
		print("                                                     .7!!^.                                         ")	
		print("                                                                                                    ")
		choice = input("To add this on you pokedex press 1: \n")
		if choice == "1":
			current_scene = "end"
			pokedex = "Arceus"
			print("You have completed your adventure by capturing Arceus!")	
			print("Thank you for playing Pokemon Adventure!")
		else:
			print("invalid choice try again")
