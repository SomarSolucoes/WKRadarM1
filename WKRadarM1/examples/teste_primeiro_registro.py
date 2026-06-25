from WKRadarM1 import WKRadarClient
from WKRadarM1.exceptions import WKRadarError
import json

def main():
    # 1. Configuração do Cliente
    # Substitua pelos dados de conexão do seu ambiente WK Radar
    client = WKRadarClient(
        base_url="https://sua-api-wk.com.br/wk.api/",
        empresa="SUA_EMPRESA",
        username="seu_usuario",
        password="sua_senha"
    )

    try:
        print("--- TESTE DE PRIMEIRO REGISTRO ---\n")

        # 1. Teste no Módulo Empresarial (Clientes)
        print("Buscando clientes...")
        clientes = client.empresarial.buscar_clientes(Fields=["Id", "CpfCnpj"])
        if clientes and len(clientes) > 0:
            print(f"Primeiro Cliente Encontrado (de {len(clientes)}):")
            print(json.dumps(clientes[0], indent=2, ensure_ascii=False))
        else:
            print("Nenhum cliente encontrado.")

        # 2. Teste no Módulo Comercial (Fluxos)
        print("\nBuscando fluxos de pedido...")
        fluxos = client.comercial.buscar_acompanhamento_de_pedidos_fluxos()
        if fluxos and len(fluxos) > 0:
            print(f"Primeiro Fluxo Encontrado (de {len(fluxos)}):")
            print(json.dumps(fluxos[0], indent=2, ensure_ascii=False))
        else:
            print("Nenhum fluxo encontrado.")

        # 3. Teste no Módulo Financeiro (Adiantamentos)
        print("\nBuscando adiantamentos...")
        adiantamentos = client.financeiro.buscar_adiantamentos(SomenteEmAberto=True)
        if adiantamentos and len(adiantamentos) > 0:
            print(f"Primeiro Adiantamento Encontrado (de {len(adiantamentos)}):")
            print(json.dumps(adiantamentos[0], indent=2, ensure_ascii=False))
        else:
            print("Nenhum adiantamento encontrado.")

    except WKRadarError as e:
        print(f"\nErro na integração: {str(e)}")
    except Exception as e:
        print(f"\nErro inesperado: {str(e)}")

if __name__ == "__main__":
    main()
