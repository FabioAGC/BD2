from database import Graph

db = Graph('bolt+s://1a05ac504bf0c9a8d0841c00a54461f3.neo4jsandbox.com:7687','neo4j','policy-operabilities-communities')


def criar_nos():
    query = [
        'CREATE(:Regiao{nome:"Ionia" , lider:"SHEN",cor="roxo"});',
        'CREATE(:Regiao{nome:"Noxus",lider:"SWAIN"},cor="vermelho");',
        'CREATE(:Regiao{nome:"Demacia",lider:"JARVAN"},cor="amarelo");',
        'CREATE(:Regiao{nome:"Targon",lider:"AURELION"},cor="azul");',
        

        'CREATE(:Camepeao{nome: "Shen", vida: 700, mana: 0, tipo: "Tank"});',
       'CREATE(:Camepeao{nome: "Zed", vida: 500, mana: 0, tipo: "Assassino"});',
       'CREATE(:Camepeao{nome: "Akali", vida: 450, mana: 0, tipo: "Assassino"});',
       'CREATE(:Camepeao{nome: "Kennen", vida: 400, mana: 0, tipo: "Mago"});', 
     
       'CREATE(:Camepeao{nome: "Darius", vida: 650, mana: 200, tipo: "Bruiser"});',
       'CREATE(:Camepeao{nome: "Katarina", vida: 450, mana: 0, tipo: "Assassino"});',
       'CREATE(:Camepeao{nome: "Leblanc", vida: 400, mana: 400, tipo: "Mago"});',
       'CREATE(:Camepeao{nome: "Sion", vida: 750, mana: 150, tipo: "Tank"});', 
            
       'CREATE(:Camepeao{nome: "Garen", vida: 650, mana: 0, tipo: "Bruiser"});',
       'CREATE(:Camepeao{nome: "Fiora", vida: 450, mana: 200, tipo: "Bruiser"});',
       'CREATE(:Camepeao{nome: "Lux", vida: 400, mana: 450, tipo: "Mago"});',
       'CREATE(:Camepeao{nome: "Quinn", vida: 450, mana: 150, tipo: "Atirador"});', 
       
       'CREATE(:Camepeao{nome: "Taric", vida: 700, mana: 200, tipo: "Tank"});',
       'CREATE(:Camepeao{nome: "Diana", vida: 500, mana: 200, tipo: "Assassino"});',
       'CREATE(:Camepeao{nome: "Aphelios", vida: 450, mana: 100, tipo: "Atirador"});',
       'CREATE(:Camepeao{nome: "Aurelion sol", vida: 500, mana: 500, tipo: "Mago"});', 

       
               ]
    for q in query:
        db.write(query=q)


def criar_relacionamentos():
    query = [

        'MATCH(r:Regiao{nome:"Ionia"}),(c:Campeao{nome:"Shen"}) CREATE(r)-[p:POSSUI]->(c);',
        'MATCH(r:Regiao{nome:"Ionia"}),(c:Campeao{nome:"Zed"}) CREATE(r)-[p:POSSUI]->(c);',
        'MATCH(r:Regiao{nome:"Ionia"}),(c:Campeao{nome:"Akali"}) CREATE(r)-[p:POSSUI]->(c);',
        'MATCH(r:Regiao{nome:"Ionia"}),(c:Campeao{nome:"Kennen"}) CREATE(r)-[p:POSSUI]->(c);',
         
         'MATCH(r:Regiao{nome:"Noxus"}),(c:Campeao{nome:"Sion"}) CREATE(r)-[p:POSSUI]->(c);',
        'MATCH(r:Regiao{nome:"Noxus"}),(c:Campeao{nome:"Katarina"}) CREATE(r)-[p:POSSUI]->(c);',
        'MATCH(r:Regiao{nome:"Noxus"}),(c:Campeao{nome:"Leblanc"}) CREATE(r)-[p:POSSUI]->(c);',
         'MATCH(r:Regiao{nome:"Noxus"}),(c:Campeao{nome:"Darius"}) CREATE(r)-[p:POSSUI]->(c);',
        
       'MATCH(r:Regiao{nome:"Demacia"}),(c:Campeao{nome:"Garen"}) CREATE(r)-[p:POSSUI]->(c);',
       'MATCH(r:Regiao{nome:"Demacia"}),(c:Campeao{nome:"Fiora"}) CREATE(r)-[p:POSSUI]->(c);',
       'MATCH(r:Regiao{nome:"Demacia"}),(c:Campeao{nome:"Lux"}) CREATE(r)-[p:POSSUI]->(c);',
       'MATCH(r:Regiao{nome:"Demacia"}),(c:Campeao{nome:"Quinn"}) CREATE(r)-[p:POSSUI]->(c);',
         
       'MATCH(r:Regiao{nome:"Targon"}),(c:Campeao{nome:"Diana"}) CREATE(r)-[p:POSSUI]->(c);',
       'MATCH(r:Regiao{nome:"Targon"}),(c:Campeao{nome:"Taric"}) CREATE(r)-[p:POSSUI]->(c);',
       'MATCH(r:Regiao{nome:"Targon"}),(c:Campeao{nome:"Aurelion"}) CREATE(r)-[p:POSSUI]->(c);',
       'MATCH(r:Regiao{nome:"Targon"}),(c:Campeao{nome:"Aphelios"}) CREATE(r)-[p:POSSUI]->(c);',

 
    ]
    for q in query:
        db.write(query=q)


def update():
    print('UPDATE')
    result = db.execute_query('''
        MATCH(r:Regiao{nome:'Ionia'})
        SET r.lider = 'ZED'
        RETURN r.nome AS nome, r.cor AS cor, r.lider AS lider;
    ''')
    for record in result:
        print(f'Regiao= {record["nome"]} - Cor= {record["cor"]} - Lider= {record["lider"]}')


def find():
    result = db.execute_query('''
        MATCH(R:regiao{nome: 'Demacia'})-[p:POSSUI]->(c)
        RETURN c.nome AS nome, c.tipo AS tipo;
    ''')
    for record in result:
        print(f'Campeao= {record["nome"]} - Role= {record["tipo"]}')


def find_2():
    result = db.execute_query('''
        MATCH(c:Campeao)
        RETURN MAX(c.mana) AS mana;
    ''')
    for record in result:
        print(f' Mana maxima = {record["mana"]} ')


def remove():
    result = db.execute_query('''
        MATCH(c:Campeao{nome:'Katarina'})
        SET c.vida = null
        RETURN c.nome AS nome, c.vida AS vida, c.mana AS mana, c.tipo AS tipo;
    ''')
    for record in result:
        print(f'Campeao= {record["nome"]} - Vida= {record["vida"]} - Mana= {record["mana"]}')


# LIMPANDO GRAFO
def clean():
    db.execute_query("MATCH(n) DETACH DELETE n;")


def menu():
    clean()
    while True:
        print('''
                Bem vindo ao banco de dados "League of Legends"
    
                [1] - Criar nós
                [2] - Criar relacionamentos
                [3] - Realizar Busca de campeos de demacia
                [4] - Realizar busca de camepao com mais mana
                [5] - Realizar Update, mudar lider de ionia
                [6] - Realizar Remoção de um campeao de noxus
                [7] - Sair
            ''')
        result = str(input('Escolha uma opção: '))
        if result == '1':
            criar_nos()
        elif result == '2':
            criar_relacionamentos()
        elif result == '3':
            find()
        elif result == '4':
            find_2()
        elif result == '5':
            update()
        elif result == '6':
            remove()
        elif result == '7':
            print('Saindo ...')
            break
        else:
            print("Número não valido")


menu()

