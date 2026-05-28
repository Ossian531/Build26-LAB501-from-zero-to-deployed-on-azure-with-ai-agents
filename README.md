# 🚀 Get Started

**This repo is where attendees go to continue their learning after your session — and your Copilot agent will help you set it up.**

### Step 1: Open your repo

Open this repo in a **Codespace** (click the green **Code** button → **Create a Codespace**) — or clone it locally. Then open **GitHub Copilot Chat**.

### Step 2: Add your content

Give the agent something to work with. Drag files into the Explorer panel — session abstracts, outlines, screenshots, notes — and drop them in one of two places:

| Where to put it | What goes there | Who sees it |
|---|---|---|
| **`_remove-before-publish/`** | Internal reference materials (abstracts, outlines, screenshots, planning docs) | **Copilot only** — never published |
| **`/docs/`, `/src/`, or repo root** | Lab instructions, demo code, sample data, getting-started guides | **Attendees** — published with the repo |

> 💡 Not sure? Start by dropping your session abstract or outline into `_remove-before-publish/`. The agent will figure out what to do with it.

### Step 3: Ask the Agent

Once your content is in the repo, use these three phrases with Copilot to build out your session repo:

| Phrase to use with Copilot | What it does | When to run it |
|---|---|---|
| **"Help me get started"** | Sets up session title, description, outcomes, and owners | After you've added your session abstract or outline to the repo |
| **"Help me refine content"** | Organizes your session content into the repo | Each time you add or update content |
| **"Help me finalize"** | Final review, cleanup, and publication prep | When you're ready to publish |

> 💡 **These three phrases are just the starting point.** Copilot can do much more — try asking it to brainstorm next steps for attendees, generate code samples, or build out your repo structure. Don't be afraid to put it in plan mode and ask for what you need.

---

<p align="center">
<img src="img/banner-build-26.png" alt="Microsoft Build 2026" width="1200"/>
</p>

# [Microsoft Build 2026](https://build.microsoft.com)

## 🔥 LAB501: From Zero to Deployed on Azure with AI Agents

### Session Description

What happens when you let AI agents do the building? In this hands-on lab, you'll go from an empty terminal to a deployed app on Azure — with GitHub Copilot CLI and coding agents handling the scaffolding, coding, debugging, and deployment. You'll use the new Azure skills to provision resources and wire up services through natural language, no portal required. This isn't a demo you watch. You'll walk out with a real, working dev workflow you can take straight to your next project.

Across 75 minutes (Level 300), you'll ship a Python Flask LEGO set browser to Azure Container Apps backed by Azure Cosmos DB, then put on your architect hat and evaluate the AI's decisions: review the generated Bicep, harden the deployment, break it on purpose, and run a full forensic investigation with KQL — all from GitHub Copilot CLI.

### 🏫 Getting started in a guided session

To get started in a guided lab session:
- Sign in to your Skillable lab VM and start **Docker Desktop**
- Open PowerShell and run `az login`, `azd auth login`, then `copilot` — follow [Login & Launch](docs/lab-instructions/02-login-and-launch.md) to install the **Azure Skills** plugin (`/plugin install azure@azure-skills`)
- Follow the [Lab Overview](docs/lab-instructions/00-overview.md) and work through the four scenarios in order

### 🏠 Getting started in your own environment

If you're following these steps at your own pace:
- Clone this repository: `git clone https://github.com/microsoft/Build26-LAB501.git`
- Install the [prerequisites](docs/lab-instructions/01-prerequisites.md): Python 3.13+, Docker Desktop, Git, Azure CLI (with Bicep), Azure Developer CLI (`azd`), GitHub Copilot CLI, and an Azure subscription with Contributor access
- Provision your own Azure Cosmos DB with the LEGO dataset (database `LegoDatabase`, container `legoSets`), then start at [Set Up the Starter App](docs/lab-instructions/03-getting-started.md) and work through the four scenarios

### 🧠 Learning Outcomes

By the end of this session, you will be able to:

- Chain Azure skills (`azure-prepare` → `azure-validate` → `azure-deploy`) from a single natural-language prompt in GitHub Copilot CLI to scaffold IaC, Docker, and config and ship a containerized app to Azure
- Critically review AI-generated Bicep, Dockerfiles, and architecture diagrams — spot the production gaps and use `azure-rbac` and `azure-resource-visualizer` to close them with least-privilege managed identity and accurate documentation
- Triage and operationalize production issues with `azure-diagnostics` — follow its reasoning chain from system logs to root cause, then turn the post-mortem into KQL queries and alert rules without ever opening the Azure Portal

### 💬 Keep Learning with Copilot

