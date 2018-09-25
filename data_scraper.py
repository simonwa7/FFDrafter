import nflgame
import json

QBs = [["A.Rodgers", 1, 1, 1, 0],
	   ["R.Wilson", 1, 1, 1, 0], 
	   ["T.Brady", 1, 1, 1, 0],
	   ["C.Newton", 1, 1, 1, 0],
	   ["D.Watson", 0, 0, 1, 0], 
	   ["D.Brees", 1, 1, 1, 0],
	   ["C.Wentz", 0, 1, 1, 0],
	   ["M.Stafford", 1, 1, 1, 0], 
	   ["K.Cousins", 1, 1, 1, 0], 
	   ["A.Luck", 1, 1, 0, 0], 
	   ["B.Roethlisberger", 1, 1, 1, 0], 
	   ["A.Smith", 1, 1, 1, 0], 
	   ["P.Rivers", 1, 1, 1, 0], 
	   ["J.Garoppolo", 0, 0, 1, 0], 
	   ["M.Ryan", 1, 1, 1, 0], 
	   ["J.Goff", 0, 1, 1, 0], 
	   ["D.Prescott", 0, 1, 1, 0],
	   ["M.Mariota", 1, 1, 1, 0], 
	   ["P.Mahomes", 0, 0, 1, 0], 
	   ["B.Bortles", 1, 1, 1, 0], 
	   ["A.Dalton", 1, 1, 1, 0], 
	   ["D.Carr", 1, 1, 1, 0], 
	   ["C.Keenum", 1, 1, 1, 0],
	   ["R.Tannehill", 1, 1, 0, 0], 
	   ["M.Trubisky", 0, 0, 1, 0], 
	   ["E.Manning", 1, 1, 1, 0], 
	   ["J.Winston", 1, 1, 1, 0], 
	   ["J.Flacco", 1, 1, 1, 0],
	   ["T.Taylor", 1, 1, 1, 0], 
	   ["S.Bradford", 1, 1, 1, 0], 
	   ["S.Darnold", 0, 0, 0, 0], 
	   ["J.Allen", 0, 0, 0, 0]]

TEs = [["R.Gronkowski", 1, 1, 1, 0],
	   ["Z.Ertz", 1, 1, 1, 0], 
	   ["G.Olsen", 1, 1, 1, 0],
	   ["E.Engram", 0, 0, 1, 0],
	   ["J.Graham", 1, 1, 1, 0], 
	   ["D.Walker", 1, 1, 1, 0],
	   ["D.Njoku", 0, 0, 1, 0],
	   ["J.Doyle", 1, 1, 1, 0], 
	   ["K.Rudolph", 1, 1, 1, 0], 
	   ["O.Howard", 0, 0, 1, 0], 
	   ["A.Hooper", 0, 1, 1, 0], 
	   ["C.Brate", 1, 1, 1, 0], 
	   ["J.Reed", 1, 1, 1, 0], 
	   ["T.Eifert", 1, 1, 1, 0], 
	   ["E.Ebron", 1, 1, 1, 0], 
	   ["T.Burton", 1, 1, 1, 0], 
	   ["G.Kittle", 0, 0, 1, 0],
	   ["J.Cook", 1, 1, 1, 0], 
	   ["C.Clay", 1, 1, 1, 0], 
	   ["V.McDonald", 1, 1, 1, 0], 
	   ["R.Seals-Jones", 0, 0, 1, 0], 
	   ["B.Watson", 1, 0, 1, 0], 
	   ["A.Seferian-Jenkins", 1, 1, 1, 0],
	   ["H.Hurst", 0, 0, 0, 0]]

def getProj(player):
	if(player[1] and player[2] and player[3]):
		return [0.1*player[1][0] + 0.3*player[2][0] + 0.6*player[3][0], 
				0.1*player[1][1] + 0.3*player[2][1] + 0.6*player[3][1],
				0.1*player[1][2] + 0.3*player[2][2] + 0.6*player[3][2],
				0.1*player[1][3] + 0.3*player[2][3] + 0.6*player[3][3]]
	if(player[1] and player[2]):
		return [0.4*player[1][0] + 0.6*player[2][0], 
				0.4*player[1][1] + 0.6*player[2][1],
				0.4*player[1][2] + 0.6*player[2][2],
				0.4*player[1][3] + 0.6*player[2][3]]
	if(player[1] and player[3]):
		return [0.25*player[1][0] + 0.75*player[3][0], 
				0.25*player[1][1] + 0.75*player[3][1],
				0.25*player[1][2] + 0.75*player[3][2],
				0.25*player[1][3] + 0.75*player[3][3]]
	if(player[2] and player[3]):
		return [0.4*player[2][0] + 0.6*player[3][0], 
				0.4*player[2][1] + 0.6*player[3][1],
				0.4*player[2][2] + 0.6*player[3][2],
				0.4*player[2][3] + 0.6*player[3][3]]
	if(player[1]):
		return [player[1]]
	if(player[2]):
		return [player[2]]
	if(player[3]):
		return [player[3]]
	return [0, 0, 0, 0]

def getPoints(data):
	passing = 0
	ppa = 0
	rushing = 0 
	ppc = 0
	receiving = 0
	ppr = 0

	ppg = 0
	if((data[0]) and (data[0] != 0)):
		passing = (0.04*data[1])+(4*data[2])+(-2*data[3])+(2*data[4])
		ppa = passing/data[0]
	if((data[5]) and (data[5] != 0)):
		rushing = ((0.1*data[6])+(6*data[7])+(2*data[8])+(-2*data[14]))
		ppc = rushing/data[5]
	if((data[11]) and (data[11] != 0)):
		receiving = ((0.1*data[9])+(6*data[10])+(2*data[12]))
		ppr = receiving/data[11]
	ppg = (passing+rushing+receiving)/data[13]
	return [ppa, ppc, ppr, ppg]

def getQBDataBySeason(year, player):
	season = nflgame.games(year)
	qbs = nflgame.combine(season)
	for p in qbs:
		if(p.name == player):
			return[p.passing_att, p.passing_yds, p.passing_tds, p.passing_ints, p.passing_twoptm,
				   p.rushing_att, p.rushing_yds, p.rushing_tds, p.rushing_twoptm,
				   p.receiving_yds, p.receiving_tds, p.receiving_rec, p.receiving_twoptm,
				   p.games, p.fumbles_tot]

def getPlayerData(player):
	# For one player
	if(player[1]):
		data = getQBDataBySeason(2015, player[0])
		player[1] = getPoints(data)
	if(player[2]):
		data = getQBDataBySeason(2016, player[0])
		player[2] = getPoints(data)
	if(player[3]):
		data = getQBDataBySeason(2017, player[0])
		player[3] = getPoints(data)
	player[4] = getProj(player)
	return player

def scrapePosition(input, outfile):
	results = []
	for player in input:
		print player
		player = getPlayerData(player)
		results.append(player)

	resultJson = json.dumps(results)

	print_file = open(outfile, "w")
	print_file.write(resultJson)
	print_file.close()

def main():
	# scrapePosition(QBs, "QBData.txt")
	scrapePosition(TEs, "TEData.json")

main()