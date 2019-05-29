import Algorithm


wuPalmer = []
shortestPath = []
LeakcockChodorow = []
target = []

with open("asset\WordSim353.tab", "r") as file:
    for line in file:
        if not line.startswith("Word"):
            text = line.split("\t")
            maxValue = Algorithm.findSimilarity(text[0], text[1])
            wuPalmer.append(maxValue[0])
            shortestPath.append(maxValue[1])
            LeakcockChodorow.append(maxValue[2])
            target.append(float(text[2].rstrip()))


    print(Algorithm.spearman(wuPalmer,target))
    print(Algorithm.pearson(wuPalmer,target))

    print(Algorithm.spearman(shortestPath,target))
    print(Algorithm.pearson(shortestPath,target))

    print(Algorithm.spearman(LeakcockChodorow,target))
    print(Algorithm.pearson(LeakcockChodorow,target))