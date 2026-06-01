# DevSecOps API Security Lab

## Secure API Development, Security Testing, Remediation & Validation

This project demonstrates a complete DevSecOps workflow by building, testing, securing, and validating a vulnerable containerized API.

The project begins with intentionally insecure API endpoints and progresses through vulnerability discovery, automated security scanning, remediation, validation, and security automation using industry-standard DevSecOps tools.

---

## Architecture

![Architecture Diagram](architecture/devsecops-api-security-lab-architecture.png)

### Architecture Components

* User / Tester
* Nginx Reverse Proxy
* Flask API (Docker)
* JWT Authentication
* Role-Based Access Control (RBAC)
* Environment Variable Secret Management
* GitHub Actions Security Pipeline
* OWASP ZAP Runtime Validation

---

## Technologies Used

### Application & Infrastructure

* Python
* Flask
* Docker
* Docker Compose
* Nginx

### Security Tools

* Bandit
* pip-audit
* GitLeaks
* Trivy
* OWASP ZAP

### DevSecOps

* GitHub Actions
* Secure SDLC
* Security Automation
* CI/CD Security Controls

---

## Project Objectives

* Build an intentionally vulnerable API
* Identify security weaknesses using automated security tools
* Remediate discovered vulnerabilities
* Validate fixes through re-testing
* Implement DevSecOps security automation
* Demonstrate Secure Software Development Lifecycle (SSDLC) practices

---

## Initial Vulnerabilities

### Broken Object Level Authorization (BOLA)

Users could access other user records without authorization.

**Example**

```bash
curl http://127.0.0.1:8000/users/2
```

---

### Broken Function Level Authorization

Administrative endpoints were accessible without proper authorization.

**Example**

```bash
curl http://127.0.0.1:8000/admin
```

---

### Sensitive Data Exposure

Application secrets and user information were exposed through insecure endpoints.

---

### Hardcoded Secrets

JWT secrets and API keys were stored directly in source code.

---

### Missing Security Headers

The application lacked common HTTP security protections.

---

## Security Assessment

### Bandit (SAST)

Identified:

* Hardcoded secrets
* Debug mode enabled
* Insecure runtime configuration

---

### pip-audit

Identified:

* Flask vulnerabilities
* PyJWT vulnerabilities
* Werkzeug vulnerabilities

---

### Trivy

Identified:

* Python package vulnerabilities
* Container OS vulnerabilities

---

### OWASP ZAP

Identified:

* Missing security headers
* Content Security Policy weaknesses
* Server information disclosure

---

## Remediation Activities

### Authentication & Authorization

Implemented:

* JWT Authentication
* Authorization middleware
* Role-Based Access Control (RBAC)

---

### Secret Management

Removed hardcoded secrets from source code and migrated them to:

```text
.env
```

using:

```python
python-dotenv
```

---

### Password Security

Implemented password hashing using:

```python
werkzeug.security
```

---

### Security Headers

Implemented:

* Content-Security-Policy
* X-Content-Type-Options
* X-Frame-Options
* Referrer-Policy

---

### Reverse Proxy Security

Implemented Nginx reverse proxy to:

* Hide application framework details
* Centralize security headers
* Improve production readiness

---

### Dependency Remediation

Upgraded vulnerable packages:

* Flask
* PyJWT
* Werkzeug

---

## Security Validation Results

| Security Control             | Before   | After    |
| ---------------------------- | -------- | -------- |
| Bandit Findings              | 6        | 0        |
| pip-audit Vulnerabilities    | 9        | 0        |
| Trivy Python Vulnerabilities | 8        | 0        |
| ZAP Header Findings          | Multiple | Reduced  |
| Debug Endpoint               | Exposed  | Removed  |
| BOLA Vulnerability           | Present  | Fixed    |
| Admin Authorization          | Missing  | Enforced |
| Hardcoded Secrets            | Present  | Removed  |

---

## GitHub Actions Security Pipeline

The CI/CD pipeline automatically performs:

1. Bandit SAST Scan
2. pip-audit Dependency Scan
3. GitLeaks Secret Scan
4. Docker Image Build
5. Trivy Container Scan

Pipeline Location:

```text
.github/workflows/security-pipeline.yml
```

---

## Security Improvements Implemented

* Debug endpoint removed
* BOLA vulnerability remediated
* Admin authorization enforced
* Password hashing implemented
* Secrets moved to environment variables
* Dependency vulnerabilities remediated
* Security headers implemented
* Nginx reverse proxy deployed
* Security scanning automated through GitHub Actions

---

## Project Structure

```text
devsecops-api-security-lab/
│
├── app/
├── nginx/
├── architecture/
│   └── devsecops-api-security-lab-architecture.png
├── reports/
├── screenshots/
├── .github/
│   └── workflows/
│       └── security-pipeline.yml
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Key Skills Demonstrated

* DevSecOps
* API Security
* Secure SDLC
* Authentication & Authorization
* RBAC Implementation
* Secret Management
* Password Hashing
* Container Security
* Dependency Management
* Vulnerability Assessment
* Security Remediation
* CI/CD Security Automation
* Docker Security
* Nginx Reverse Proxy Configuration
* OWASP Top 10
* Runtime Security Validation

---

## Security Tools Used

| Tool           | Purpose                                     |
| -------------- | ------------------------------------------- |
| Bandit         | Static Application Security Testing (SAST)  |
| pip-audit      | Dependency Vulnerability Scanning           |
| GitLeaks       | Secret Scanning                             |
| Trivy          | Container Vulnerability Scanning            |
| OWASP ZAP      | Dynamic Application Security Testing (DAST) |
| GitHub Actions | Security Automation                         |
| Docker         | Containerization                            |
| Nginx          | Reverse Proxy & Security Headers            |


