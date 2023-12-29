import webbrowser

print('\n1. Manhattan', '\n2. Brooklyn', '\n3. Queens', '\n4. Bronx', '\n5. Staten Island')
user = input('\nWhich borough are you planning to visit in New York? Please enter the borough with the first letter capitalized (Ex. Staten Island, Manhattan): ')

def importchecker(lst, prompt, user):
    while user not in lst:
        user = input(prompt)
    return user

user = importchecker(['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island'], '\nPlease re-enter the borough you are planning to visit in New York: ', user)

lst1 = ['Central Park', 'Times Square', 'Rockefeller Center', 'Chelsea Market', 'Statue of Liberty']
lst2 = ['Brooklyn Botanic Garden', 'Brooklyn Bridge', 'Dekalb Market Hall', 'Industry City', 'Coney Island']
lst3 = ["Gulliver's Gate", 'Snug Harbor Cultural Center', 'Staten Island Zoo', 'High Rock Park', 'Fort Wadsworth']
lst4 = ['Bronx Zoo', 'Van Cortlandt Park', 'Yankee Stadium', 'Orchard Beach', 'Bronx Museum of the Arts']
lst5 = ['The Rockaways', 'Museum of the Moving Image', 'Flushing Meadows Corona Park', 'MoMA PS1', 'Gantry Plaza State Park']

def Manhattan():
    choice = input('Please enter the number for the tourist attraction: ')
    if choice == '1':
        print("\nCentral Park is a famous urban park located in New York City that demonstrates the beauty of nature. The history of the park dates back to 1858, when it was first established. Central Park is famous for its beautiful views that can be seen through various iconic activities such as tours, entertainment, sports, etc.") 
        print("\nRestaurants near Central Park")

        #1st Restaurant
        print("\n1. Tavern On the Green" + '\n   Link: https://www.tavernonthegreen.com/')
    
        #2nd Restaurant 
        print("\n2. Jacob's Pickles" + "\n   Link: https://jacobs.picklehospitality.com/" + "\n   Reservation: https://jacobs.picklehospitality.com/reservation/")
            
        #3rd Restaurant
        print("\n3. Sarabeth's" + '\n   Link: https://sarabethsrestaurants.com/' + '\n   Reservation: https://www.opentable.com/sarabeths-central-park-south')
    
        #4th Restaurant
        print('\n4. Jean-Georges' + '\n   Link: https://www.jean-georgesrestaurant.com/')
    
        #5th Restaurant 
        print('\n5. Marea' + '\n   Link: https://www.marearestaurant.com/' + '\n   Reservation: https://www.sevenrooms.com/reservations/marea')

#Times Square
    elif choice == '2':
        print("\nTimes Square is a major tourist attraction, consisting of entertainment, restaurants, shopping, and public events. Times Square is a great place to enjoy the show business due to the numerous musicals, dramas, and performers that appear, especially on Broadway. Some of the most well-known Broadway musicals include the Lion King, Hamilton, West Side Story, and Wicked. ")
        print("\nRestaurants near Times Square:")

        #1st Restaurant 
        print("\n1. Carmine's Italian Restaurant" +"\n   Link: https://www.carminesnyc.com/" + "\n   Reservation: https://www.carminesnyc.com/reservations")
    
        #2nd Restaurant 
        print("\n2. Junior's Restaurant & Bakery" + "\n   Link: https://www.juniorscheesecake.com/")
        
        #3rd Restaurant 
        print('\n3. Bubba Gump Shrimp Co.' + "\n   Link: https://www.bubbagump.com/" + '\n   Reservation: https://www.opentable.com/r/bubba-gump-new-york?ref=1068')
        
        #4th Restaurant 
        print("\n4. Virgil's Real BBQ" + "\n   Link: https://www.virgilsbbq.com/")
        
        #5th Restaurant 
        print("\n5. Los Tacos No.1" + "\n   Link: https://www.lostacos1.com/")

