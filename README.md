# 🔓 Quebra de RSA fraco e recuperação de chave AES

Este programa realiza a **quebra de um sistema RSA propositalmente fraco**, recuperando a chave simétrica usada em uma criptografia AES-256-CBC.

## 📦 Requisitos

- Python 3.x
- Biblioteca `sympy`

### Instalação da biblioteca

Execute o seguinte comando para instalar:

```bash
pip install sympy
```

## 🚀Como usar
O programa realiza automaticamente as seguintes etapas:

Fatora o valor de n (produto de dois primos pequenos)

Calcula φ(n)

Encontra d, o inverso modular de e

Decifra os blocos RSA fornecidos

Reconstrói a chave AES a partir dos códigos ASCII

## ▶️ Executar o script

```bash
python decifra_rsa.py
```

A saída mostrará a senha simétrica derivada dos blocos RSA.

Exemplo de saída esperada:

```bash
Senha simétrica AES-256: STD16
```

## 🔓 Decifrar o arquivo criptografado
Depois de obter a senha, use o comando abaixo para decifrar o arquivo .enc usando o OpenSSL:

```bash
openssl aes-256-cbc -d -a -in break_me.enc -out break_me_dec.pdf -k STD16
```

## 🔐 Observações

*A senha é reconstruída a partir dos blocos RSA usando uma tabela ASCII.

*Cada bloco RSA é interpretado como um grupo de 3 dígitos.

*A chave RSA privada é derivada automaticamente pela fatoração de n.

## 📄 Licença

Uso livre para fins educacionais, acadêmicos ou de pesquisa. Não use este código para comprometer sistemas reais sem autorização.
