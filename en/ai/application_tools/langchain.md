---
title: "langchain"
lang: en
category: "AI/Application Software Stack"
source_page: https://www.spacemit.com/community/document/info?nodepath=ai/application_tools/langchain.md&lang=en
source_file: https://cdn-resource.spacemit.com/ai/docs-ai/en/application_tools/langchain.md
updated: "2026-05-28 16:39:08"
---
# langchain

## Platform Support

| Platform & System | Support |
| --- | --- |
| K1 Buildroot | ❌ Not supported |
| K1 OpenHarmony | ❌ Not supported |
| K1 Bianbu LXQT/GNOME | ✅ Supported |
| K3 Buildroot | ❌ Not supported |
| K3 OpenHarmony | ❌ Not supported |
| K3 Bianbu LXQT/GNOME | ✅ Supported |

## Installation

### 1.1 Install dependencies

Install the basic dependencies:

```bash
sudo apt update
sudo apt install python3-venv libffi-dev libssl-dev pkg-config
```

Install Rust:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain stable
source ~/.cargo/env
rustc --version
```

If you see output similar to the following, the installation was successful:
![Rust installation output](../../../_assets/docs-ai/static/rust-install.png)

### 1.2 Install LangChain

```bash
python3 -m venv ./langchain_venv
source langchain_venv/bin/activate
pip install langchain  -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## Usage

```bash
source langchain_venv/bin/activate
python -c "import langchain; print(langchain.__version__)"
```

![LangChain demo output](../../../_assets/docs-ai/static/langchain-demo.png)
