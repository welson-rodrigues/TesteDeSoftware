from usuarios import cadastrar_usuario, usuarios_db
from produtos import cadastrar_produto, produtos_db
from compras import realizar_compra, listar_compras, compras_db

def test_fluxo_integra_compras():
    print("\nIniciando teste de integração do sistema de compras...\n")

    # Limpa os "bancos" em memória
    usuarios_db.clear()
    produtos_db.clear()
    compras_db.clear()

    # 1. Cadastrar usuários e testar
    cadastrar_usuario(1, "Elizeu")
    cadastrar_usuario(2, "Moroni")
    cadastrar_usuario(3, "Keylly")

    # Teste
    assert usuarios_db[1] == "Elizeu"
    assert usuarios_db[2] == "Moroni"
    assert usuarios_db[3] == "Keylly"

    # 2. Cadastrar produtos e testar
    cadastrar_produto(4, "Boneca Reborn", 200.00)
    cadastrar_produto(5, "Mili Bianco Papel Higiênico", 139.95)
    cadastrar_produto(6, "Dreamgirl Peruca feminina bob", 198.99)

    # Teste
    assert produtos_db[4] == {"nome": "Boneca Reborn", "preco": 200.00}
    assert produtos_db[5] == {"nome": "Mili Bianco Papel Higiênico", "preco": 139.95}
    assert produtos_db[6] == {"nome": "Dreamgirl Peruca feminina bob", "preco": 198.99}

    # 3. Realizar compra válida
    #Elizeu
    total = realizar_compra(1, [4, 5]) # Ele comprou a boneca e o papel higiênico
    assert total == 339.95 # seria o 139.95 + 198.99 das compras

    #Moroni
    total = realizar_compra(2, [6, 4]) # Ele comprou a Peruca e boneca
    assert total == 398.99 # seria o 198.99 + 200.00 das compras

    #Keylly
    total = realizar_compra(3, [5, 6]) # Ele comprou a Peruca e o papel higiênico
    assert total == 338.94 # seria o 139.95 + 198.99 das compras

    # Verificar compra no banco
    # Elizeu
    compras = listar_compras(1)
    assert len(compras) == 1
    assert compras[0]["produtos"] == [4, 5]
    assert compras[0]["total"] == 339.95

    # Moroni
    compras = listar_compras(2)
    assert len(compras) == 1
    assert compras[0]["produtos"] == [6, 4]
    assert compras[0]["total"] == 398.99

    # Keylly
    compras = listar_compras(3)
    assert len(compras) == 1
    assert compras[0]["produtos"] == [5, 6]
    assert compras[0]["total"] == 338.94

    # 4. Tentar compra com produto inválido
    try:
        realizar_compra(1, [7])  # Usuário 1 quer comprar produto 7 que não existe
        assert False
    except ValueError as invalido:
        print(invalido)
        assert str(invalido) == "Produto 7 não encontrado."


    # 5. Verificar compras do usuário 1
    compras = listar_compras(1)
    assert len(compras) == 1
    assert compras[0]["produtos"] == [4, 5]
    assert compras[0]["total"] == 339.95
    print("Compras do usuário 1:", compras[0]["produtos"])

    # 6. Verificar um usuário que não tem compras
    cadastrar_usuario(4, "Danilo")
    compras_usuario4 = listar_compras(4)
    assert compras_usuario4 == []

# Executa o teste
if __name__ == "__main__":
    test_fluxo_integra_compras()
