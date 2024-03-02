matches = [
    {
        'home_team': 'Bolivia',
        'away_team': 'Uruguay',
        'home_team_score': 3,
        'away_team_score': 1,
        'home_team_result': 'Win'
    },
    {
        'home_team': 'Brazil',
        'away_team': 'México',
        'home_team_score': 1,
        'away_team_score': 1,
        'home_team_result': 'Draw'
    },
    {
        'home_team': 'Ecuador',
        'away_team': 'Venezuela',
        'home_team_score': 5,
        'away_team_score': 0,
        'home_team_result': 'Win'
    }
]

winners = list(filter(lambda item: item['home_team_result'] == 'Win', matches))
country_winners = list(map(lambda item: item['home_team'], winners))
print(f'Datos ganadores => {winners}')
print(f'Cantidad = {len(winners)}')
print(f'Equipos ganadores => {country_winners}')