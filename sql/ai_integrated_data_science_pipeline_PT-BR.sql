-- Criação da tabela PostgreSQL para armazenar os resultados analíticos processados
CREATE TABLE IF NOT EXISTS resultados_analiticos (
    id SERIAL PRIMARY KEY,
    nome_dataset VARCHAR(255),
    nome_metrica VARCHAR(255),
    valor_metrica FLOAT,
    processado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
