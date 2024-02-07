import random

def generate_titulo_eleitoral(estado=None):
    uf_codes = {
        "SP": "01",
        "MG": "02",
        "RJ": "03",
        "RS": "04",
        "BA": "05",
        "PR": "06",
        "CE": "07",
        "PE": "08",
        "SC": "09",
        "GO": "10",
        "MA": "11",
        "PB": "12",
        "PA": "13",
        "ES": "14",
        "PI": "15",
        "RN": "16",
        "AL": "17",
        "MT": "18",
        "MS": "19",
        "DF": "20",
        "SE": "21",
        "AM": "22",
        "RO": "23",
        "AC": "24",
        "AP": "25",
        "RR": "26",
        "TO": "27",
        "ZZ": "28",  # Exterior
    }
    
    if estado is None:
        estado = "ZZ"  # Default to exterior if state is not specified
    
    if estado.upper() not in uf_codes:
        raise ValueError("Estado não identificado")

    numero_sequencial = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    uf = uf_codes[estado.upper()]
    titulo_eleitoral = numero_sequencial + uf

    # Calcula os dígitos verificadores
    v1 = sum(int(titulo_eleitoral[i]) * (i + 2) for i in range(8)) % 11
    v2 = (int(uf) + v1) % 11

    return titulo_eleitoral + str(v1) + str(v2)