#Rockefeller Center
    elif choice == '3':
        print("\nRockefeller Center is a famous landmark and home to many attractions, restaurants, and businesses. In addition, it consists of an ice skate rink and explores the history of art through various artistic events. One of the most iconic events is the annual lighting of the Christmas Tree during Christmas.")
        print("\nRestaurants near Rockefeller Center:")
      
        #1st Restaurant 
        print('\n1. Beatnic - Rock Center' + '\n   Link: https://www.eatbeatnic.com/')
      
        #2nd Restaurant 
        print("\n2. Bill's Bar & Burger" + '\n   Link: https://www.billsbarandburger.com/specials/' + '\n   Reservation: https://www.opentable.com/bills-bar-and-burger')
      
        #3rd Restaurant 
        print("\n3. Del Frisco's Grille" + '\n   Link: https://www.delfriscosgrille.com/' + '\n   Reservation: https://www.opentable.com/r/del-friscos-grille-nyc-new-york')
      
        #4th Restaurant 
        print("\n4. Del Frisco's Double Eagle Steakhouse" + '\n   Link: https://www.delfriscos.com/' + '\n   Reservation: https://www.opentable.com/r/del-friscos-double-eagle-steak-house-new-york-city-new-york')
      
        #5th Restaurant 
        print("\n5. Sean's Bar and Kitchen" + '\n   Link: http://www.seansbarandkitchen.com/' + '\n   Reservation: https://www.opentable.com/r/seans-bar-and-kitchen-new-york')

#Chelsea Market
    elif choice == '4':
        print('\nChelsea Market is a marketplace filled with food and retail stores located in the heart of the Meatpacking District in New York. The market consists of food and beverages from various cultures worldwide and promotes art, entertainment, and culture through performances and exhibitions. Chelsea Market is also a shopping center for many tourists due to the many stores, from food to lifestyle goods.')
        print('\nRestaurants in Chelsea Market:')
      
        #1st Restaurant 
        print('\n1. Very Fresh Noodles' + '\n   Link: https://www.veryfreshnoodles.com/menu')
      
        #2nd Restaurant 
        print('\n2. Miznon' + '\n   Link: https://www.miznonnyc.com/' + '\n   Reservation: https://resy.com/cities/ny/miznon-at-chelsea-market')
      
        #3rd Restaurant
        print('\n3. Lobster Place' +  '\n   Link: https://www.lobsterplace.com/')
      
        #4th Restaurant
        print('\n4. Los Mariscos' +  '\n   Link: https://www.losmariscos1.com/')
      
        #5th Restaurant
        print("\n5. L'Arte Del Gelato" +  '\n   Link: https://lartedelgelato.com/')

#Statue of Liberty
    elif choice == '5':
        print("\nThe Statue of Liberty is a historical monument dating back to the 1800s as a symbol of liberty or freedom. Visitors can reserve a ticket to climb stairs up to the statue’s crown, which has 25 windows where visitors can view the surrounding New York Harbor. A museum was also built dedicated to the monument that consists of the Immersive Theater, Engagement Gallery, Inspiration Gallery, and Roof Deck.")
        print("\nRestaurants near the Statue of Liberty:")
      
        #1st Restaurant 
        print('\n1. Statue of Liberty Crown Cafe' + '\n   Link: https://thestatueofliberty.com/')
      
        #2nd Restaurant 
        print('\n2. Terra e Mare: Restaurant in Jersey City at the Hudson House' + '\n   Link: https://www.landmarkhospitality.com/page-eat/c/0/i/54804237/terra-e-mare' + '\n   Reservation: https://www.opentable.com/r/terra-e-mare-hudson-house-jersey-city')
      
        #3rd Restaurant 
        print('\n3. El Vez and Burrito Bar' + '\n   Link: https://elveznyc.com/' + '\n   Reservation: https://resy.com/cities/ny/el-vez')
      
        #4th Restaurant 
        print("\n4. George's" + '\n   Link: https://www.georges-ny.com/')
      
        #5th Restaurant 
        print('\n5. Westville Wall Street' + '\n   Link: https://westvillenyc.com/' + '\n   Reservation: https://www.opentable.com/r/westville-wall-street-new-york')

