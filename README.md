# Shell Manager / ឧបករណ៍គ្រប់គ្រង Shell

[ខ្មែរ](#khmer) | [English](#english)

---

<div id="khmer">

# ឧបករណ៍គ្រប់គ្រង Shell

ឧបករណ៍ដែលបង្កើតឡើងដោយ Python សម្រាប់គ្រប់គ្រង និងដំណើរការ shell scripts ជាមួយនឹងការជ្រើសរើសអន្តរកម្ម និងការគ្រប់គ្រងការអនុញ្ញាតដោយស្វ័យប្រវត្តិ។ ល្អសម្រាប់អ្នកអភិវឌ្ឍន៍ដែលប្រើ shell scripts ញឹកញាប់សម្រាប់កិច្ចការអភិវឌ្ឍន៍ដូចជាការផ្លាស់ប្តូរអ្នកប្រើ Git ការកំណត់ឡើងវិញនូវ IDE និងការគ្រប់គ្រងមូលដ្ឋានទិន្នន័យ។

---

## 🚀 មុខងារ

- **ការជ្រើសរើស Script អន្តរកម្ម:** រុករក និងដំណើរការ `.sh` scripts ពីថត `shell_file/` បានយ៉ាងងាយស្រួលដោយប្រើចំណុចប្រទាក់ប៊ូតុងវិទ្យុដែលយល់បាន។
- **ការគ្រប់គ្រងការអនុញ្ញាតដោយស្វ័យប្រវត្តិ:** ស្នើឱ្យធ្វើឱ្យ scripts អាចដំណើរការបានមុនពេលដំណើរការ ធានាការដំណើរការរលូន។
- **ការរៀបចំការអនុញ្ញាតច្រើន:** ឧបករណ៍ម្តងមួយដងដើម្បីធ្វើឱ្យ shell scripts ទាំងអស់អាចដំណើរការបានជាមួយនឹងការបញ្ជាក់ជាក្រុម ឬបុគ្គល។
- **សុវត្ថិភាព និងអនាមិក:** តែងតែស្នើមុនពេលផ្លាស់ប្តូរការអនុញ្ញាត គ្រប់គ្រងកំហុសយ៉ាងរលូនជាមួយនឹងសារកំហុសច្បាស់លាស់។
- **ការរួមបញ្ចូល `uv`:** ដំណើរការយ៉ាងរលូនជាមួយនឹង [uv](https://github.com/astral-sh/uv) Python package manager សម្រាប់ការអភិវឌ្ឍន៍ Python ទំនើប។
- **ការរុករកដោយព្រួញ:** ការគាំទ្រ keyboard ពេញលេញជាមួយនឹងព្រួញសម្រាប់ការរុករក និងការជ្រើសរើស។

---

## 📁 រចនាសម្ព័ន្ធគម្រោង

```
sh_manager/
├── main.py                 # ចំណុចចូលកម្មវិធីគោល
├── make_executable.py      # ឧបករណ៍ការអនុញ្ញាតច្រើន
├── pyproject.toml          # ការកំណត់រចនាសម្ព័ន្ធ និងការពឹងផ្អែកគម្រោង
├── uv.lock                 # ឯកសារ lock សម្រាប់ uv package manager
├── data/
│   └── git_user_configs.json  # ការកំណត់រចនាសម្ព័ន្ធអ្នកប្រើ Git
└── shell_file/
    ├── switch_git_user.sh      # ឧបករណ៍ផ្លាស់ប្តូរអ្នកប្រើ Git
    ├── reset_intellijidea.sh   # Script កំណត់ឡើងវិញនូវ IntelliJ IDEA
    └── reset_navicate.sh       # Script កំណត់ឡើងវិញនូវ Navicat database
```

---

## 🛠️ ការដំឡើង

### តម្រូវការមុន

- Python 3.11.11 ឬខ្ពស់ជាង
- [uv](https://github.com/astral-sh/uv) package manager (ណែនាំ)

### ការរៀបចំ

1. Clone ឬទាញយក repository នេះ
2. ចូលទៅកាន់ថតគម្រោង
3. ដំឡើងការពឹងផ្អែកដោយប្រើ uv:
   ```bash
   uv sync
   ```

---

## 🚀 ការប្រើប្រាស់

### ការដំណើរការកម្មវិធីគោល

ចាប់ផ្តើមឧបករណ៍គ្រប់គ្រង shell script អន្តរកម្ម:

```bash
# ប្រើ uv
uv run main.py

# ឬដំឡើង និងដំណើរការជា script
uv run sh-manager
```

### ការរៀបចំការអនុញ្ញាតច្រើន

ធ្វើឱ្យ shell scripts ទាំងអស់អាចដំណើរការបានក្នុងម្តង:

```bash
# ប្រើ uv
uv run make_executable.py

# ឬដំឡើង និងដំណើរការជា script
uv run make-executable
```

---

## 📋 Scripts ដែលមាន

### 1. `switch_git_user.sh`

ផ្លាស់ប្តូររវាងការកំណត់រចនាសម្ព័ន្ធអ្នកប្រើ Git ផ្សេងៗគ្នាដែលកំណត់ក្នុង `data/git_user_configs.json`។

**ការកំណត់រចនាសម្ព័ន្ធបច្ចុប្បន្ន:**

- `@username` (username@example.com)
- `@username2` (username2@example.com)

### 2. `reset_intellijidea.sh`

កំណត់ឡើងវិញនូវការកំណត់ និង cache របស់ IntelliJ IDEA។ មានប្រយោជន៍សម្រាប់ដោះស្រាយបញ្ហា IDE។

### 3. `reset_navicate.sh`

កំណត់ឡើងវិញនូវការកំណត់ការតភ្ជាប់មូលដ្ឋានទិន្នន័យ Navicat និង cache។

---

## 🎮 ចំណុចប្រទាក់អន្តរកម្ម

កម្មវិធីផ្តល់ចំណុចប្រទាក់ប៊ូតុងវិទ្យុដែលយល់បាន:

- **ព្រួញ ↑/↓:** រុករករវាង scripts
- **ព្រួញ →:** ជ្រើសរើស script (ការជ្រើសរើសប៊ូតុងវិទ្យុ)
- **Enter:** ដំណើរការ script ដែលបានជ្រើសរើស
- **q:** ចាកចេញពីកម្មវិធី

ឧទាហរណ៍ចំណុចប្រទាក់:

```
ប្រើ ↑/↓ ដើម្បីផ្លាស់ទី, → ដើម្បីជ្រើសរើស, Enter ដើម្បីដំណើរការ, q ដើម្បីចាកចេញ។

> [x] switch_git_user.sh
  [ ] reset_intellijidea.sh
  [ ] reset_navicate.sh

រុករកដោយព្រួញ។ ជ្រើសរើសដោយ →, ដំណើរការដោយ Enter, ចាកចេញដោយ q។
```

---

## 🔧 ការកំណត់រចនាសម្ព័ន្ធ

### ការកំណត់រចនាសម្ព័ន្ធអ្នកប្រើ Git

កែសម្រួល `data/git_user_configs.json` ដើម្បីបន្ថែម ឬកែប្រែ profile អ្នកប្រើ Git:

**ចំណាំ:** ប្រសិនបើឯកសារ `git_user_configs.json` មិនមានទេ សូមចម្លងពី `data/git_user_configs_example.json` ទៅ `data/git_user_configs.json` និងកែសម្រួលតាមតម្រូវការរបស់អ្នក។

```json
[
  {
    "name": "ឈ្មោះរបស់អ្នក",
    "email": "email.របស់អ្នក@example.com"
  }
]
```

### ការបន្ថែម Scripts ថ្មី

1. ដាក់ `.sh` script របស់អ្នកក្នុងថត `shell_file/`
2. ត្រូវប្រាកដថា script មាន shebang ត្រឹមត្រូវ (`#!/bin/bash`) និងការអនុញ្ញាត
3. Script នឹងបង្ហាញដោយស្វ័យប្រវត្តិក្នុងចំណុចប្រទាក់ជ្រើសរើស

---

## 🛡️ មុខងារសុវត្ថិភាព

- **ការបញ្ជាក់ការអនុញ្ញាត:** តែងតែស្នើមុនពេលធ្វើឱ្យឯកសារអាចដំណើរការបាន
- **ការគ្រប់គ្រងកំហុស:** ការគ្រប់គ្រងកំហុសយ៉ាងរលូនជាមួយនឹងសារកំហុសច្បាស់លាស់
- **ការដំណើរការមានសុវត្ថិភាព:** Scripts ដំណើរការក្នុងបរិស្ថានដែលគ្រប់គ្រងបាន
- **ការផ្ទៀងផ្ទាត់ការបញ្ចូល:** ការផ្ទៀងផ្ទាត់ត្រឹមត្រូវនូវការបញ្ចូលរបស់អ្នកប្រើ

---

## 🔧 ការអភិវឌ្ឍន៍

### ការរៀបចំគម្រោង

```bash
# ដំឡើងការពឹងផ្អែកអភិវឌ្ឍន៍
uv sync

# ដំណើរការកម្មវិធីគោល
uv run main.py

# ដំណើរការឧបករណ៍ការអនុញ្ញាត
uv run make_executable.py
```

### ការពឹងផ្អែក

- **Python 3.11.11+:** មុខងារ និងដំណើរការ Python ទំនើប
- **Standard Library តែប៉ុណ្ណោះ:** មិនត្រូវការការពឹងផ្អែកខាងក្រៅ
- **uv:** ការគ្រប់គ្រង package Python ទំនើប

---

## 📝 អាជ្ញាប័ណ្ណ

គម្រោងនេះគឺជា open source និងមានជាមួយអាជ្ញាប័ណ្ណ MIT។

---

## 🤝 ការរួមចំណែក

1. Fork repository
2. បង្កើត feature branch
3. ធ្វើការផ្លាស់ប្តូររបស់អ្នក
4. ធ្វើតេស្តយ៉ាងហ្មត់ចត់
5. ដាក់ស្នើ pull request

---

## 🐛 ការដោះស្រាយបញ្ហា

### បញ្ហាទូទៅ

**Script មិនអាចដំណើរការបាន:**

- ដំណើរការ `uv run make-executable` ដើម្បីរៀបចំការអនុញ្ញាត
- ឬដំណើរការដោយដៃ `chmod +x shell_file/your_script.sh`

**ការអនុញ្ញាតត្រូវបានបដិសេធ:**

- ត្រូវប្រាកដថាអ្នកមានការអនុញ្ញាតសរសេរទៅថត `shell_file/`
- ពិនិត្យមើលថា script files មិនមែនជា read-only

**Script មិនត្រូវបានរកឃើញ:**

- ផ្ទៀងផ្ទាត់ថា script មាននៅក្នុងថត `shell_file/`
- ពិនិត្យមើលថា file មាន extension `.sh`

---

## 📞 ការគាំទ្រ

សម្រាប់បញ្ហា សំណួរ ឬការរួមចំណែក សូមបើក issue នៅលើ repository គម្រោង។

</div>

---

<div id="english">

# Shell Manager

A Python-based tool for managing and running shell scripts with interactive selection and automatic permission handling. Perfect for developers who frequently use shell scripts for development tasks like Git user switching, IDE resets, and database management.

---

## 🚀 Features

- **Interactive Script Selection:** Easily browse and run `.sh` scripts from the `shell_file/` directory using an intuitive radio-button interface.
- **Automatic Permission Handling:** Prompts to make scripts executable before running, ensuring smooth execution.
- **Bulk Permission Setup:** One-time utility to make all shell scripts executable with batch or individual confirmation.
- **Safe & Secure:** Always asks before changing permissions; handles errors gracefully with proper error messages.
- **`uv` Integration:** Works seamlessly with the [uv](https://github.com/astral-sh/uv) Python package manager for modern Python development.
- **Arrow Key Navigation:** Full keyboard support with arrow keys for navigation and selection.

---

## 📁 Project Structure

```
sh_manager/
├── main.py                 # Main application entry point
├── make_executable.py      # Bulk permission utility
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Lock file for uv package manager
├── data/
│   └── git_user_configs.json  # Git user configurations
└── shell_file/
    ├── switch_git_user.sh      # Git user switching utility
    ├── reset_intellijidea.sh   # IntelliJ IDEA reset script
    └── reset_navicate.sh       # Navicat database reset script
```

---

## 🛠️ Installation

### Prerequisites

- Python 3.11.11 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)

### Setup

1. Clone or download this repository
2. Navigate to the project directory
3. Install dependencies using uv:
   ```bash
   uv sync
   ```

---

## 🚀 Usage

### Running the Main Application

Start the interactive shell script manager:

```bash
# Using uv
uv run main.py

# Or install and run as a script
uv run sh-manager
```

### Bulk Permission Setup

Make all shell scripts executable at once:

```bash
# Using uv
uv run make_executable.py

# Or install and run as a script
uv run make-executable
```

---

## 📋 Available Scripts

### 1. `switch_git_user.sh`

Switches between different Git user configurations defined in `data/git_user_configs.json`.

**Current configurations:**

- `@username` (username@example.com)
- `@username2` (username2@example.com)

### 2. `reset_intellijidea.sh`

Resets IntelliJ IDEA settings and caches. Useful for resolving IDE issues.

### 3. `reset_navicate.sh`

Resets Navicat database connection settings and caches.

---

## 🎮 Interactive Interface

The application provides an intuitive radio-button interface:

- **↑/↓ Arrow Keys:** Navigate between scripts
- **→ Arrow Key:** Select a script (radio button selection)
- **Enter:** Run the selected script
- **q:** Quit the application

Example interface:

```
Use ↑/↓ to move, → to select, Enter to run, q to quit.

> [x] switch_git_user.sh
  [ ] reset_intellijidea.sh
  [ ] reset_navicate.sh

Navigate with arrow keys. Select with →, run with Enter, quit with q.
```

---

## 🔧 Configuration

### Git User Configurations

Edit `data/git_user_configs.json` to add or modify Git user profiles:

**Note:** If the `git_user_configs.json` file doesn't exist, copy from `data/git_user_configs_example.json` to `data/git_user_configs.json` and modify according to your needs.

```json
[
  {
    "name": "Your Name",
    "email": "your.email@example.com"
  }
]
```

### Adding New Scripts

1. Place your `.sh` script in the `shell_file/` directory
2. Make sure the script has proper shebang (`#!/bin/bash`) and permissions
3. The script will automatically appear in the selection interface

---

## 🛡️ Security Features

- **Permission Confirmation:** Always asks before making files executable
- **Error Handling:** Graceful error handling with informative messages
- **Safe Execution:** Scripts run in a controlled environment
- **Input Validation:** Proper validation of user inputs

---

## 🔧 Development

### Project Setup

```bash
# Install development dependencies
uv sync

# Run the main application
uv run main.py

# Run the permission utility
uv run make_executable.py
```

### Dependencies

- **Python 3.11.11+:** Modern Python features and performance
- **Standard Library Only:** No external dependencies required
- **uv:** Modern Python package management

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 🐛 Troubleshooting

### Common Issues

**Script not executable:**

- Run `uv run make-executable` to set up permissions
- Or manually run `chmod +x shell_file/your_script.sh`

**Permission denied:**

- Ensure you have write permissions to the `shell_file/` directory
- Check that the script files are not read-only

**Script not found:**

- Verify the script exists in the `shell_file/` directory
- Check that the file has a `.sh` extension

---

## 📞 Support

For issues, questions, or contributions, please open an issue on the project repository.

</div>

---
