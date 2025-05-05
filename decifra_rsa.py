from sympy import factorint, mod_inverse

# --- Dados iniciais
n = 46222907
e = 65537
cipher_blocks = [35191279, 28831642, 6113081, 36161830]

# --- Etapa 1: Fatorar n
factors = factorint(n)
p, q = list(factors.keys())
print(f"[+] Fatores de n: p = {p}, q = {q}")

# --- Etapa 2: Calcular phi(n)
phi_n = (p - 1) * (q - 1)
print(f"[+] φ(n) = {phi_n}")

# --- Etapa 3: Calcular d (chave privada)
d = mod_inverse(e, phi_n)
print(f"[+] d (chave privada) = {d}")

# --- Etapa 4: Decifrar os blocos
dec_blocks = [pow(c, d, n) for c in cipher_blocks]
print(f"[+] Blocos decifrados: {dec_blocks}")

# --- Etapa 5: Juntar blocos em string e quebrar em grupos de dois
num_str = ''.join(f"{block:03d}" for block in dec_blocks)  # garantir 3 dígitos por bloco
pairs = [num_str[i:i+2] for i in range(0, len(num_str), 2)]
print(f"[+] Pares: {pairs}")

# --- Etapa 6: Converter pares em caracteres ASCII
# ignorar "00" no final, se houver
ascii_chars = [chr(int(p)) for p in pairs if p != "00"]
password = ''.join(ascii_chars)

print(f"[+] Senha simétrica AES-256: {password}")
