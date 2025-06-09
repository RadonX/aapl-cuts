### Directory Structure

Each Shortcut in this repository includes the following files:

- `shortcut_name.cherri`: The Shortcut source file in Cherri language. It can also be compiled online using the [Cherri Playground](https://playground.cherrilang.org/).
- `shortcut_name.shortcut`: A signed executable Shortcut.
- `shortcut_name.xml`: The Shortcut plist file compiled from the Cherri file.


### Shortcut Helpers

#### Backup and Restore Shortcuts

- **Backup Shortcuts**: [Backup](https://www.icloud.com/shortcuts/c30bd6cf47d8401bb87a685fd8f7797b)
- **Edit Backups**: [Edit backups](https://www.icloud.com/shortcuts/69e70d3940614d819634afb09fcc9003)
- **Restore Backups**: [Restore backups](https://www.icloud.com/shortcuts/cf8c143819c145269a478042ed1d7d15)

#### Advanced Shortcut Management

- **Shortcut Source Tool**: [Shortcut Source Tool](https://routinehub.co/shortcut/5256/)
  - **Helper Tool**: [Shortcut Source Helper](https://routinehub.co/shortcut/10060)

The Shortcut Source Tool allows exporting unsigned Shortcut files, which can be processed using the [Cherri CLI](https://cherrilang.org/decompilation.html) to convert them into `.cherri` files.

```bash
cherri --import="Exported Shortcut File.plist" # Outputs Exported_Shortcut_File.cherri
```
