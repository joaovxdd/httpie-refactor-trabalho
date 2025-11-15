import requests

def send_request(url: str, method: str, data: dict) -> str:
    """
    Envia uma requisição HTTP com tratamento de erro e timeout.
    """
    try:
        response = requests.request(method, url, data=data, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        raise RuntimeError(f"Erro ao enviar requisição: {e}")
