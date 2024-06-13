# Projeto IoT: Integração de Dados de Hardwares Libelium com PiVision

## Introdução

Este projeto visa integrar dados coletados por dispositivos IoT da Libelium com o PiVision, uma plataforma de visualização de dados. Através de um script Python, os dados armazenados em um banco de dados são processados e enviados para o PiVision para monitoramento e análise.

## Objetivo do Projeto

O objetivo é criar um sistema que possa:
- Coletar dados de sensores IoT da Libelium armazenados em um banco de dados.
- Processar esses dados conforme necessário.
- Enviar os dados processados para o PiVision, onde podem ser visualizados e analisados em tempo real.

## Descrição do Script

O script é desenvolvido em Python e realiza as seguintes funções principais:
1. **Conexão com o Banco de Dados**: O script se conecta ao banco de dados que armazena os dados dos sensores da Libelium.
2. **Extração de Dados**: Ele extrai dados relevantes para o monitoramento.
3. **Processamento dos Dados**: Opcionalmente, os dados podem ser filtrados ou transformados.
4. **Envio para PiVision**: Os dados processados são enviados para o PiVision via API ou outro método de integração suportado.

## Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Banco de Dados**: Utilizado para armazenar os dados dos sensores Libelium.
- **Libelium**: Plataforma de hardware para IoT, responsável pela coleta inicial dos dados.
- **PiVision**: Plataforma de visualização de dados utilizada para monitoramento e análise.
- **Bibliotecas Python**: `requests` para comunicação com APIs, `pandas` para manipulação de dados, entre outras.

## Funcionamento do Sistema

### 1. Coleta de Dados

Os dispositivos Libelium coletam dados ambientais e os armazenam em um banco de dados. Estes dados podem incluir informações como temperatura, umidade, qualidade do ar, etc.

### 2. Processamento

O script Python se conecta ao banco de dados e extrai os dados relevantes. Durante a extração, os dados podem ser filtrados ou transformados para se adequarem aos requisitos do PiVision.

### 3. Envio para o PiVision

Após o processamento, os dados são enviados para o PiVision. Isso pode ser feito usando a API do PiVision ou outros métodos de integração suportados pela plataforma. O PiVision, então, visualiza os dados recebidos em tempo real, permitindo uma análise rápida e eficaz.