Try these prompts with GitHub Copilot to explore the topics from this session. Open Copilot Chat in VS Code (`Ctrl+Alt+I` on Windows/Linux, `Cmd+Shift+I` on Mac), paste a prompt, and see what you learn. Try connecting the [Microsoft Learn MCP Server](#-microsoft-learn-mcp-server) for the latest official documentation.

Use these as a starting point — or write your own!

- "Scaffold a Python Flask app on Azure Container Apps with Bicep and `azd`, using a system-assigned managed identity to pull images from ACR."
- "Review my Container App Bicep for production-readiness gaps — managed identity, RBAC, VNet integration, diagnostic settings, and health probes — and propose fixes."
- "Find the minimum-privilege Cosmos DB RBAC role for an app that only reads data, and generate the `az cosmosdb sql role assignment create` command."
- "Visualize the resources in my resource group as a Mermaid architecture diagram, including cross-resource-group dependencies like Cosmos DB."
- "My Container App is returning 503. Pull system logs, correlate with ingress configuration, and tell me the root cause and fix."
- "Write a KQL query against `ContainerAppSystemLogs_CL` that calculates downtime between the first `ProbeFailed` event and the next `RevisionReady` event, then turn it into an `az monitor scheduled-query create` alert rule."

### 💻 Technologies Used

1. GitHub Copilot CLI + Azure Skills plugin (`azure-prepare`, `azure-validate`, `azure-deploy`, `azure-rbac`, `azure-resource-visualizer`, `azure-diagnostics`) and the Azure MCP Server
2. Azure Container Apps, Azure Container Registry, and Azure Cosmos DB (NoSQL) with managed identity + RBAC
3. Azure Developer CLI (`azd`), Bicep, Docker, Python 3.13 / Flask, Azure Monitor + Log Analytics, and KQL

### 📚 Resources and Next Steps

| Resource | Description |
|:---------|:------------|
| [https://aka.ms/build26-next-steps](https://aka.ms/build26-next-steps) | Take the next step in your learning journey after Build 2026 |
| [Lab Overview](docs/lab-instructions/00-overview.md) | Architecture diagram, skills map, and section-by-section lab guide |
| [What's Next](docs/lab-instructions/09-whats-next.md) | Extension ideas — private endpoints, VNet integration, Key Vault, CI/CD with OIDC, Terraform |
| [Announcing the Azure Skills Plugin](https://devblogs.microsoft.com/all-things-azure/announcing-the-azure-skills-plugin/) | Background on the Azure skills used throughout the lab |
| [Azure MCP Server docs](https://learn.microsoft.com/azure/developer/azure-mcp-server) | Reference for the MCP tools that power the Azure skills |
| [GitHub Copilot CLI docs](https://docs.github.com/en/copilot/github-copilot-in-the-cli) | Install, configure, and extend GitHub Copilot CLI |
| [Deploy and manage Container Apps](https://learn.microsoft.com/training/paths/deploy-manage-container-apps) | Microsoft Learn path for Azure Container Apps |
| [Azure Cosmos DB documentation](https://learn.microsoft.com/azure/cosmos-db) | Data modeling, RBAC, and operational guidance for Cosmos DB |


### 🌟 Microsoft Learn MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D)

The Microsoft Learn MCP Server is a remote MCP Server that enables clients like GitHub Copilot and other AI agents to bring trusted and up-to-date information directly from Microsoft's official documentation. Get started by using the one-click button above for VSCode or access the [mcp.json](.vscode/mcp.json) file included in this repo.

For more information, setup instructions for other dev clients, and to post comments and questions, visit our Learn MCP Server GitHub repo at [https://github.com/MicrosoftDocs/MCP](https://github.com/MicrosoftDocs/MCP). Find other MCP Servers to connect your agent to at [https://mcp.azure.com](https://mcp.azure.com).

*Note: When you use the Learn MCP Server, you agree with [Microsoft Learn](https://learn.microsoft.com/en-us/legal/termsofuse) and [Microsoft API Terms](https://learn.microsoft.com/en-us/legal/microsoft-apis/terms-of-use) of Use.*

## Content Owners

<!-- TODO: Add yourself as a content owner
1. Change the src in the image tag to {your github url}.png
2. Change INSERT NAME HERE to your name
3. Change the github url in the final href to your url. -->

<table>
<tr>
    <td align="center"><a href="http://github.com/yourGitHubHandle">
        <img src="https://github.com/yourGitHubHandle.png" width="100px;" alt="INSERT NAME HERE"/><br />
        <sub><b>INSERT NAME HERE</b></sub></a><br />
            <a href="https://github.com/yourGitHubHandle" title="talk">📢</a>
    </td>
</tr></table>

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit [Contributor License Agreements](https://cla.opensource.microsoft.com).

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
