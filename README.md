### Directory Structure

Each Shortcut in this repository includes the following files:

- `shortcut_name.cherri`: The source file written in Cherri language. It can also be compiled online using the [Cherri Playground](https://playground.cherrilang.org/).
- `shortcut_name.shortcut`: The signed executable Shortcut file.
- `shortcut_name.xml`: The plist file compiled from the Cherri source.

The `unsigned_original` directory contains Shortcuts created using the Apple Shortcuts app. Most Cherri files are converted from these originals. Since Cherri's compiled plist files may differ from the originals, the original files are retained for reference.

### Shortcut Helpers

#### Backup and Restore

- **Backup Shortcuts**: [Backup](https://www.icloud.com/shortcuts/c30bd6cf47d8401bb87a685fd8f7797b)
- **Edit Backups**: [Edit backups](https://www.icloud.com/shortcuts/69e70d3940614d819634afb09fcc9003)
- **Restore Backups**: [Restore backups](https://www.icloud.com/shortcuts/cf8c143819c145269a478042ed1d7d15)

#### Advanced Management

- **Shortcut Source Tool**: [Shortcut Source Tool](https://routinehub.co/shortcut/5256/)
  - **Helper Tool**: [Shortcut Source Helper](https://routinehub.co/shortcut/10060)

The Shortcut Source Tool enables exporting unsigned Shortcut files, which can then be processed using the [Cherri CLI](https://cherrilang.org/decompilation.html) to generate `.cherri` files.

```bash
cherri --import="Exported Shortcut File.plist" # Outputs Exported_Shortcut_File.cherri
```

### Cherri Basics

- Constants in Cherri represent Magic Variables. Using `const` does not create a new variable.
