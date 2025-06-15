### Directory Structure

Each Shortcut in this repository includes the following files:

- `{shortcut_name}.cherri`: The source file written in the Cherri language. It can also be compiled online using the [Cherri Playground](https://playground.cherrilang.org/).
- `shortcuts/{shortcut_name}.shortcut`: The executable signed Shortcut file.
- `shortcuts/{shortcut_name}.xml`: The unsigned plist file compiled from the Cherri source.

The `unsigned_original` directory contains Shortcuts created using the Apple Shortcuts app. Most Cherri files are converted from these originals. Since Cherri's compiled plist files differ from the originals, the original files are retained for reference.

### Shortcut Helpers

#### Backup and Restore

- **Backup Shortcuts**: [Backup](https://www.icloud.com/shortcuts/c30bd6cf47d8401bb87a685fd8f7797b)
- **Edit Backups**: [Edit Backups](https://www.icloud.com/shortcuts/69e70d3940614d819634afb09fcc9003)
- **Restore Backups**: [Restore Backups](https://www.icloud.com/shortcuts/cf8c143819c145269a478042ed1d7d15)

#### Advanced Management

- **Shortcut Source Tool**: [Shortcut Source Tool](https://routinehub.co/shortcut/5256/)
  - **Helper Tool**: [Shortcut Source Helper](https://routinehub.co/shortcut/10060)

The Shortcut Source Tool allows exporting unsigned Shortcut files, which can then be processed using the [Cherri CLI](https://cherrilang.org/decompilation.html) to generate `.cherri` files.

```bash
cherri --import="Exported Shortcut File.plist" # Outputs Exported_Shortcut_File.cherri
```

### Shortcuts/Cherri Basics

- **Magic Variables**  
  In Cherri, constants represent Magic Variables. Declaring a `const` does not create a new variable but references an existing one.

- **Runtime Type System**  
  Apple Shortcuts has a runtime type system. In Cherri, explicit [type coercion](https://cherrilang.org/language/types.html#type-coercion) is necessary. For instance, `"{chosen_action_var['Name']}"` converts the value to text.

- **iOS Version Compatibility**  
  Starting with iOS 18, there are changes in shortcut syntax. For compatibility, include `#define version 17` in your Cherri source code. This ensures that the compiled shortcuts function correctly on iOS versions below 18.
