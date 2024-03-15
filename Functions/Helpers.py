def classify_broker(broker: str) -> str:
    broker = broker.lower()
    broker_list = ['Proaktiv', 'Aktiv', 'DNB Eiendom', 'EIE Eiendomsmegling', 'Eiendomsmegler 1',
                   'Heimdal Eiendomsmegling', 'Krogsveen', 'Lokalmegleren', 'Meglerhuset Nylander',
                   'Privatmegleren', 'Propr']

    for i in range(len(broker_list)):
        if broker_list[i].lower() in broker:
            return broker_list[i]
    return 'Other'