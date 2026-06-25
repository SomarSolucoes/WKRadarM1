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
        print("--- EXEMPLO DE USO WKRadarM1 ---\n")

        # 1. Busca de Clientes (Módulo Empresarial)
        print("Buscando clientes...")
        clientes = client.empresarial.buscar_clientes(Fields=["Id", "CpfCnpj"])
        if clientes:
            print(f"Primeiro Cliente Encontrado:")
            print(json.dumps(clientes[0], indent=2, ensure_ascii=False))

        # 2. Busca de Fluxos de Pedido (Módulo Comercial)
        print("\nBuscando fluxos de pedido...")
        fluxos = client.comercial.buscar_acompanhamento_de_pedidos_fluxos()
        if fluxos:
            print(f"Primeiro Fluxo Encontrado:")
            print(json.dumps(fluxos[0], indent=2, ensure_ascii=False))

    except WKRadarError as e:
        print(f"\nErro na integração: {str(e)}")
    except Exception as e:
        print(f"\nErro inesperado: {str(e)}")

if __name__ == "__main__":
    main()
