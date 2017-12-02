group_list = list(A = unlist(worldCup[1:4,2])
                  , B = unlist(worldCup[5:8,2])
                  , C = unlist(worldCup[9:12,2])
                  , D = unlist(worldCup[13:16,2])
                  , E = unlist(worldCup[17:20,2])
                  , F = unlist(worldCup[21:24,2])
                  , G = unlist(worldCup[25:28,2]) 
                  , H = unlist(worldCup[29:32,2]))

boxplot(group_list
        , names = c("A", "B", "C", "D", "E", "F", "G", "H")
        , main="World Cup 2018 Group Stage", xlab="Group", ylab="FIFA Rank", plot=F)