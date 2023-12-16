## Dicionário de Dados IFoverflow

### Tabela Campus

| Campo            | Tipo        | Descrição                           | Tamanho                   |
| ---------------- | ----------- | ----------------------------------- | ------------------------- |
| `id_campus`      | Inteiro     | Identificador único do campus       |                           |
| `nome`           | Varchar(80) | Nome do campus                      | 80 caracteres             |
| `UF_id_uf`       | Inteiro     | Identificador único do estado (UF)  |                           |


### Tabela Categorias

| Campo             | Tipo        | Descrição                   | Tamanho                   |
| ----------------- | ----------- | --------------------------- | ------------------------- |
| `id_categoria`    | Inteiro     | Identificador único da categoria |                           |
| `nome`            | Varchar(80) | Nome da categoria           | 80 caracteres             |

### Tabela Classes

| Campo           | Tipo        | Descrição                     | Tamanho                   |
| --------------- | ----------- | ----------------------------- | ------------------------- |
| `id_classe`     | Inteiro     | Identificador único da classe |                           |
| `nome`          | Varchar(80) | Nome da classe                | 80 caracteres             |
| `descricao`     | Texto       | Descrição da classe           |                           |
| `limite`        | Inteiro     | Limite associado à classe     |                           |

### Tabela UF

| Campo        | Tipo        | Descrição                   | Tamanho                   |
| ------------ | ----------- | --------------------------- | ------------------------- |
| `id_uf`      | Inteiro     | Identificador único do estado|                           |
| `nome`       | Varchar(80) | Nome do estado              | 80 caracteres             |

### Tabela Usuarios

| Campo                  | Tipo        | Descrição                                   | Tamanho                   |
| ---------------------- | ----------- | -------------------------------------------| ------------------------- |
| `id_usuario`           | Inteiro     | Identificador único do usuário              |                           |
| `nome`                 | Varchar(80) | Nome do usuário                             | 80 caracteres             |
| `votos`                | Inteiro     | Contagem de votos do usuário                |                           |
| `avatar`               | Varchar(200)| URL ou caminho do avatar do usuário         | 200 caracteres            |
| `email`                | Varchar(200)| Endereço de e-mail do usuário               | 200 caracteres            |
| `senha`                | Varchar(200)| Senha criptografada do usuário              | 200 caracteres            |
| `campus_id_campus`     | Inteiro     | Identificador único do campus associado     |                           |
| `Classe_id_classe`     | Inteiro     | Identificador único da classe do usuário    |                           |

### Tabela Perguntas

| Campo                       | Tipo        | Descrição                                   | Tamanho                   |
| --------------------------- | ----------- | -------------------------------------------| ------------------------- |
| `id_pergunta`               | Inteiro     | Identificador único da pergunta             |                           |
| `assunto`                   | Varchar(100)| Assunto da pergunta                         | 100 caracteres            |
| `descricao`                 | Texto       | Descrição detalhada da pergunta             |                           |
| `votos`                     | Inteiro     | Contagem de votos da pergunta               |                           |
| `categorias_id_categoria`    | Inteiro     | Identificador único da categoria associada  |                           |
| `usuarios_id_usuario`        | Inteiro     | Identificador único do usuário que fez a pergunta |                   |

### Tabela Respostas

| Campo                          | Tipo        | Descrição                                   | Tamanho                   |
| ------------------------------ | ----------- | -------------------------------------------| ------------------------- |
| `id_resposta`                  | Inteiro     | Identificador único da resposta             |                           |
| `descricao`                    | Texto       | Descrição detalhada da resposta             |                           |
| `votos`                        | Inteiro     | Contagem de votos da resposta               |                           |
| `aceita`                       | Tinyint     | Indicador se a resposta foi aceita (0 ou 1) |                           |
| `usuarios_id_usuario`           | Inteiro     | Identificador único do usuário que respondeu |                        |
| `perguntas_id_pergunta`        | Inteiro     | Identificador único da pergunta associada   |                           |

### Tabela Comentarios_Pergunta

| Campo                                | Tipo        | Descrição                                   | Tamanho                   |
| ------------------------------------ | ----------- | -------------------------------------------| ------------------------- |
| `id_comentarios_pergunta`           | Inteiro     | Identificador único do comentário na pergunta |                      |
| `descricao`                          | Texto       | Descrição detalhada do comentário na pergunta|                      |
| `usuarios_id_usuario`                | Inteiro     | Identificador único do usuário que comentou |                         |
| `perguntas_id_pergunta`              | Inteiro     | Identificador único da pergunta associada   |                           |

### Tabela Comentarios_Resposta

| Campo                               | Tipo        | Descrição                                    | Tamanho                   |
| ----------------------------------- | ----------- | --------------------------------------------| ------------------------- |
| `id_comentarios_resposta`           | Inteiro     | Identificador único do comentário na resposta |                     |
| `descricao`                         | Texto       | Descrição detalhada do comentário na resposta  |                     |
| `usuarios_id_usuario`               | Inteiro     | Identificador único do usuário que comentou    |                        |
| `respostas_id_resposta`             | Inteiro     | Identificador único da resposta associada      |                        |

### Tabela Votos_Pergunta

| Campo                             | Tipo        | Descrição                                     | Tamanho                   |
| --------------------------------- | ----------- | ---------------------------------------------| ------------------------- |
| `id_votos_pergunta`               | Inteiro     | Identificador único do voto na pergunta       |                           |
| `voto`                            | Tinyint     | Valor do voto (+1 para cima, -1 para baixo)   |                           |
| `usuarios_id_usuario`             | Inteiro     | Identificador único do usuário que votou      |                           |
| `perguntas_id_pergunta`           | Inteiro     | Identificador único da pergunta votada        |                           |

### Tabela Votos_Resposta

| Campo                             | Tipo        | Descrição                                    | Tamanho                   |
| --------------------------------- | ----------- | --------------------------------------------| ------------------------- |
| `id_votos_resposta`               | Inteiro     | Identificador único do voto na resposta      |                           |
| `voto`                            | Tinyint     | Valor do voto (+1 para cima, -1 para baixo)  |                           |
| `usuarios_id_usuario`             | Inteiro     | Identificador único do usuário que votou     |                           |
| `respostas_id_resposta`           | Inteiro     | Identificador único da resposta votada       |                           |