#BROOKLYN_______________________________________________________________________________________
def Brooklyn():
    choice = input('\nPlease enter the number for the tourist attraction: ')
    if choice == '1':
        print('\nBrooklyn Botanic Garden is a garden that allows people to interact and connect with the environment. It is at least 52-arce and over 14,000 diverse plants and flowers in the Herb Garden, Water Garden, and Rock Garden. The garden is also home to birds and other wildlife animals, including rabbits, chipmunks, and butterflies. There are many activities that adults and kids can participate in to educate and explore the habitats of animals and plants.')
        print('\nRestaurants near Brooklyn Botanic Garden:')

        #1st Restaurant 
        print('\n1. Oxalis' + '\n   Link: https://www.oxalisnyc.com/' + '\n   Reservation: https://www.oxalisnyc.com/#reservations')
      
        #2nd Restaurant 
        print('\n2. Olmsted' + '\n   Link: https://www.olmstednyc.com/' + '\n   Reservation: https://resy.com/cities/ny/olmsted')
      
        #3rd Restaurant 
        print('\n3. Barboncino Pizza' + '\n   Link: https://www.barboncinopizza.com/')
      
        #4th Restaurant 
        print("\n4. Chavela's" + '\n   Link: https://chavelasnyc.com/')
      
        #5th Restaurant 
        print("\n5. Tom's Restaurant" + '\n   Link: https://tomsbrooklyn.com/')

#Brooklyn Bridge
    elif choice == '2':
        print("\nBrooklyn Bridge is a hybrid cable-suspension bridge that connects the boroughs of Manhattan and Brooklyn. It is around 6,016 feet long and a bridge where people can bike, walk, or drive on. The bridge's history dates back to the 1800s when the bridge was built and opened to cross the East River.")
        print('\nRestaurants near the Brooklyn Bridge:')
      
        #1st Restaurant 
        print('\n1. Shake Shack Dumbo' + '\n   Link: https://shakeshack.com/location/dumbo-ny')
      
        #2nd Restaurant
        print('\n2. Industry Kitchen' + '\n   Link: https://www.industry-kitchen.com/' + '\n   Reservation: https://www.industry-kitchen.com/#/form-reservations')
      
        #3rd Restaurant
        print("\n3. Clark's Restaurant" + '\n   Link: https://www.clarksdiner.com/')
      
        #4th Restaurant
        print('\n4. 1803 NYC' + '\n   Link: https://1803nyc.com/' + '\n   Reservation: https://1803nyc.com/#reservation')
      
        #5th Restaurant
        print('\n5. Cowgirl SeaHorse' + '\n   Link: https://www.cowgirlseahorse.com/')

#Dekalb Market Hall
    elif choice == '3':
        print('\nDekalb Market Hall is the largest food hall in Brooklyn, filled with international cuisines that presents its unique dining experience. The food hall consists of 30+ vendors ranging from American fast food, Japanese food, Thai food, and Caribbean cuisine to desserts, such as crepes and donuts. With its entertainment and underground vibe, the hall is a great tourist attraction to wine and dine food worldwide.')
        print("\nRestaurants in Dekalb Market Hall:")
      
        #1st Restaurant
        print('\n1. Arepa Lady' + '\n   Link: https://www.thearepalady.com/')
      
        #2nd Restaurant
        print("\n2. Pierogi Boys" + '\n   Link: https://pierogiboys.com/')
      
        #3rd Restaurant
        print('\n3. Daigo Handroll' + '\n   Link: https://www.daigobrooklyn.com/')
      
        #4th Restaurant
        print("\n4. A Taste of Katz's" + '\n   Link: https://katzsdelicatessen.com/brooklyn')
        
        #5th Restaurant
        print("\n5. Cuzin's Duzin" + '\n   Link: https://www.cuzinsduzin.com/')

#Industry City
    elif choice == '4':
        print('\nIndustry City is home to 550+ companies, which includes restaurants, retail stores, and refreshments. The IC presents traditional food, street food, bakeries, and cafes that visitors can explore and enjoy. In addition, the IC is a place where designers are able to express themselves through hand-made clothes and crafts.')
        print('\nRestaurants in Industry City:')
      
        #1st Restaurant 
        print('\n1. Japan Village' + '\n   Link: https://japanvillage.com/')
      
        #2nd Restaurant 
        print('\n2. Burger Joint' + '\n   Link: https://www.burgerjointny.com/')
      
        #3rd Restaurant 
        print('\n3. Hometown Bar-B-Que' + '\n   Link: https://hometownbbq.com/')
      
        #4th Restaurant 
        print('\n4. Taco Mix' + '\n   Link: https://www.tacomix.com/')
      
        #5th Restaurant 
        print('\n5. Frying Pan Brooklyn' + '\n   Link: https://fryingpanbrooklyn.com/')

