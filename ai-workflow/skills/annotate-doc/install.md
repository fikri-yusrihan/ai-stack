# Install Plannotator

Use the official Plannotator installer in binary-only mode. This gives the annotation skills a CLI while leaving agent settings and hooks alone. Install only when the user requests it. These examples use GitHub CLI (`gh`) to verify the downloaded binary's provenance. [Official installation and verification instructions](https://github.com/backnotprop/plannotator#install)

## macOS, Linux or WSL

Download and inspect the installer before running it. Run the second block after reviewing the script and confirming `gh` is available.

```sh
plannotator_install_dir=$(mktemp -d)
curl -fsSL https://plannotator.ai/install.sh -o "$plannotator_install_dir/install.sh"
```

```sh
bash "$plannotator_install_dir/install.sh" --minimal --verify-attestation --non-interactive
plannotator --version
```

## Windows PowerShell

Download the installer to a fresh temporary directory and inspect the script. Run the second block after reviewing it and confirming `gh` is available.

```powershell
$PlannotatorInstallDir = Join-Path ([IO.Path]::GetTempPath()) ([guid]::NewGuid().ToString())
New-Item -ItemType Directory -Path $PlannotatorInstallDir | Out-Null
$PlannotatorInstaller = Join-Path $PlannotatorInstallDir 'install.ps1'
Invoke-WebRequest -Uri 'https://plannotator.ai/install.ps1' -OutFile $PlannotatorInstaller
```

```powershell
& $PlannotatorInstaller -Minimal -VerifyAttestation -NonInteractive
plannotator --version
```

If the command is missing after a successful install, follow the installer's PATH instructions or open a new shell and check again. Report an installation or attestation failure before retrying. Follow the upstream release notes if you need to pin a version. [Releases](https://github.com/backnotprop/plannotator/releases)
