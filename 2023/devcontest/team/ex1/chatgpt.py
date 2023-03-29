def make_symmetric_trophy(W, H, trophy):
    # Calculer le nombre de morceaux manquants pour rendre le trophée symétrique
    missing_pieces = 0
    for i in range(H):
        for j in range(W//2):
            if trophy[i][j] == '#' and trophy[i][W-1-j] != '#':
                missing_pieces += 1
                trophy[i] = trophy[i][:W-1-j] + '#' + trophy[i][W-j:]
            elif trophy[i][j] != '#' and trophy[i][W-1-j] == '#':
                missing_pieces += 1
                trophy[i] = trophy[i][:j] + '#' + trophy[i][j+1:]
            elif trophy[i][j] != '#' and trophy[i][W-1-j] != '#':
                missing_pieces += 2
                trophy[i] = trophy[i][:j] + '##' + trophy[i][j+1:W-1-j] + '##' + trophy[i][W-j:]
    
    # Ajouter les morceaux manquants pour rendre le trophée symétrique
    for i in range(H):
        for j in range(W//2, W):
            if trophy[i][j] != '#':
                trophy[i] = trophy[i][:j] + '#' + trophy[i][j+1:W-j-1] + '#' + trophy[i][W-j:]
    
    return trophy

# Entrée
W, H = map(int, input().split())
trophy = []
for i in range(H):
    trophy.append(input())

# Résolution
trophy = make_symmetric_trophy(W, H, trophy)

# Sortie
for row in trophy:
    print(row)