#Coney Island
    elif choice == '5':
        print('\nConey Island is famous for its entertainment, from amusement parks, aquariums, and boardwalk to the beachfront. From live performances to shopping at gift shops, the fun never ends. The  amusement park consists of a carousel, go-karts, mini-golf, wonder wheel, and roller coasters. To end off the week, there is a weekly firework event every Friday night.')
        print('\nRestaurants near Coney Island:')
      
        #1st Restaurant
        print('\n1. L&B Spumoni Gardens' + '\n   Link: https://spumonigardens.com/')
        
        #2nd Restaurant
        print("\n2. Gargiulo's" + '\n   Link: https://gargiulos.com/' + '\n   Reservation: https://www.opentable.com/r/gargiulos-coney-island-brooklyn')
      
        #3rd Restaurant
        print('\n3. IHOP' + '\n   Link: https://www.ihop.com/en/menu')
      
        #4th Restaurant
        print('\n4. Opera Cafe Lounge' + '\n   Link: https://www.operacafelounge.com/')
        
        #5th Restaurant
        print('\n5. Kashkar Cafe' + '\n   Link: https://www.kashkar-cafe.com/')

#STATEN ISLAND__________________________________________________________________________________
def StatenIsland():
    choice = input("\nPlease enter the number for the tourist attraction: ")
    if choice == '1':
        print("\nGulliver's Gate recreates and connects the real world to a world of miniatures. The miniature world consists of famous landmarks, attractions, and cityscapes surrounded by nature, the subway system, cars, and bridges. Not only is New York City made into a miniature version, but countries in Latin America, Asia, Europe, Russia, and the Middle East are also recreated. The attraction is filled with history and stories.")
        print("\nRestaurants near Gulliver's Gate:")
        
          #1st Restaurant
        print('\n1. Beso' + '\n   Link: https://besonyc.com/' + '\n   Reservation: https://www.opentable.com/r/beso-staten-island')
        
          #2nd Restaurant
        print('\n2. Enoteca Maria' + '\n   Link: https://www.enotecamaria.com/')
        
          #3rd Restaurant 
        print('\n3. Wasabi Steak and Sushi' + '\n   Link: https://www.restaurantwasabi.com/')
        
          #4th Restaurant 
        print('\n4. Taverna on the Bay' + '\n   Link: http://tavernaonthebay.com/' + '\n   Reservation: https://www.opentable.com/r/taverna-on-the-bay-staten-island')
        
          #5th Restaurant
        print('\n5. Pastavino'  + '\n   Link: https://www.pastavinosi.com/' + '\n   Reservation: https://www.opentable.com/r/pastavino-staten-island')

#Snug Harbor Cultural Center
    elif choice == '2':
        print('\nSnug Harbor Cultural Center is centered around nature, education, and performing arts. The Snug Harbor Cultural Center consists of numerous gardens and farms, such as the New York Chinese Scholar’s Garden, Rose Garden, Healing Garden, Heritage Farm, etc. It is also home to diverse music and art that everyone can enjoy.')
        print('\nRestaurants near Snug Harbor Cultural Center:')
      
        #1st Restaurant 
        print('\n1. Harbor Eats'  + '\n   Link: https://snug-harbor.org/visit/dining/')
        
        #2nd Restaurant
        print('\n2. Blue'  + '\n   Link: https://bluerestaurantnyc.com/' + '\n   Reservation: https://www.opentable.com/r/blue-staten-island')
      
        #3rd Restaurant 
        print("\n3. Sally's Southern"  + '\n   Link: http://sallyssouthern.com/' + '\n   Reservation: https://www.opentable.com/r/sallys-southern-staten-island')
      
        #4th Restaurant
        print("\n4. Duffy's"  + '\n   Link: https://www.duffystavernnyc.com/')
      
        #5th Restaurant
        print('\n5. Ruddy & Dean'  + '\n   Link: https://www.ruddyanddean.com/')

