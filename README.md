# Ansible Role postfix mailrelay

This role installs and configures a postfix mailrelay.

Ofter times, applications or services will want to send out e-mails.
This role will configure any such server to queue mails locally and then
forwarding them to any specific mail-relay.

This way, applications and services on such a configured instance don't
require any special send/relay/bounce logic and can simply use mail-drop
to reliably send out e-mails.

The variables used by this role should be self-explanatory for anyone
with a Postfix background.

# Example play

```yaml
- hosts: mx-relays
  vars:
    mailrelay_default_sender_email: "server@example.com"
    mailrelay_default_sender_user: "ServerExampleCom"
    mailrelay_default_sender_password: "verylongpassword"
    mailrelay_default_sender_server: "smtp.gmail.com"
    mailrelay_default_sender_server_port: "587"
    mailrelay_default_monitoring_recipient: "monitoring-alerts@exampe.com"
    
    # Set to False to disable or to 'mail@example.com' to receive bounce mails
    mailrelay_bounce_notice_recipient: False
    
    # Sending address to sending server association
    mailrelay_relayhost_maps:
      - name: "{{ mailrelay_default_sender_email }}"
        target: "[{{ mailrelay_default_sender_server }}]:{{ mailrelay_default_sender_server_port }}"
      - name: "example@gmail.com"
        target: "[smtp.gmail.com]:587"
    
    # Sending address - user:password association
    mailrelay_sasl_passwords:
      - name: "{{ mailrelay_default_sender_email }}"
        target: "{{ mailrelay_default_sender_user }}:{{ mailrelay_default_sender_password }}"
      - name: "subscribe@example.com"
        target: "SubscribeExampleCom:secretpass"
    
    # Sending Linux user - sender address rewriting, http://www.postfix.org/ADDRESS_REWRITING_README.html
    mailrelay_sender_canonical_maps:
      # Note that it "seems" possible to rewrite every account using a regex like:
      # /etc/postfix/sender-canonical-maps.regex
      # /.*/    masqueraded@example.com
      # However this calls for some unexpected behavior and loops with mails to fo@bar.comcom and so on, so I don't recommend it
      - name: "root"
        target: "{{ mailrelay_default_sender_email }}"
      - name: "www_example_com"
        target: "{{ mailrelay_default_sender_email }}"
    
    # When those linux users receive
    mailrelay_aliases:
      # Relay mails to the root use to the default_monitoring_recipient
      - name: root
        target: "{{mailrelay_default_monitoring_recipient }}"

  roles:
    - blunix.role-mailrelay
```

# License

Apache-2.0

# License

Apache-2.0

# Author Information

Service and support for orchestrated hosting environments,
continuous integration/deployment/delivery and various Linux
and open-source technology stacks are available from:

```
Blunix GmbH - Consulting for Linux Hosting 24/7
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: service[at]blunix.org
Phone: (+49) 30 / 12 08 39 90
```
