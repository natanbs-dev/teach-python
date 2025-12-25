Para trocar o gerenciador de arquivos padrão do GNOME para o Dolphin, você pode combinar comandos de terminal com algumas configurações manuais. É importante saber que o Nautilus está fortemente integrado ao GNOME, então não é recomendado removê-lo.

### 🔧 Método Principal: Usando o Comando `xdg-mime`
Este é o método mais direto e amplamente sugerido para definir o Dolphin como padrão:

1.  **Instale o Dolphin** (se ainda não o fez):
    ```bash
    sudo apt install dolphin konsole
    ```
    *O Konsole é recomendado para melhor integração, pois o Dolphin é um aplicativo do KDE (Qt).*

2.  **Defina o Dolphin como gerenciador padrão para pastas**:
    Execute o seguinte comando no terminal:
    ```bash
    xdg-mime default dolphin.desktop inode/directory application/x-gnome-saved-search
    ```
    Este comando configura o Dolphin para abrir diretórios e buscas salvas.

### ⚙️ Configurações Adicionais para Melhor Integração
Para que a mudança funcione em mais situações (como ao abrir pastas a partir do navegador), siga estes passos:

1.  **Defina manualmente a associação em arquivos específicos**:
    *   No **Dolphin**, clique com o botão direito em qualquer arquivo.
    *   Vá em **"Abrir com" > "Escolher outro aplicativo"**.
    *   Selecione **"Dolphin"** (ou outro aplicativo desejado para aquele tipo de arquivo).
    *   **Marque a caixa** `"Lembrar associação de aplicativo para todos os arquivos deste tipo"`.
    *   Clique em **"Abrir"**.

2.  **Verifique e edite o arquivo de associações MIME**:
    O sistema gerencia os aplicativos padrão através do arquivo `~/.config/mimeapps.list`. Você pode inspecioná-lo e editar manualmente se necessário.
    *   Abra o terminal e veja o conteúdo do arquivo:
        ```bash
        cat ~/.config/mimeapps.list
        ```
    *   Procure por linhas que contenham `inode/directory=` e certifique-se de que estejam definidas como `dolphin.desktop`.

### 💡 Considerações e Observações Importantes
*   **Não remova o Nautilus**: Remover o **Nautilus** pode quebrar partes do seu ambiente GNOME, pois ele está profundamente integrado. A abordagem segura é instalar o Dolphin por cima e defini-lo como padrão.
*   **Integração visual (tema escuro)**: Como o Dolphin usa as bibliotecas **Qt** e o GNOME usa **GTK**, o Dolphin pode não seguir automaticamente o tema claro/escuro do seu sistema. Existem ferramentas como o `qt5ct` para ajustar a aparência, mas isso envolve configuração adicional.
*   **Desktop (área de trabalho)**: Alterar o gerenciador de arquivos **pode afetar a funcionalidade da área de trabalho**. Alguns usuários preferem desabilitar os ícones na área de trabalho do GNOME para evitar conflitos.
*   **Possíveis limitações**: Em alguns casos muito específicos, aplicativos (como o Firefox) podem ignorar a configuração global e continuar usando o antigo gerenciador. Reiniciar a sessão ou o computador após fazer as mudanças pode ajudar.

Em resumo, use o comando `xdg-mime` principal e complemente com as configurações manuais no Dolphin e na verificação do arquivo MIME para garantir que a mudança seja aplicada de forma ampla.

Se você quiser ajustar a aparência visual do Dolphin para combinar melhor com o tema do seu GNOME, posso te ajudar a encontrar mais detalhes sobre isso.