#Staten Island Zoo
    elif choice == '3':
        print("\nStaten Island Zoo is home to various animals ranging from mammals, reptiles, and farm animals, to unique birds. A zoo is a home to endangered species from all over the world, such as in Africa and Australia are protected and managed in a safe environment. In addition, people can contribute to these animals through donations, volunteering, interning at the zoo, and educating themselves through zoo programs.")
        print('\nRestaurants near Staten Island Zoo:')
      
        #1st Restaurant 
        print('\n1. Kings Arms Diner'  + '\n   Link: https://kingsarmsdinersi.com/')
      
        #2nd Restaurant 
        print("\n2. Ho'Brah"  + '\n   Link: https://www.hobrahtacos.com/')
      
        #3rd Restaurant 
        print('\n3. Nurnberger Bierhaus'  + '\n   Link: https://www.nurnbergerbierhaus.info/menu')
      
        #4th Restaurant
        print('\n4. Panini Grill'  + '\n   Link: https://www.paninigrillny.com/')
        
        #5th Restaurant 
        print('\n5. The Local'  + '\n   Link: https://thelocalsi.com/dinner-menu/')

#High Rock Park
    elif choice == '4':
        print('\nHigh Rock Park is a park that is filled with attractions, activities, animals, and nature. There are 6 walking trails surrounded by red maples, highbush blueberries, and skunk cabbages. Hawks, owls, woodpeckers, etc., who soar in the sky use the park as a habitat. While frogs, turtles, and wood ducks live in the ponds and swamps of the park. In addition, some activities that visitors can explore include climbing Mt. Moses, where they can have a 360-degree view of the park.')
        print('\nRestaurants near High Rock Park:')
      
        #1st Restaurant
        print("\n1. Patrizia's of Staten Island"  + '\n   Link: https://thestonehousesi.com/' + '\n   Reservation: https://www.opentable.com/the-stone-house-at-clove-lakes-ny')
      
        print("\n2. Tommy's Tavern + Tap"  + '\n   Link: https://www.tommystavernandtap.com/staten-island')
      
        print("\n3. Canlon's"  + '\n   Link: https://canlons.com/')
      
        print('\n4. Sakana Sushi & Hibachi Steakhouse'  + '\n   Link: https://sakanasi.com/' + '\n   Reservation: https://www.opentable.com/r/sakana-sushi-and-hibachi-steakhouse-staten-island')
      
        print('\n5. 99 Favor Taste'  + '\n   Link:  https://www.99favortaste.com/index.html' + '\n   Reservation: https://client.minitable.net/c_reservation')

#Fort Wadworth
    elif choice == '5':
        print('\nFort Wadsworth is a tourist attraction that used to be a military installation to defend the Upper Bay and Manhattan. The attraction is crucial to the nation’s history and offers a spectacular view of New York Harbor. It is well-known for the various activities, such as running, walking, and biking, that people can do while enjoying the sight of the harbor.')
        print('\nRestaurants near Fort Wadsworth:')
      
        #1st Restaurant
        print("\n1. Nino's Restaurant"  + '\n   Link: http://ninosrestaurant.com/')
      
        #2nd Restaurant
        print("\n2. J's On The Bay"  + '\n   Link: https://www.jsonthebaysiny.com/' + '\n   Reservation: https://www.opentable.com/r/js-on-the-bay-staten-island')
      
        #3rd Restaurant
        print('\n3. Italianissimo Ristorante Cafe Bar'  + '\n   Link: https://www.italianissimony.com/')
      
        #4th Restaurant
        print('\n4. Bocelli'  + '\n   Link: https://www.osteriabocelli.com/' + '\n   Reservation: https://www.opentable.com/bocelli-ristorante')
        
        #5th Restaurant
        print('\n5. Nori Izakaya'  + '\n   Link: https://www.noriyakitori.com/' + '\n   Reservation: https://order.mealkeyway.com/customer/release/index')

#QUEENS_________________________________________________________________________________________
def Queens():
    choice = input("\nPlease enter the number for the tourist attraction: ")
    if choice == '1':
        print("\nThe Rockaways is an area where visitors can enjoy the sandy beaches, local street foods, boutiques, and the boardwalk. Not only is it beautiful, but the food and beverages are also delicious. In addition, surfers and sunbathers can enjoy the sun and waves on the beach.")
        print('\nRestaurants near The Rockaways:')
      
        #1st Restaurant 
        print("\n1. Uma's" + '\n   Link: https://umasrockaway.com/')
      
        #2nd Restaurant 
        print('\n2. Boardwalk Pizzeria' + '\n   Link: https://www.boardwalkpizzany.com/')
      
        #3rd Restaurant 
        print('\n3. Tacoway Beach (SUMMER ONLY)' + '\n   Link: https://www.tacowaybeach.com/')
      
        #4th Restaurant 
        print("\n4. Kimo's" + '\n   Link: https://kimoskitchen.com/')
      
        #5th Restaurant 
        print('\n5. Rippers (SUMMER ONLY)' + '\n   Link: https://www.eatrippers.com/')

