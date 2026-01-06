from validate_docbr import CNPJ


def validar_cnpj(cnpj: str) -> bool:
    """Valida CNPJ."""
    return CNPJ().is_valid(cnpj)