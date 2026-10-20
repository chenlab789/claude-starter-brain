# Windows tips — PowerShell & non-English text

Gotchas that bite when the AI runs commands on Windows, especially with Thai (or any
non-English) file names and text. Read before writing files or scripts on Windows.

## Encoding
- Write text files that contain non-English characters as **UTF-8 with BOM** if Excel
  or Windows PowerShell 5.1 will open them — without the BOM they read the file in the
  system code page and the text turns to garbage.
- CSV for Excel: `df.to_csv("file.csv", encoding="utf-8-sig")` (the `-sig` adds the BOM).
- Before printing non-English text in PowerShell:
  `[Console]::OutputEncoding = [Text.UTF8Encoding]::new()`
- Don't pass non-English strings through `python -c "..."` — write a `.py` file and run it.

## Paths
- If OneDrive backup is on, the real Desktop is `C:\Users\<you>\OneDrive\Desktop\`
  (the folder name is localized — e.g. `เดสก์ท็อป` on a Thai system).
- `Get-ChildItem` can choke on some non-English paths — `cmd /c dir` is a reliable fallback.

## PowerShell 5.1 (the built-in one)
- No `&&` — chain with `;` or `if ($?) { ... }`.
- `Out-File` defaults to UTF-16 — pass `-Encoding utf8`.
- `Remove-Item -Force` skips the Recycle Bin. Ask before using it.

## Excel files (openpyxl)
- Close the file in Excel before a script writes to it — otherwise it's locked, or
  Excel's recovery copy overwrites the script's changes later.
- `load_workbook(path)` keeps formulas. `load_workbook(path, data_only=True)` gives
  computed values but **read only** — saving it replaces every formula with its value.
- `pandas.to_excel()` on a file with formulas wipes them.

## Related
- [[00_Index]]
- [[preferences]]
