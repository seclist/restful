import requests

print("""
   ▄████████    ▄████████    ▄████████     ███        ▄████████ ███    █▄   ▄█       
  ███    ███   ███    ███   ███    ███ ▀█████████▄   ███    ███ ███    ███ ███       
  ███    ███   ███    █▀    ███    █▀     ▀███▀▀██   ███    █▀  ███    ███ ███       
 ▄███▄▄▄▄██▀  ▄███▄▄▄       ███            ███   ▀  ▄███▄▄▄     ███    ███ ███       
▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ▀███████████     ███     ▀▀███▀▀▀     ███    ███ ███       
▀███████████   ███    █▄           ███     ███       ███        ███    ███ ███       
  ███    ███   ███    ███    ▄█    ███     ███       ███        ███    ███ ███▌    ▄ 
  ███    ███   ██████████  ▄████████▀     ▄████▀     ███        ████████▀  █████▄▄██ 
  ███    ███                                                               ▀         
                                                                                     
                        osint by seclist                                                                                 
                                                                                     
                                                                                     
                                                                                  
                                                                                             
      
      
      """)

def usernamesel():
    global username
    username = input("Enter the username you want to check: ")
    print("\nUsername selected is:", username)
    uservalid()

def uservalid():
    while True:
        choice = input("\nWould you like to see 'not found' and error codes? (y/n): ")
        if choice.lower() == "n" or choice.lower() == "N":
            usercheck_exist()
            break
        elif choice.lower() == "y" or choice.lower() == "Y":
            usercheck_all()
            break
        else:
            print("\nInvalid choice. Please type 'y' or 'n'.")

def usercheck_all():
    with open(f"{username}.txt", "w") as file:
        for url, site in sites:
            response = requests.get(url.format(username))
            if response.status_code == 200:
                print(f"{site}: Username exists")
                file.write(f"{site}: {url.format(username)}\n")
            elif response.status_code == 404:
                print(f"{site}: Username not found")
            else:
                print(f"{site}: Error {response.status_code}")
    print("Links of existing usernames saved to "+username,".txt")

def usercheck_exist():
    existing_links = []
    for url, site in sites:
        response = requests.get(url.format(username))
        if response.status_code == 200:
            print(f"{site}: Username exists")
            existing_links.append(url.format(username))
    save_links(existing_links)

def save_links(links):
    with open(username + ".txt", "w") as file:
        for link in links:
            file.write(link + "\n")
    print("Links of existing usernames saved to "+username,".txt")

sites = [
    ("https://www.instagram.com/{}", "Instagram"),
    ("https://www.google.com/search?q=site:twitter.com{}", "Twitter"),
    ("https://www.facebook.com/{}", "Facebook"),
    ("https://www.linkedin.com/in/{}", "LinkedIn"),
    ("https://www.youtube.com/user/{}", "YouTube"),
    ("https://www.pinterest.com/{}", "Pinterest"),
    ("https://www.snapchat.com/add/{}", "Snapchat"),
    ("https://www.twitch.tv/{}", "Twitch"),
    ("https://www.tiktok.com/@{}", "TikTok"),
    ("https://{}.tumblr.com/", "Tumblr"),
    ("https://www.quora.com/profile/{}", "Quora"),
    ("https://www.flickr.com/people/{}", "Flickr"),
    ("https://www.deviantart.com/{}", "DeviantArt"),
    ("https://www.behance.net/{}", "Behance"),
    ("https://dribbble.com/{}", "Dribbble"),
    ("https://soundcloud.com/{}", "SoundCloud"),
    ("https://vimeo.com/{}", "Vimeo"),
    ("https://wa.me/{}", "WhatsApp"),
    ("https://t.me/{}", "Telegram"),
    ("https://line.me/ti/p/~{}", "LINE"),
    ("https://www.snapchat.com/add/{}", "Snapchat"),
    ("https://www.joinclubhouse.com/@{}", "Clubhouse"),
    ("https://github.com/{}", "GitHub"),
    ("https://steamcommunity.com/id/{}", "Steam"),
    ("https://open.spotify.com/user/{}", "Spotify"),
    ("https://stackoverflow.com/users/{}", "Stack Overflow"),
    ("https://bitbucket.org/{}", "Bitbucket"),
    ("https://{}.wordpress.com/", "WordPress"),
    ("https://{}.blogspot.com/", "Blogger"),
    ("https://en.wikipedia.org/wiki/User:{}", "Wikipedia"),
    ("https://www.imdb.com/user/{}", "IMDb"),
    ("https://www.origin.com/{}", "Origin"),
    ("https://club.ubisoft.com/en-us/profile/{}", "Uplay"),
    ("https://www.gog.com/u/{}", "GOG"),
    ("https://battle.net/{}", "Battle.net"),
    ("https://itch.io/profile/{}", "itch.io"),
    ("https://account.garena.com/{}/info", "Garena"),
    ("https://bethesda.net/en/profile/{}", "Bethesda.net"),
    ("https://www.humblebundle.com/user/{}", "Humble Bundle"),
    ("https://bandcamp.com/{}", "Bandcamp"),
    ("https://www.last.fm/user/{}", "Last.fm"),
    ("https://www.mixcloud.com/{}", "Mixcloud"),
    ("https://splice.com/{}", "Splice"),
    ("https://audius.co/{}", "Audius"),
    ("https://listen.tidal.com/{}", "Tidal"),
    ("https://500px.com/{}", "500px"),
    ("https://www.flickr.com/people/{}", "Flickr"),
    ("https://unsplash.com/@{}", "Unsplash"),
    ("https://archiveofourown.org/users/{}", "ArchiveofOurOwn(AO3)"),
    ("https://www.foodnetwork.com/profiles/talent/{}", "FoodNetwork"),
    ("https://www.myfitnesspal.com/profile/{}", "MyFitnessPal"),
    ("https://www.mapmyfitness.com/profile/{}", "MapMyFitness"),
    ("https://www.strava.com/athletes/{}", "Strava"),
    ("https://artistsnclients.com/people/{}", "Artists&Clients"),
    ("https://www.pixiv.net/en/users/{}", "Pixiv"),
    ("https://www.webtoons.com/en/{}/", "Webtoon"),
    ("https://dribbble.com/{}", "Dribbble"),
    ("https://www.behance.net/{}", "Behance"),
    ("https://www.codecademy.com/profiles/{}", "Codecademy"),
    ("https://leetcode.com/{}", "LeetCode"),
    ("https://www.topcoder.com/members/{}", "TopCoder"),
    ("https://www.kaggle.com/{}", "Kaggle"),
    ("https://devpost.com/{}", "Devpost"),
    ("https://www.freelancer.com/u/{}", "Freelancer"),
    ("https://www.toptal.com/freelancers/{}", "Toptal"),
    ("https://www.guru.com/freelancers/{}", "Guru"),
    ("https://stackexchange.com/users/{}", "Stack Exchange"),
    ("https://news.ycombinator.com/user?id={}", "HackerNews"),
    ("https://www.producthunt.com/@{}", "ProductHunt"),
    ("https://www.transformice.com/profiles/view/{}/", "Transformice"),
    ("https://www.binweevils.com/profile/{}/", "Bin Weevils"),
    ("https://www.poptropica.com/avatarstudio/avatar.html?a={}&page=0", "Poptropica"),
    ("https://www.neopets.com/userlookup.phtml?user={}", "Neopets"),
    ("https://terraria.gamepedia.com/User:{}", "Terraria"),
]

usernamesel()