#Museum of the Moving Image
    elif choice == '2':
        print('\nThe Museum of the Moving Image is a museum that exhibits art, music, history, and media for every visitor to appreciate. The museum provides educational programs and hands-on workshops for everyone to enjoy and learn. The museum is home to more than 130,000 objects and award-winning films. In addition, it is a way to connect various diverse cultures through the world of fine arts.')
        print("\nRestaurants near Museum of the Moving Image:")
      
        #1st Restaurant 
        print("\n1. Mom's Kitchen & Bar" + '\n   Link: https://www.eatatmomsnyc.com/')
      
        #2nd Restaurant 
        print('\n2. Burger Club' + '\n   Link: https://www.burger-club.com/')
      
        #3rd Restaurant
        print('\n3. Amylos Taverna' + '\n   Link: https://amylos.com/' +  '\n   Reservation: https://amylos.com/reservations/')
      
        #4th Restaurant
        print('\n4. Arepas Grill' + '\n   Link: https://arepasny.com/')
      
        #5th Restaurant
        print('\n5. Sanfords' + '\n   Link: https://www.sanfordsnyc.com/')

#Flushing Meadows Corona Park
    elif choice == '3':
        print('\nFlushing Meadows Corona Park, also known as Flushing Meadows Park, is a large public park that consists of hiking trails, sports, and an indoor pool. From exploring the lakes at the park through kayaking to barbecuing on the fields, Flushing Meadows Corona Park is filled with adventures and excitement. Within the park, there are numerous food courts and trucks, where visitors can enjoy a relaxing lunch. It is also a dog-friendly environment for dogs to enjoy nature and interact with other dogs.')
        print('\nRestaurants near Flushing Meadows Corona Park:')
      
        #1st Restaurant 
        print('\n1. Portofino Ristorante' + '\n   Link: https://www.grubhub.com/restaurant/portofino-ristorante-10932-ascan-ave-forest-hills/71428')
      
        #2nd Restaurant
        print('\n2. Guantanamera' + '\n   Link: https://guantanamerany.com/' +  '\n   Reservation: https://www.opentable.com/r/guantanamera-forest-hills-queens?ref=1068')
      
        #3rd Restaurant
        print('\n3. Reef Restaurant & Bar' + '\n   Link: http://reef-restaurant.com/')
      
        #4th Restaurant 
        print('\n4. Bareburger' + '\n   Link: https://bareburger.com/' +  '\n   Reservation: https://www.bareburger.com/')
      
        #5th Restaurant
        print("\n5. Dee's Wood Fired Pizza" + '\n   Link: https://www.deesnyc.com/' +  '\n   Reservation: https://www.opentable.com/dees-restaurant-queens?ref=1068')

#MoMA PS1
    elif choice == '4':
        print('\nMoMA PS1 offers a place where international artists can express themselves through contemporary art. It connects local and international artists to join together as a community to seek numerous perspectives and embrace diversity. On the other hand, the audience can explore, engage, and understand the meaning behind the paintings of numerous artists.')
        print('\nRestaurants near MoMA PS1:')
      
        #1st Restaurant
        print('\n1. Blend on the Water' + '\n   Link: https://www.blendonthewater.com/' +  '\n   Reservation: https://www.opentable.com/r/blend-on-the-water-long-island-city')
      
        #2nd Restaurant
        print("\n2. Manetta's" + '\n   Link: http://www.manettaslic.com/')
      
        #3rd Restaurant
        print('\n3. Bareburger' + '\n   Link: https://bareburger.com/')
      
        #4th Restaurant
        print('\n4. Tuk Tuk' + '\n   Link: https://www.tuktukny.com/')
      
        #5th Restaurant
        print("\n5. Jackson's Eatery|Bar" + '\n   Link: http://www.jacksonslic.com/' +  '\n   Reservation: https://www.opentable.com/r/jacksons-eatery-long-island-city')

