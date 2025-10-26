# Roll: compliance_check

Denna roll utför **icke-invasiva säkerhetskontroller** baserade på *CIS Benchmark för AlmaLinux 10* (nivå 1).

Syftet är att verifiera att systemen följer grundläggande säkerhetskrav — utan att ändra något i systemet.

## Funktioner
- Utför endast kontroller (read-only), inga förändringar
- Baserad på Ansible-moduler: `package_facts`, `service_facts`, `stat` och `assert`
- Rapporterar tydligt om varje kontroll är godkänd eller inte
- Kan köras mot både webbserver- och databasserver-VM

## Exempel på användning

```yaml
- hosts: all
  roles:
    - compliance_check
