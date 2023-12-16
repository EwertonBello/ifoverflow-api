## Dicionário de Dados IFoverflow

### Tabela Campus
| Campo          | Tipo        | Restrições                              |
| -------------- | ----------- | ----------------------------------------|
| `id_campus`    | Inteiro     | Not Null, Auto Incremento, Chave Primária|
| `nome`         | Varchar(80) | Not Null                                |
| `UF_id_uf`     | Inteiro     | Not Null, Chave Estrangeira (fk_campus_UF1), referenciando `uf.id_uf` ON DELETE CASCADE ON UPDATE CASCADE|

### Tabela Categorias
| Campo           | Tipo        | Restrições                              |
| --------------- | ----------- | ----------------------------------------|
| `id_categoria`  | Inteiro     | Not Null, Auto Incremento, Chave Primária|
| `nome`          | Varchar(80) | Not Null                                |

### Tabela Classes
| Campo           | Tipo        | Restrições                              |
| --------------- | ----------- | ----------------------------------------|
| `id_classe`     | Inteiro     | Not Null, Auto Incremento, Chave Primária|
| `nome`          | Varchar(80) | Not Null                                |
| `descricao`     | Texto       | Not Null                                |
| `limite`        | Inteiro     | Not Null                                |

### Tabela UF
| Campo        | Tipo        | Restrições                              |
| ------------ | ----------- | ----------------------------------------|
| `id_uf`      | Inteiro     | Not Null, Auto Incremento, Chave Primária|
| `nome`       | Varchar(80) | Not Null                                |

### Tabela Usuarios
| Campo                  | Tipo        | Restrições                                                 |
| ---------------------- | ----------- | ----------------------------------------------------------|
| `id_usuario`           | Inteiro     | Not Null, Auto Incremento, Chave Primária                  |
| `nome`                 | Varchar(80) | Not Null                                                   |
| `votos`                | Inteiro     | Not Null, Padrão: 0                                       |
| `avatar`               | Varchar(200)| Not Null                                                   |
| `email`                | Varchar(200)| Not Null                                                   |
| `senha`                | Varchar(200)| Not Null                                                   |
| `campus_id_campus`     | Inteiro     | Not Null, Chave Estrangeira (fk_usuarios_campus1), referenciando `campus.id_campus` ON DELETE CASCADE ON UPDATE CASCADE |
| `Classe_id_classe`     | Inteiro     | Not Null, Padrão: 1, Chave Estrangeira (fk_usuarios_Classe1), referenciando `classes.id_classe`|

### Tabela Perguntas
| Campo                       | Tipo        | Restrições                                                           |
| --------------------------- | ----------- | --------------------------------------------------------------------|
| `id_pergunta`               | Inteiro     | Not Null, Auto Incremento, Chave Primária                            |
| `assunto`                   | Varchar(100)| Not Null                                                             |
| `descricao`                 | Texto       | Not Null                                                             |
| `votos`                     | Inteiro     | Not Null, Padrão: 0                                                  |
| `categorias_id_categoria`    | Inteiro     | Not Null, Chave Estrangeira (fk_perguntas_categorias2), referenciando `categorias.id_categoria` ON DELETE CASCADE ON UPDATE CASCADE |
| `usuarios_id_usuario`        | Inteiro     | Not Null, Chave Estrangeira (fk_perguntas_usuarios1), referenciando `usuarios.id_usuario` ON DELETE CASCADE ON UPDATE CASCADE  |

### Tabela Respostas
| Campo                          | Tipo        | Restrições                                                               |
| ------------------------------ | ----------- | ------------------------------------------------------------------------|
| `id_resposta`                  | Inteiro     | Not Null, Auto Incremento, Chave Primária                                |
| `descricao`                    | Texto       | Not Null                                                                 |
| `votos`                        | Inteiro     | Not Null, Padrão: 0                                                      |
| `aceita`                       | Tinyint     | Not Null, Padrão: 0 (indicando se a resposta foi aceita ou não)          |
| `usuarios_id_usuario`           | Inteiro     | Not Null, Chave Estrangeira (fk_respostas_usuarios1), referenciando `usuarios.id_usuario` ON DELETE CASCADE ON UPDATE CASCADE |
| `perguntas_id_pergunta`        | Inteiro     | Not Null, Chave Estrangeira (fk_respostas_perguntas1), referenciando `perguntas.id_pergunta` ON DELETE CASCADE ON UPDATE CASCADE |

### Tabela Comentarios_Pergunta
| Campo                                | Tipo        | Restrições                                                                   |
| ------------------------------------ | ----------- | ------------------------------------------------------------------------------|
| `id_comentarios_pergunta`           | Inteiro     | Not Null, Auto Incremento, Chave Primária                                    |
| `descricao`                          | Texto       | Not Null                                                                     |
| `usuarios_id_usuario`                | Inteiro     | Not Null, Chave Estrangeira (fk_comentarios_pergunta_usuarios1), referenciando `usuarios.id_usuario` ON DELETE CASCADE ON UPDATE CASCADE |
| `perguntas_id_pergunta`              | Inteiro     | Not Null, Chave Estrangeira (fk_comentarios_pergunta_perguntas1), referenciando `perguntas.id_pergunta` ON DELETE CASCADE ON UPDATE CASCADE |

### Tabela Comentarios_Resposta
| Campo                               | Tipo        | Restrições                                                                   |
| ----------------------------------- | ----------- | ------------------------------------------------------------------------------|
| `id_comentarios_resposta`           | Inteiro     | Not Null, Auto Incremento, Chave Primária                                    |
| `descricao`                         | Texto       | Not Null                                                                     |
| `usuarios_id_usuario`               | Inteiro     | Not Null, Chave Estrangeira (fk_comentarios_resposta_usuarios1), referenciando `usuarios.id_usuario` ON DELETE CASCADE ON UPDATE CASCADE |
| `respostas_id_resposta`             | Inteiro     | Not Null, Chave Estrangeira (fk_comentarios_resposta_respostas1), referenciando `respostas.id_resposta` ON DELETE CASCADE ON UPDATE CASCADE |

### Tabela Votos_Pergunta
| Campo                             | Tipo        | Restrições                                                                   |
| --------------------------------- | ----------- | ------------------------------------------------------------------------------|
| `id_votos_pergunta`               | Inteiro     | Not Null, Auto Incremento, Chave Primária                                    |
| `voto`                            | Tinyint     | Not Null                                                                     |
| `usuarios_id_usuario`             | Inteiro     | Not Null, Chave Estrangeira (fk_votos_pergunta_usuarios1), referenciando `usuarios.id_usuario` ON DELETE CASCADE |
| `perguntas_id_pergunta`           | Inteiro     | Not Null, Chave Estrangeira (fk_votos_pergunta_perguntas1), referenciando `perguntas.id_pergunta` ON DELETE CASCADE |

### Tabela Votos_Resposta
| Campo                             | Tipo        | Restrições                                                                   |
| --------------------------------- | ----------- | ------------------------------------------------------------------------------|
| `id_votos_resposta`               | Inteiro     | Not Null, Auto Incremento, Chave Primária                                    |
| `voto`                            | Tinyint     | Not Null                                                                     |
| `usuarios_id_usuario`             | Inteiro     | Not Null, Chave Estrangeira (fk_votos_resposta_usuarios1), referenciando `usuarios.id_usuario` ON DELETE CASCADE |
| `respostas_id_resposta`           | Inteiro     | Not Null, Chave Estrangeira (fk_votos_resposta_respostas1), referenciando `respostas.id_resposta` ON DELETE CASCADE |

