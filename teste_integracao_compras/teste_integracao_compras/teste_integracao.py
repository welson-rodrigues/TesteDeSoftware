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


    # 4. Tentar compra com produto inválido


    # 5. Verificar compras do usuário 1


    # 6. Verificar um usuário que não tem compras

# Executa o teste
if __name__ == "__main__":
    test_fluxo_integra_compras()
