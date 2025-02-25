# Dashboard de Paradas Mensais MDF

## Descrição
Dashboard interativo desenvolvido com Streamlit para visualização de paradas mensais MDF, focado em visualizações de dados empresariais com animações suaves de transição.

## Características
- Visualização de dados interativos
- Gráficos de impacto para MDF1 e MDF2
- Gráfico de pizza para paradas repetidas
- Animações suaves de transição entre seções
- Integração com logo personalizada

## Tecnologias Utilizadas
- Python 3.11
- Streamlit 1.42.2
- Plotly 6.0.0
- CSS Animations

## Como Fazer o Deploy
### GitHub
1. Crie um novo repositório no GitHub
2. Clone o repositório localmente:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

3. Copie os arquivos do projeto para o repositório
4. Faça commit e push das alterações:
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### Streamlit Cloud
1. Acesse [share.streamlit.io](https://share.streamlit.io)
2. Faça login com sua conta GitHub
3. Clique em "New app"
4. Selecione o repositório e configure:
   - Main file path: `main.py`
   - Python version: 3.11

### GitHub Pages
1. No seu repositório GitHub, vá para Settings > Pages
2. Na seção "Source", selecione "main" branch e pasta "/docs"
3. Clique em "Save"
4. Seu site estará disponível em: `https://seu-usuario.github.io/seu-repositorio`

## Como Fazer o Deploy pelo Android

### Usando GitHub Mobile
1. Instale o app GitHub no seu Android
2. Faça login na sua conta
3. Toque no "+" e selecione "New repository"
4. Nomeie seu repositório e torne-o público
5. Após criar, use o botão "Add file" para fazer upload dos arquivos

### Usando Streamlit Cloud (pelo navegador móvel)
1. Acesse [share.streamlit.io](https://share.streamlit.io)
2. Faça login com sua conta GitHub
3. Toque em "New app"
4. Selecione o repositório e configure:
   - Main file path: `main.py`
   - Python version: 3.11

### Configurando GitHub Pages (pelo navegador móvel)
1. Acesse seu repositório no GitHub
2. Toque nos três pontos (...) e vá em "Settings"
3. Role até encontrar "Pages"
4. Em "Source", selecione "main" e pasta "/docs"
5. Toque em "Save"

## Como Executar Localmente
1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Instale as dependências
```bash
pip install streamlit plotly
```

3. Execute o aplicativo
```bash
streamlit run main.py
```

## Demonstração
- GitHub Pages: [https://seu-usuario.github.io/seu-repositorio](https://seu-usuario.github.io/seu-repositorio)
- Streamlit Cloud: [https://share.streamlit.io/seu-usuario/seu-repositorio](https://share.streamlit.io/seu-usuario/seu-repositorio)

## Licença
Este projeto está sob a licença MIT.