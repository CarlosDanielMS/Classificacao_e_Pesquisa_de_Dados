from jogo import Jogo
from busca_jogos import MotorBuscaJogos

# Instanciar o motor de busca
motor_busca = MotorBuscaJogos()

# Adicionar jogos
motor_busca.adicionar_jogo(Jogo(1, "League of Legends", "Riot Games", 30, ["MOBA", "Intenso"]))
motor_busca.adicionar_jogo(Jogo(2, "Valorant", "Riot Games", 60, ["FPS", "Competitivo"]))
motor_busca.adicionar_jogo(Jogo(3, "The Witcher 3", "CD Projekt Red", 100, ["RPG", "Aventura"]))
motor_busca.adicionar_jogo(Jogo(4, "Minecraft", "Mojang Studios", 50, ["Sandbox", "Criativo"]))
motor_busca.adicionar_jogo(Jogo(5, "FIFA 24", "EA Sports", 150, ["Esportes", "Simulação"]))
motor_busca.adicionar_jogo(Jogo(6, "Cyberpunk 2077", "CD Projekt Red", 200, ["RPG", "Futurista"]))
motor_busca.adicionar_jogo(Jogo(7, "Among Us", "Innersloth", 20, ["Multiplayer", "Estratégia"]))
motor_busca.adicionar_jogo(Jogo(8, "Hollow Knight", "Team Cherry", 80, ["Indie", "Metroidvania"]))
motor_busca.adicionar_jogo(Jogo(9, "God of War", "Santa Monica Studio", 250, ["Ação", "Aventura"]))
motor_busca.adicionar_jogo(Jogo(10, "Dark Souls 3", "FromSoftware", 320, ["RPG", "Difícil"]))
motor_busca.adicionar_jogo(Jogo(11, "RPG de ação", "Diablo 4", 400, ["RPG", "Ação"]))
motor_busca.adicionar_jogo(Jogo(12, "Ação Intenso", "call of duty ops 6", 350, ["Ação"]))
motor_busca.adicionar_jogo(Jogo(13, "Estratégia", "Hearthstone", 30, ["Estratégia", "Cartas"]))


# Buscar por preço
print("Jogos com preço R$100: \n", motor_busca.buscar_por_preco(100))

# Buscar por faixa de preço
print("Jogos entre R$50 e R$150:\n", motor_busca.busca_por_faixa_preco(50, 150))

# Buscar por gênero
print("Jogos do gênero RPG:\n", motor_busca.buscar_por_genero("RPG"))
print("Jogos do gênero Ação:\n", motor_busca.buscar_por_genero("Ação"))