#Gantry Plaza
    elif choice == '5':
        print("\nGantry Plaza State Park is a 12-acre park near the riverside that displays an amazing view of the midtown Manhattan buildings, such as the Empire State Building. The area is surrounded by gardens, a mist foundation, and recreational facilities. It is a dog-friendly environment, allowing dogs to interact and roam freely within the park. In addition, the plaza presents numerous concerts in the spring or summer.")
        print('\nRestaurants near Gantry Plaza State Park:')
      
        #1st Restaurant 
        print('\n1. Piatto' + '\n   Link: https://piattolic.com/' +  '\n   Reservation: https://piattolic.com/long-island-city-long-island-city-piatto-restaurant-reservations')
      
        #2nd Restaurant 
        print('\n2. American Brass' + '\n   Link: https://www.americanbrasslic.com/' +  '\n   Reservation: https://www.americanbrasslic.com/')
      
        #3rd Restaurant 
        print('\n3. Sweet Chick' + '\n   Link: https://www.sweetchick.com/')
      
        #4th Restaurant 
        print('\n4. SHI' + '\n   Link: https://www.shilic.com/' +  '\n   Reservation: https://www.opentable.com/shi')
      
        #5th Restaurant 
        print('\n5. Vernon Grille' + '\n   Link: https://vernongrille.com/')

#BRONX________________________________________________________________________________________
def Bronx():
    choice = input("\nPlease enter the number for the tourist attraction: ")
    if choice == '1':
        print('\nBronx Zoo is home to wildlife, including raccoons, alligators, gorillas, leopards, monkeys, birds, and other species. Within the zoo, peacocks are free to roam the grounds on their own. The zoo is divided into two sections, outdoor and indoor. The indoor area exhibits animals from the World of Birds, JungleWorld, Madagascar, the World of Reptiles, etc. The outdoor area displays animals from Tiger Mountain, Himalayan Highlands, Sea Lion Pool, Birds of Prey, etc.')
        print('\nRestaurants near Bronx Zoo:')
      
        #1st Restaurant 
        print('\n1. Cafe Colonial Restaurant' + '\n   Link: https://www.cafecolonialnyc.com/')
      
        #2nd Restaurant 
        print("\n2. Mario's Restaurant" + '\n   Link: https://mariosarthurave.org/about-us' +  '\n   Reservation: https://www.opentable.com/marios-restaurant-arthur-ave')
      
        #3rd Restaurant 
        print("\n3. EZ Grill NYC" + '\n   Link: https://www.ezgrillnycbronx.com/' +  '\n   Reservation: https://www.opentable.com/marios-restaurant-arthur-ave')
      
        #4th Restaurant
        print("\n4. F&J Pine" + '\n   Link: https://fjpine.com/')
      
        #5th Restaurant 
        print("\n5. Michelangelos Restaurant" + '\n   Link: http://www.michaelangelosnyc.com/' +  '\n   Reservation: https://www.opentable.com/r/michaelangelos-lounge-and-restaurant-the-bronx')

#Van Cortlandt Park
    elif choice == '2':
        print("\nVan Cortlandt Park is more than a thousand acres, consisting of ridges, forests, and valleys. It is considered to be the 3rd largest park in New York City. Within the park, visitors can explore numerous activities, such as hiking trails, sports, horseback riding, fishing, and playgrounds. In addition, Van Cortlandt Park is the first park to have a public golf course and the largest freshwater lake in the borough.")
        print('\nRestaurants near Van Cortlandt Park:')

          #1st Restaurant 
        print('\n1. Tin Marín Tapas' + '\n   Link: https://www.tinmarintapas.com/')
      
        #2nd Restaurant 
        print("\n2. Jake's Steakhouse" + '\n   Link: https://www.jakessteakhouse.com/' +  '\n   Reservation: https://www.opentable.com/r/jakes-steakhouse-bronx')
      
        #3rd Restaurant 
        print("\n3. Yukka" + '\n   Link: https://yukkalatinbistronyc.com/' +  '\n   Reservation: https://yukkalatinbistronyc.com/reservations/')
      
        #4th Restaurant 
        print("\n4. Yo-Burger" + '\n   Link: https://www.yo-burger.com/')
      
        #5th Restaurant 
        print("\n5. Aoyu Sushi" + '\n   Link: http://www.aoyusushi.com/')

