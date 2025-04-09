def parse_alerts(alerts):
    parsed = []
    for alert in alerts:
        parsed.append({
            'name': alert['alert'],
            'risk': alert['risk'],
            'desc': alert['description'],
            'solution': alert['solution']
        })
    return parsed
