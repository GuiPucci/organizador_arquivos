# organizador_arquivos — Organizador Automático de Arquivos por Extensão

O **organizador_arquivos** é um utilitário simples em Python que organiza automaticamente os arquivos de uma pasta, movendo-os para subpastas conforme suas extensões. Ideal para quem quer manter pastas organizadas sem esforço!

## Por que usar o organizador_arquivos?

- Para organizar rapidamente pastas bagunçadas, separando imagens, documentos, áudios, vídeos e arquivos compactados.
- Para evitar perder tempo movendo arquivos manualmente.
- Para manter seu computador ou workspace sempre limpo e organizado.

---

## Instalação

1. **Clone este repositório ou baixe o arquivo `organizador_de_arquivos.py`.**
2. Certifique-se de ter o Python 3 instalado.
3. (Opcional) Torne o script executável:
   ```bash
   chmod +x organizador_de_arquivos.py
   ```
4. Pronto! Você pode rodar o aplicativo a partir do terminal.

---

## Como usar

Execute o script no terminal, informando o caminho da pasta que deseja organizar:

```bash
python organizador_de_arquivos.py /caminho/da/pasta
```

Se não informar o caminho, o script pode pedir para você digitar ou usar o diretório atual.

---

### Exemplo de uso

```bash
python organizador_de_arquivos.py ~/Downloads
```

Após a execução, você verá subpastas como `Imagens`, `Documentos`, `Áudio`, `Vídeos` e `Arquivos`, cada uma contendo os arquivos correspondentes.

---

## Como funciona

- O script percorre todos os arquivos da pasta informada.
- Para cada arquivo, verifica sua extensão e move para a subpasta correspondente:
  - **Imagens:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
  - **Documentos:** `.pdf`, `.txt`, `.docx`, `.xlsx`
  - **Áudio:** `.mp3`, `.wav`, `.flac`
  - **Vídeos:** `.mp4`, `.avi`, `.mov`
  - **Arquivos:** `.zip`, `.tar`, `.gz`
- Se a subpasta não existir, ela é criada automaticamente.
- Arquivos com extensões não listadas permanecem na pasta original.

---

## Testando o script

O repositório inclui o arquivo `criar_arquivos_teste.py`, que gera 10 arquivos de cada extensão para você testar o funcionamento do organizador.

Para criar arquivos de teste:
```bash
python criar_arquivos_teste.py /caminho/da/pasta
```

Depois, execute o organizador normalmente.

---

## Processo de criação

Este projeto foi desenvolvido para ser simples, didático e útil no dia a dia.  
O objetivo é mostrar como manipular arquivos e pastas em Python, além de resolver um problema prático de organização.

---

## Contribuindo

Sugestões, melhorias e pull requests são bem-vindos!  
Se quiser adicionar suporte a mais extensões, mover arquivos por data, ou criar uma interface gráfica, fique à vontade para contribuir.

---

## Aviso

O **organizador_arquivos** move arquivos de verdade!  
Sempre revise a pasta antes de rodar o script para evitar mover arquivos importantes por engano.

---

**Mantenha suas pastas organizadas com praticidade!**