#Yankee Stadium
    elif choice == '3':
        print('\nYankee Stadium is a field where baseball fans can join as a community to watch major baseball games. Not only does it provide visitors with a magnificent game to watch, but an online and in-person shop is also available. The shop displays jerseys and caps for kids and adults. In addition, the stadium provides a variety of dining options such as Steakhouse, Halal food, Hawaiian food, and Japanese food.')
        print('\nRestaurants near Yankee Stadium:')
      
        #1st Restaurant 
        print("\n1. Hibachi Grill & Supreme Buffet" + '\n   Link: http://www.hibachigrillbronx.com/')
      
        #2nd Restaurant 
        print("\n2. Porto Salvo" + '\n   Link: http://portosalvobronx.com/bronx/')
      
        #3rd Restaurant 
        print("\n3. Court Deli" + '\n   Link: https://www.courtdelinyc.com/')
      
        #4th Restaurant 
        print("\n4. Molino Rojo Restaurant" + '\n   Link: https://www.molinorojorestaurante.com/')
      
        #5th Restaurant 
        print("\n5. Papaye" + '\n   Link: https://www.papayenyc.com/')

#Orchard Beach
    elif choice == '4':
        print("\nOrchard Beach, also known as “The Riviera of New York”, is a public beach located in the Bronx. The beach is a place to visit for food and entertainment. It is an area with food carts, snack bars, 2 picnic areas to barbecue, 2 playgrounds, and 26 courts for sports activities.")
        print('\nRestaurants near Orchard Beach:')
      
        #1st Restaurant 
        print("\n1. City Island Lobster House" + '\n   Link: https://cilobsterhouse.com/')
      
        #2nd Restaurant 
        print("\n2. Vistamar" + '\n   Link: https://www.vistamarcityisland.com/' +  '\n   Reservation: https://www.vistamarcityisland.com/reservations/')
      
        #3rd Restaurant 
        print("\n3. Ohana Japanese Hibachi Seafood & Steakhouse" + '\n   Link: https://www.ohanany.com/' +  '\n   Reservation: https://www.ohanany.com/reservations')
      
        #4th Restaurant 
        print("\n4. Artie's Steak and Seafood Restaurant" + '\n   Link: https://www.artiescityisland.com/')
      
        #5th Restaurant 
        print("\n5. The Original Crab Shanty" + '\n   Link: https://www.originalcrabshanty.com/')

#Bronx Museum of the Arts
    elif choice == '5':
        print('\nBronx Museum of the Arts is a museum that connects the audience to the artistic world by displaying various exhibitions and dancing events that highlights unique cultures. Each year, there are numerous events that the museum presents that are different from the past.')
        print('\nRestaurants near The Bronx Museum of the Arts:')

        #1st Restaurant 
        print("\n1. Suyo" + '\n   Link: https://suyonyc.com/' +  '\n   Reservation: https://www.opentable.com/r/suyo-gastrofusion-bronx')
      
        #2nd Restaurant 
        print("\n2. El Nuevo Valle" + '\n   Link: https://www.elnuevovalle3.com/')
      
        #3rd Restaurant 
        print("\n3. Mi Pueblito" + '\n   Link: https://www.mipueblitothebronx.com/#/')
      
        #4th Restaurant 
        print("\n4. El Nuevo Bohío" + '\n   Link: https://www.elnuevobohiorestaurant.com/')
        
        #5th Restaurant 
        print("\n5. Xochimilco Family Restaurant" + '\n   Link: https://xochimilco-family-restaurant.business.site/')

#OPEN WEBSITE_________________________________________________________________________________
def open_url(url):
    try:
        webbrower.open(url, new = 2, autoraise = True)
    except webrowser.Error as e:
        print('ERROR: opening url', e)
        open_url()

index = 0

locations = []
if user == 'Manhattan':
    locations = lst1
    index = 1 
    for items in locations:
        print(str(index)+"."+ items)
        index += 1
    Manhattan()
  
elif user == 'Brooklyn':
    locations = lst2
    index = 1 
    for items in locations:
        print(str(index)+"."+ items)
        index += 1
    Brooklyn()

elif user == "Staten Island":
    locations = lst3
    index = 1 
    for items in locations:
        print(str(index)+"."+ items)
        index += 1
    StatenIsland()

elif user == "Queens":
    locations = lst5
    index = 1 
    for items in locations:
        print(str(index)+"."+ items)
        index += 1
    Queens()

elif user == "Bronx":
    locations = lst4
    index = 1
    for items in locations:
        print(str(index) + "." + items)
        index +=1
    Bronx()
