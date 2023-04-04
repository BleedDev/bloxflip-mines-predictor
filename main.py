import cloudscraper
import random

cs = cloudscraper.create_scraper()




auth = "yourauth" #place yur auth


r = cs.get('https://rest-bf.blox.land/games/mines/history', headers={"x-auth-token": auth}, params={'size': '1','page': '0'})
data = r.json()['data']
latest_game = data[0]
mines_location = latest_game['mineLocations']
clicked_spots = latest_game['uncoveredLocations'] #get the past game's clicked locations
fp = f"{clicked_spots[0]}" #1.
sp = f"{clicked_spots[1]}" #2.
tp = f"{clicked_spots[2]}" #3.

spots = [fp, sp, tp]

random.seed(42) #always the same result

ml1 = random.choice(spots)
ml2 = random.choice(spots)
ml3 = random.choice(spots)

if ml1 == ml2 or ml1 == ml3 or ml2 == ml3:
        i = random.randint(0, 2)
        spots[i] = str(int(spots[i]) + random.randint(1, 3))
        if int(spots[i]) > 24:
            spots[i] = str(int(spots[i]) - 1)
        if int(spots[i]) > 24:
            spots[i] = str(int(spots[i]) - random.randint(1, 15))
        ml1, ml2, ml3 = spots

ml4 = [ml1, ml2, ml3] 
grid = ['💣'] * 25
for i in ml4:
        grid[int(i)-1] = '✅'
response = ''
for i in range(0, 25, 5):
        response += ' '.join(grid[i:i+5])
        response += '\n'
        print(response) #only look at the last print, others are just generating phases
