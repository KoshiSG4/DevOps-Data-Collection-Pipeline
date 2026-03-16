# DevOps Data Collection Pipeline

A comprehensive DevOps data collection pipeline that aggregates, normalizes, and stores DevOps metrics from multiple sources such as GitHub, GitLab, CI/CD tools, and Jira. This pipeline leverages Apache Airflow for orchestration and Apache DevLake for normalization and storage, providing a unified view of development, deployment, and operational metrics.

---

## Table of Contents

- [Architecture](#architecture)
- [Main Components](#main-components)
- [Build Plan](#build-plan)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Monitoring and Alerting](#monitoring-and-alerting)
- [Contributing](#contributing)
- [License](#license)

---

## Architecture

---

## Main Components

| Component            | Technology                  | Concepts / Features                                  |
| -------------------- | --------------------------- | ---------------------------------------------------- |
| Orchestrator         | Apache Airflow              | DAG, Task, Operator, Scheduler, Executor             |
| Collectors           | GitHub, GitLab, CI/CD, Jira | REST APIs, Authentication (tokens, OAuth),           |
|                      |                             | Pagination, Rate Limits, Python `requests`/`httpx`   |
| Transformation Layer | Apache DevLake              | DevLake Plugins, Data Models, Extractors, Converters |
| Storage              | DevLake DB                  | Data Normalization, Unified DevOps Schema            |
| Status Reporting     | PlatformNex                 | Airflow Failure Handling, Pipeline Metadata          |
| Alerting             | Slack / Email / Teams       | Failure Notifications                                |

## Build Plan

### 1. Environment Setup

    - **Tool:** Apache DevLake
    - **Goal:** Deploy DevLake backend, database, and dashboards
    - **Method:** Use Docker to run DevLake components

### 2. Pipeline Orchestration

    - **Tool:** Apache Airflow
    - **Goal:** Schedule and orchestrate data collection
    - **Method:** Install Airflow, create DAGs for tasks

### 3. Git Data Collection

    - **Tool:** GitHub APIs
    - **Goal:** Collect commits, PRs, and issues
    - **Method:** Airflow tasks call APIs with authentication

### 4. CI/CD Data Collection

    - **Tool:** GitHub Actions
    - **Goal:** Collect build and deployment status
    - **Method:** Airflow tasks call CI/CD APIs

### 4. CI/CD Data Collection

    - **Tool:** GitHub Actions
    - **Goal:** Collect build and deployment status
    - **Method:** Airflow tasks call CI/CD APIs

### 5. Jira / Incident Collection

    - **Tool:** GitHub Projects
    - **Goal:** Collect issues, incident data
    - **Method:** Airflow tasks call APIs

### 6. Cloud Log Collection

    - **Tool:** Google Cloud Logging → BigQuery
    - **Goal:** Efficiently store large log datasets
    - **Method:** Export logs to BigQuery, Airflow reads them

### 7. Data Normalization

    - **Tool:** Apache DevLake
    - **Goal:** Normalize data to DevLake schema
    - **Method:** Use DevLake plugins and converters

### 8. Load into DevLake

    - **Tool:** DevLake Database
    - **Goal:** Store normalized data in the database

### 9. Pipeline Metadata

    - **Tool:** PlatformNex API
    - **Goal:** Track pipeline execution status

### 10. Failure Handling & Alerts

    - **Tool:** Slack, Teams, Email
    - **Goal:** Python function to send notifications on task failure

## Technologies

- **Airflow** – Orchestrates tasks and pipelines
- **Apache DevLake** – Normalizes and stores DevOps data
- **GitHub/GitLab API** – Collects code repository data
- **CI/CD Tools** – GitHub Actions, Jenkins, GitLab pipelines
- **Jira API** – Collects project and issue data
- **Google Cloud Logging / BigQuery** – Cloud log collection
- **Python** – Task scripting, API calls, and notifications
- **Slack / Email / Teams** – Alerting and notifications

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/devops-data-pipeline.git
cd devops-data-pipeline
```

2. Run DevLake using Docker:

```bash
docker-compose up -d
```

3. Install Airflow:

```bash
pip install apache-airflow
airflow db init
```

4. Configure DAGs in airflow/dags/ for Git, CI/CD, Jira, and logs collection.

5. Set environment variables for API tokens and credentials:

```bash
export GITHUB_TOKEN=<your-token>
export JIRA_TOKEN=<your-token>
```

6. Start the Airflow scheduler and webserver:

```bash
airflow scheduler
airflow webserver
```

7. Configure Slack/Email notifications in alerts.py.

## Usage

- Navigate to the Airflow UI to monitor DAG runs.
- Check PlatformNex for pipeline execution status.
- View normalized DevOps metrics on the DevLake dashboard.

## Monitoring and Alerting

- Task failures trigger Slack or Email alerts.
- Airflow provides detailed logs for debugging and auditing.
- PlatformNex tracks pipeline execution success/failure for reporting.
