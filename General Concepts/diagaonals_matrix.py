a = [[10,6,0],
    [10,5,5],
    [10,6,0]]
    #[1,1]

#top left to bottom right
diag = [ row[i] for i,row in enumerate(a) ]
# top right to bottom left
diag2 = [ row[-i-1] for i,row in enumerate(a) ]
