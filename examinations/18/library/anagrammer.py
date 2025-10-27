#!/usr/bin/python
# -*- coding: utf-8 -*-

# ============================================================
# Ansible-modul: anagrammer
# Syfte: Ta emot en sträng (message), vända den, och returnera
# original + omvänd version. Markerar "changed" om de skiljer sig.
# ============================================================

# Importera AnsibleModule från ansible.module_utils.basic
# Detta är basen för alla Ansible-moduler och hanterar
# argument, felhantering och JSON-output till Ansible
from ansible.module_utils.basic import AnsibleModule

def run_module():
    # ------------------------------------------------------------
    # Definiera de parametrar som modulen tar emot från användaren
    # ------------------------------------------------------------
    module_args = dict(
        message=dict(type='str', required=True)  # message är obligatorisk och ska vara en sträng
    )

    # ------------------------------------------------------------
    # Skapa en instans av AnsibleModule
    # ------------------------------------------------------------
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False  # Vi kan inte göra "check mode" här
        # check mode används för att "torrkörning" utan att ändra något.
        # Eftersom modulen alltid räknar ut strängar och ändrar 'changed' dynamiskt,
        # finns ingen meningsfull "torrkörning". Därför False.
    )

    # Hämta parametern som användaren skickade in
    message = module.params['message']

    # Skapa den omvända versionen av meddelandet
    reversed_message = message[::-1]  # Python-syntax för att vända en sträng

    # Sätt 'changed' True om meddelandet och den omvända skiljer sig
    changed = message != reversed_message

    # ------------------------------------------------------------
    # Speciell fail-case: Om message == "fail me", avbryt modulen
    # ------------------------------------------------------------
    if message == "fail me":
        module.fail_json(
            msg="You requested this to fail",
            changed=True,
            original_message=message,
            reversed_message=reversed_message
        )

    # ------------------------------------------------------------
    # Returnera resultatet till Ansible
    # ------------------------------------------------------------
    module.exit_json(
        changed=changed,
        original_message=message,
        reversed_message=reversed_message
    )

# Kör modulen
def main():
    run_module()

if __name__ == '__main__':
    main()

# ============================================================
# SAMMANFATTNING (för nybörjare)
#
# 1. AnsibleModule: Basen för alla moduler. Hanterar argument,
#    felhantering och returnerar JSON till Ansible.
# 2. module_args: Här definierar vi vilka parametrar användaren
#    kan skicka in. I detta fall 'message' som är en sträng.
# 3. message[::-1]: Python-syntax för att vända en sträng.
# 4. changed: True om original och reversed skiljer sig, annars False.
# 5. fail_json(): Avbryter modulen med fel om något går fel.
# 6. exit_json(): Returnerar resultatet till Ansible när allt gått bra.
# 7. supports_check_mode=False: Vi kan inte göra "torrkörning" här,
#    eftersom modulen dynamiskt beräknar 'changed' och det inte finns
#    något faktiskt system som ändras.
# ============================================================
